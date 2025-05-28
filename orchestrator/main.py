# orchestrator/main.py

from fastapi import FastAPI
from agents.api_agent import APIAgent
from agents.scraping_agent import ScrapingAgent
from agents.language_agent import LanguageAgent

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Finance Assistant Orchestrator running!"}

@app.get("/market_brief")
def market_brief():
    # Step 1: Get stock exposure
    api_agent = APIAgent()
    exposure = api_agent.get_portfolio_exposure()

    # Step 2: Scrape earnings headlines
    scraper = ScrapingAgent()
    news = scraper.get_earnings_news()
    news_texts = [n['title'] for n in news]

    if not news_texts:
        news_texts = ["No current earnings headlines found for Indian tech stocks."]

    # Step 3: Generate summary using LLM
    lang_agent = LanguageAgent()
    summary = lang_agent.generate_summary(exposure["India_Tech"], news_texts)

    return {"summary": summary}
