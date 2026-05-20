\# AI-First CRM – HCP Interaction Logger



\## Overview

An AI-powered CRM system for logging Healthcare Professional (HCP) interactions using natural language via chat or structured form.



\## Tech Stack

\- Frontend: React + Redux

\- Backend: Python FastAPI

\- AI Agent: LangGraph + Groq (llama-3.3-70b-versatile)

\- Database: MySQL



\## How to Run



\### Backend

cd backend

pip install -r requirements.txt

uvicorn main:app --reload --port 8000



\### Frontend

cd frontend

npm install

npm start



\### Environment Variables

Create backend/.env file with:

GROQ\_API\_KEY=your\_groq\_api\_key

DB\_URL=mysql+pymysql://root:yourpassword@localhost/hcp\_crm



\## 5 LangGraph Tools

1\. log\_interaction - Extracts and saves interaction from natural language

2\. edit\_interaction - Modifies existing logged data

3\. search\_hcp\_history - Retrieves past interactions for an HCP

4\. suggest\_followup - AI generated follow-up recommendations

5\. analyze\_sentiment - Classifies interaction sentiment

