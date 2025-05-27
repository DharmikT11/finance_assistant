# 🎙️ Finance Assistant – AI Agentic Market Briefing System 🇮🇳

This project is a multi-agent, voice-enabled financial assistant that delivers daily market briefs for Indian tech stocks.

---

## 🧠 Features

- ✅ Real-time stock & earnings data (via `nsetools` and Google News RSS)
- ✅ FAISS-based RAG for contextual retrieval of financial news
- ✅ LLM-based narrative generation (FLAN-T5)
- ✅ Voice output using `gTTS`
- ✅ Modular backend built with FastAPI
- ✅ Streamlit UI for interaction

---

## 🧱 Architecture

User → Voice Input (Whisper) or Button
→ FastAPI Orchestrator
→ API Agent (stock data)
→ Scraping Agent (earnings headlines)
→ Retriever Agent (FAISS)
→ Language Agent (LLM Summary)
→ Streamlit App UI + gTTS Voice Out

yaml
Copy
Edit

---

## 📁 Project Structure

agents/ → Individual agents (api, scraping, etc.)
orchestrator/ → FastAPI microservice for routing
streamlit_app/ → Streamlit frontend app
docs/ → AI tool usage documentation

yaml
Copy
Edit

---

## 🚀 Setup & Run

### 1. Install dependencies:
pip install -r requirements.txt
### 2. Start backend API:
uvicorn orchestrator.main:app --reload
### 3. Run the Streamlit frontend:
streamlit run streamlit_app/app.py

📄 Documentation
/docs/ai_tool_usage.md: Full record of AI models/tools used and why

🔗 Demo (optional)
Add your Streamlit or Hugging Face Space deployment link here if available.

🤖 Agent Tools Used
nsetools, feedparser

sentence-transformers, faiss-cpu

transformers (FLAN-T5)

gTTS, playsound, openai-whisper

FastAPI, Streamlit

🧑‍💼 Author
Dharmik Thakkar
Internship Task – AI Agent (Voice Finance Assistant)

## 🔼 Step 3: Upload to GitHub

### Go to:
- [https://github.com/new](https://github.com/new)

### Fill in:
- Repository name: `finance-assistant`
- Description: `AI Agentic Voice-Enabled Market Briefing System for Indian Tech Stocks`
- Set to **Public**
- Click **Create Repository**

---

### Run These Commands in Terminal

```bash
cd path/to/your/finance-assistant

git init
git add .
git commit -m "Initial commit - AI finance assistant"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/finance-assistant.git
git push -u origin main


