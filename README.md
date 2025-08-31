Here is your complete **README.md** for the HR Resource Query Chatbot—**ready to copy-paste to your GitHub repo**.  
Just update the `YOUR_GITHUB_USERNAME` and add screenshots/demo links if desired.

***

# HR Resource Query Chatbot

## Overview

The **HR Resource Query Chatbot** is an AI-powered assistant that helps HR teams efficiently search for and recommend employees using plain language questions (like “Find Python developers with 3+ years experience” or “Who has worked on healthcare projects?”).  
The system combines *semantic search* (embeddings) with *LLM-powered responses* (Gemini API) to provide relevant and natural recommendations in chat format.

***

## Features

- **Natural language employee searches** (skills/experience/projects)
- **Vector similarity (semantic) search** using embeddings
- **LLM-powered answer generation** (Google Gemini 1.5 Flash API)
- **Clean, easy chat interface** (Streamlit)
- **Sample employee data** (JSON, extensible)
- **REST API** for backend (`/chat`, `/employees/search`)
- **Supports secret management** via `.env`
- **Simple install — ready for cloud/local demo**

***

## Architecture

```
┌────────────┐      POST /chat        ┌────────────┐        ┌───────────────────┐
│ Frontend   │ ───────────────────▶   │  FastAPI   │ ─────▶ │ Gemini LLM (API)  │
│ (Streamlit)│   natural query        │  Backend   │        └───────────────────┘
└────────────┘   (user input)         │  + RAG     │
         ▲    ◀─────────────┐         └────────────┘
         │       JSON API   │  /employees/search ▲
         │      recommended │     sample data    │
         │      employees   └─────────────read────
```
- **Frontend:** Streamlit UI for HR chat experience.
- **Backend:** FastAPI for employee retrieval + LLM answer generation.
- **RAG pipeline:** Embedding-based retrieval and Gemini-powered text generation.
- **Data:** Simple employees.json, easy to extend.

***

## Setup & Installation

1. **Clone the repo:**
   ```sh
   git clone https://github.com/YOUR_GITHUB_USERNAME/hr-resource-query-chatbot.git
   cd hr-resource-query-chatbot
   ```

2. **Install requirements:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your API key:**
   - Create a `.env` file:
     ```
     GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
     ```
   - Get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

4. **Run backend:**
   ```sh
   uvicorn main:app --reload
   ```

5. **Run frontend:**
   ```sh
   streamlit run frontend.py
   ```

6. **Open the app:**
   - Streamlit chat UI at: [http://localhost:8501](http://localhost:8501)
   - FastAPI docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

***

## How to Use

- Use the chat UI to ask HR queries like:
  - *Find Python devs with 3+ years experience*
  - *Who has worked on healthcare projects?*
  - *Suggest people for a React Native project*
  - *Find developers who know both AWS and Docker*
- See LLM-powered summarized answers, with candidate details and reasoning.
- Use `/employees/search` endpoint for quick API-driven search/filtering by skill/project.

***

## API Documentation

**POST `/chat`**
- **Request:**  
  `{"query": "your HR search..."}`
- **Response:**  
  `{"answer": "...", "matches": [...]}`

**GET `/employees/search`**
- **Example:**  
  `/employees/search?skill=python&project=E-commerce Platform`
- **Response:**  
  `{"employees": [ ... ]}`

**Swagger/OpenAPI docs:**  
Visit `/docs` in your browser (i.e. [http://localhost:8000/docs](http://localhost:8000/docs)) to try endpoints live.

***

## AI Development Process

- **AI Tools Used:** ChatGPT, Gemini Flash, GitHub Copilot.
- **AI Assistance:**  
  - Requirements breakdown, semantic search code, Gemini integration, prompt design.
  - About 60–70% AI-assisted code; rest manual/bugfix.
- **Optimizations:**  
  - Prompt chaining for HR summaries, auto-profile formatting.
- **Challenges:**  
  - Gemini API model name quirks, error handling.
  - Stable LLM summary formatting.

***

## Technical Decisions

- **LLM:** Google Gemini for free, robust LLM API and fast REST integration.
- **No local LLM:** Resource-light prototype for all machines.
- **Retrieval:** Used strong, fast MiniLM embeddings for semantic search.
- **Frontend:** Streamlit for fast, no-JS UI.
- **Secret management:** .env/.gitignore to protect API keys.

***

## Future Improvements

- In-app add/edit/delete for employee data
- Persistent real database (SQLite/Postgres, etc.)
- User authentication (password/roles)
- Feedback + usage analytics
- Cloud deployment: Streamlit Cloud, Vercel, Hugging Face Spaces, etc.
- More advanced RAG: multi-pass, hybrid rules + LLM
- User feedback collection and scoring

***

## Demo

_Add a link to your Streamlit Cloud or screenshots/GIF here, if available._

***

## Project Structure

```
hr-resource-query-chatbot/
├── main.py         # FastAPI backend + RAG pipeline
├── frontend.py     # Streamlit UI
├── employees.json  # Sample employee data
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

***

### License

Apache License
