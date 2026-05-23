from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import HCPInteraction
from schemas import InteractionCreate, ChatMessage
from langchain_groq import ChatGroq
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0, api_key=os.getenv("GROQ_API_KEY"))

router = APIRouter()

def extract_json(text):
    try:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except:
        pass
    return {}

def clean_value(value):
    if isinstance(value, list):
        return ', '.join(str(v) for v in value)
    if value is None:
        return ''
    return str(value)

@router.post("/interactions")
def create_interaction(data: InteractionCreate, db: Session = Depends(get_db)):
    record = HCPInteraction(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return {"id": record.id, "message": "Interaction logged successfully"}

@router.get("/interactions")
def get_interactions(db: Session = Depends(get_db)):
    return db.query(HCPInteraction).all()

@router.put("/interactions/{id}")
def update_interaction(id: int, data: dict, db: Session = Depends(get_db)):
    record = db.query(HCPInteraction).filter(HCPInteraction.id == id).first()
    if not record:
        return {"error": "Not found"}
    for k, v in data.items():
        setattr(record, k, v)
    db.commit()
    return {"message": "Updated successfully"}

@router.post("/chat")
async def chat_with_agent(message: ChatMessage, db: Session = Depends(get_db)):
    try:
        prompt = f"""Extract these fields from this text and return ONLY a JSON object:
hcp_name (doctor name), interaction_type (Meeting/Call/Email), topics_discussed (string), materials_shared (string), sentiment (Positive/Neutral/Negative).
All values must be strings not lists.
Text: {message.text}
Return only JSON, no explanation."""

        response = llm.invoke(prompt)
        data = extract_json(response.content)

        if not data:
            data = {
                "hcp_name": "Unknown",
                "interaction_type": "Meeting",
                "topics_discussed": message.text,
                "materials_shared": "",
                "sentiment": "Neutral"
            }

        allowed_keys = ['hcp_name', 'interaction_type', 'topics_discussed',
                        'materials_shared', 'sentiment', 'outcomes', 'follow_up_actions']

        safe_data = {}
        for k, v in data.items():
            if k in allowed_keys:
                safe_data[k] = clean_value(v)

        record = HCPInteraction(**safe_data)
        db.add(record)
        db.commit()

        reply = f"✅ Interaction logged successfully! The details (HCP Name, Sentiment, and Materials) have been automatically populated based on your summary. Would you like me to suggest a follow-up action?"

        return {"reply": reply, "form_data": safe_data}

    except Exception as e:
        return {"reply": f"Error: {str(e)}"}