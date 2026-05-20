from langchain_groq import ChatGroq
from langchain.tools import tool
from database import SessionLocal
from models import HCPInteraction
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0, api_key=os.getenv("GROQ_API_KEY"))

def extract_json(text):
    try:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except:
        pass
    return {}

@tool
def log_interaction(summary: str) -> str:
    """Extract interaction details from natural language and save to database."""
    try:
        extraction_prompt = f"""Extract these fields from this text and return ONLY a JSON object:
hcp_name (doctor name), interaction_type (Meeting/Call/Email), topics_discussed, materials_shared, sentiment (Positive/Neutral/Negative).
Text: {summary}
Return only JSON, no explanation."""
        response = llm.invoke(extraction_prompt)
        data = extract_json(response.content)
        if not data:
            data = {
                "hcp_name": "Unknown",
                "interaction_type": "Meeting",
                "topics_discussed": summary,
                "materials_shared": "",
                "sentiment": "Neutral"
            }
        db = SessionLocal()
        safe_data = {k: v for k, v in data.items() if k in [
            'hcp_name','interaction_type','topics_discussed',
            'materials_shared','sentiment','outcomes','follow_up_actions'
        ]}
        interaction = HCPInteraction(**safe_data)
        db.add(interaction)
        db.commit()
        db.refresh(interaction)
        interaction_id = interaction.id
        db.close()
        return json.dumps({"success": True, "id": interaction_id, "data": safe_data})
    except Exception as e:
        return json.dumps({"error": str(e)})

@tool
def edit_interaction(interaction_id: str, updates: str) -> str:
    """Edit a previously logged HCP interaction by ID."""
    try:
        db = SessionLocal()
        record = db.query(HCPInteraction).filter(
            HCPInteraction.id == int(interaction_id)
        ).first()
        if not record:
            return json.dumps({"error": "Interaction not found"})
        updates_dict = extract_json(updates) if isinstance(updates, str) else updates
        for key, value in updates_dict.items():
            if hasattr(record, key):
                setattr(record, key, value)
        db.commit()
        db.close()
        return json.dumps({"success": True, "message": f"Interaction {interaction_id} updated"})
    except Exception as e:
        return json.dumps({"error": str(e)})

@tool
def search_hcp_history(hcp_name: str) -> str:
    """Retrieve all past interactions with a specific HCP."""
    try:
        db = SessionLocal()
        records = db.query(HCPInteraction).filter(
            HCPInteraction.hcp_name.ilike(f"%{hcp_name}%")
        ).all()
        db.close()
        return json.dumps([{
            "id": r.id,
            "date": str(r.interaction_date),
            "topics": r.topics_discussed,
            "sentiment": r.sentiment
        } for r in records])
    except Exception as e:
        return json.dumps({"error": str(e)})

@tool
def suggest_followup(hcp_name: str, last_topics: str) -> str:
    """Suggest a follow-up action based on the last interaction."""
    try:
        prompt = f"Suggest 1 specific follow-up action for a pharma sales rep after meeting {hcp_name} about {last_topics}. Be brief."
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return str(e)

@tool
def analyze_sentiment(interaction_notes: str) -> str:
    """Analyze sentiment from interaction notes."""
    try:
        prompt = f"""Return ONLY a JSON object with these keys:
sentiment (Positive/Neutral/Negative), confidence (0.0 to 1.0), key_signals (list of 2 short phrases).
No explanation, only JSON.
Notes: {interaction_notes}"""
        response = llm.invoke(prompt)
        data = extract_json(response.content)
        if not data:
            data = {"sentiment": "Neutral", "confidence": 0.5, "key_signals": []}
        return json.dumps(data)
    except Exception as e:
        return json.dumps({"error": str(e)})