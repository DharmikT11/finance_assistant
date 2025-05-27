# AI Tool Usage Log

This file documents how AI tools and models were used.

---

## 1. Retrieval-Augmented Generation (RAG)

- **Model**: sentence-transformers/all-MiniLM-L6-v2
- **Used For**: Embedding earnings headlines, storing in FAISS vector store

## 2. Summarization LLM

- **Model**: Hugging Face – `google/flan-t5-large`
- **Used For**: Generating spoken-style summaries for financial data

## 3. Text-to-Speech

- **Tool**: `gTTS` (Google Text-to-Speech)
- **Used For**: Speaking the market brief aloud in the Streamlit app

## 4. Speech-to-Text

- **Tool**: `openai-whisper`
- **Used For**: Transcribing user's voice questions (used locally)

## 5. Orchestration

- **Tool**: `FastAPI`
- **Used For**: Creating modular endpoints to integrate all agents
