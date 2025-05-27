# orchestrator/main.py

from fastapi import FastAPI
from agents.api_agent import APIAgent
from agents.scraping_agent import ScrapingAgent
from agents.retriever_agent import RetrieverAgent
from agents.language_agent import LanguageAgent

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Finance Assistant Orchestrator running!"}

@app.get("/market_brief")
def market_brief():
    # Step 1: Get portfolio exposure
    api_agent = APIAgent()
    exposure = api_agent.get_portfolio_exposure()

    # Step 2: Get news
    scraper = ScrapingAgent()
    news = scraper.get_earnings_news()
    news_texts = [n['title'] for n in news]

    if not news_texts:
        news_texts = ["No earnings news available for Indian tech stocks."]

    # Step 3: Filter with retriever
    retriever = RetrieverAgent()
    retriever.add_documents(news_texts)
    relevant_news = retriever.retrieve("latest India tech stock earnings", top_k=3)

    # Step 4: Summarize
    lang_agent = LanguageAgent()
    summary = lang_agent.generate_summary(exposure["India_Tech"], relevant_news)

    return {"summary": summary}
