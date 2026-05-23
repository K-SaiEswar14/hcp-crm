# 🏥 AI-First CRM – HCP Interaction Logger

![HCP CRM Banner](https://img.shields.io/badge/AI--First%20CRM-HCP%20Module-blue?style=for-the-badge&logo=robot)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Redux](https://img.shields.io/badge/Redux-593D88?style=for-the-badge&logo=redux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)

---

## 👨‍💻 About the Developer

| | |
|---|---|
| **Name** | K. Sai Eswar |
| **Location** | Anthapuram, Andhra Pradesh, India 🇮🇳 |
| **Education** | B.Tech in CSE (AI Specialization) |
| **University** | Bharatiya Engineering Science and Technology Innovation University, Gorantla |
| **GitHub** | [@K-SaiEswar14](https://github.com/K-SaiEswar14) |

---

## 📌 Project Overview

> 🤖 An **AI-powered CRM system** designed for **Pharmaceutical Sales Representatives** to log their meetings with **Healthcare Professionals (HCPs)** using simple natural language — no more manual form filling!

In the pharmaceutical industry, sales representatives meet with doctors every single day. After each meeting they need to log interaction details. This application uses **Artificial Intelligence** to make that process fast, easy and accurate.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🗣️ **AI Chat Interface** | Type your meeting summary in plain English |
| 📋 **Auto Form Fill** | AI automatically fills all form fields |
| 💾 **Database Storage** | All interactions saved to MySQL |
| 😊 **Sentiment Detection** | Automatically detects Positive / Neutral / Negative |
| 🔍 **Search History** | Find all past interactions with any doctor |
| 💡 **Follow-up Suggestions** | AI suggests next best action |
| 📊 **Sentiment Analysis** | Analyze any text for sentiment |
| ✏️ **Edit Interactions** | Modify any previously saved interaction |

---

## 🖥️ App Screenshot

```
┌─────────────────────────────────┬──────────────────────────┐
│      Log HCP Interaction        │     🤖 AI Assistant      │
│                                 │                          │
│  HCP Name: [Dr. Smith        ]  │  ┌──────────────────┐   │
│  Type:     [Meeting    ▼     ]  │  │ Log interaction  │   │
│  Date:     [11/29/2025       ]  │  │ details here...  │   │
│  Time:     [07:36 PM         ]  │  └──────────────────┘   │
│                                 │                          │
│  Topics:   [Product X        ]  │  > Today I met with     │
│            [efficiency       ]  │    Dr. Smith...         │
│                                 │                          │
│  Sentiment:                     │  ┌──────────────────┐   │
│  ● 😊 Positive                  │  │ ✅ Interaction   │   │
│  ○ 😐 Neutral                   │  │ logged! Form     │   │
│  ○ 😞 Negative                  │  │ auto-filled!     │   │
│                                 │  └──────────────────┘   │
│  Materials: [Brochures       ]  │                          │
│                                 │  [Describe Interaction]  │
│       [💾 Save Interaction]     │              [🤖 Log]   │
└─────────────────────────────────┴──────────────────────────┘
```

---

## 🛠️ Tech Stack

### 🎨 Frontend
- ⚛️ **React** — UI Framework
- 🔄 **Redux + Redux Toolkit** — State Management
- 🌐 **Axios** — API calls
- 🔤 **Inter Font** — Google Fonts

### ⚙️ Backend
- 🐍 **Python** — Programming Language
- ⚡ **FastAPI** — REST API Framework
- 🗄️ **SQLAlchemy** — Database ORM
- 🔐 **Python Dotenv** — Environment Variables

### 🤖 AI / ML
- 🦜 **LangGraph** — AI Agent Framework
- 🧠 **Groq LLM** — llama-3.3-70b-versatile Model
- 🔗 **LangChain** — LLM Integration

### 🗃️ Database
- 🐬 **MySQL** — Relational Database

---

## 🤖 5 LangGraph AI Tools

```
🔧 Tool 1 — log_interaction
   ➜ Extracts doctor name, sentiment, topics from natural language
   ➜ Saves interaction directly to MySQL database
   ➜ Auto-fills the React form via API response

🔧 Tool 2 — edit_interaction
   ➜ Modifies any previously saved interaction by ID
   ➜ Updates specific fields without changing others
   ➜ Confirms update with success message

🔧 Tool 3 — search_hcp_history
   ➜ Searches database for all past interactions
   ➜ Filters by doctor name using fuzzy search
   ➜ Returns date, topics and sentiment history

🔧 Tool 4 — suggest_followup
   ➜ Takes doctor name and topics discussed
   ➜ Uses LLM to suggest best next action
   ➜ Helps sales reps stay organized

🔧 Tool 5 — analyze_sentiment
   ➜ Analyzes any text or notes
   ➜ Returns Positive / Neutral / Negative
   ➜ Includes confidence score and key signals
```

---

## 📁 Project Structure

```
hcp-crm/
│
├── 📂 backend/
│   ├── 📂 agent/
│   │   ├── 🤖 graph.py          # LangGraph agent graph
│   │   ├── 🔧 tools.py          # 5 LangGraph tools
│   │   └── 📄 __init__.py
│   ├── 📂 routers/
│   │   ├── 🛣️ interactions.py   # API routes
│   │   └── 📄 __init__.py
│   ├── 🗄️ database.py           # SQLAlchemy setup
│   ├── 📊 models.py             # Database models
│   ├── 📝 schemas.py            # Pydantic schemas
│   ├── 🚀 main.py               # FastAPI app entry
│   └── 🔐 .env                  # Environment variables
│
├── 📂 frontend/
│   └── 📂 src/
│       ├── 📂 components/
│       │   ├── 💬 AIAssistant.jsx        # Chat panel
│       │   └── 📋 LogInteractionForm.jsx # Form panel
│       ├── 📂 redux/
│       │   ├── 🏪 store.js               # Redux store
│       │   └── 🔄 interactionSlice.js    # Redux slice
│       ├── 📂 services/
│       │   └── 🌐 api.js                 # Axios API calls
│       └── 📄 App.js
│
├── 📄 .gitignore
└── 📖 README.md
```

---

## 🚀 How to Run the Project

### ✅ Prerequisites
Make sure you have these installed:
- 🟢 Node.js v18+
- 🐍 Python 3.11+
- 🐬 MySQL 8.0+
- 🔑 Groq API Key from https://console.groq.com

---

### 🗄️ Step 1: Setup Database

```sql
CREATE DATABASE hcp_crm;
USE hcp_crm;

CREATE TABLE hcp_interactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hcp_name VARCHAR(255),
    interaction_type VARCHAR(100),
    interaction_date DATE,
    interaction_time TIME,
    attendees TEXT,
    topics_discussed TEXT,
    materials_shared TEXT,
    samples_distributed TEXT,
    sentiment VARCHAR(20),
    outcomes TEXT,
    follow_up_actions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### ⚙️ Step 2: Setup Backend

```bash
# Go to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy pymysql python-dotenv langgraph langchain-groq pydantic langchain

# Create .env file
GROQ_API_KEY=your_groq_api_key_here
DB_URL=mysql+pymysql://root:yourpassword@localhost/hcp_crm

# Start backend server
uvicorn main:app --reload --port 8000
```

✅ Backend running at: **http://localhost:8000**
📖 API Docs at: **http://localhost:8000/docs**

---

### 🎨 Step 3: Setup Frontend

```bash
# Go to frontend folder
cd frontend

# Install dependencies
npm install

# Start React app
npm start
```

✅ Frontend running at: **http://localhost:3000**

---

## 💬 Example AI Chat Messages

Try these messages in the AI Assistant chat:

```
1️⃣  "Today I met with Dr. Smith and discussed product X efficiency.
     The sentiment was positive, and I shared the brochures."

2️⃣  "I had a call with Dr. Johnson about the new diabetes medication.
     He was neutral and I shared sample kits."

3️⃣  "Show me all past interactions with Dr. Smith"

4️⃣  "Suggest a follow-up action for Dr. Smith after discussing
     product X efficiency"

5️⃣  "Analyze the sentiment of this: The doctor was very enthusiastic
     and asked for more product details"
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/interactions` | Create new interaction |
| `GET` | `/interactions` | Get all interactions |
| `PUT` | `/interactions/{id}` | Update interaction |
| `POST` | `/chat` | AI chat endpoint |

---

## 🎯 How It Works

```
User types message in chat
         ↓
React sends to FastAPI /chat endpoint
         ↓
FastAPI sends to Groq LLM (llama-3.3-70b)
         ↓
LLM extracts structured data (JSON)
         ↓
Data saved to MySQL database
         ↓
Form auto-fills on the left panel
         ↓
Success message shown in chat ✅
```

---

## 📜 License

This project was built as part of an assignment for an AI-First CRM system.

---

## 🙏 Acknowledgements

- 🤖 [Groq](https://console.groq.com) — For the fast LLM API
- 🦜 [LangGraph](https://langchain-ai.github.io/langgraph/) — For the AI agent framework
- ⚡ [FastAPI](https://fastapi.tiangolo.com) — For the backend framework
- ⚛️ [React](https://reactjs.org) — For the frontend framework

---

<div align="center">

### ⭐ If you like this project, please give it a star! ⭐

**Built with ❤️ by K. Sai Eswar from Anthapuram, Andhra Pradesh 🇮🇳**

</div>
