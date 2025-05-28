import streamlit as st
import requests
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import os
import feedparser
from nsetools import Nse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# -- Agents Recreated Inline --

# API Agent
def get_portfolio_exposure():
    return {
        "India_Tech": {
            "current_allocation": "25%",
            "previous_allocation": "21%"
        }
    }

# Scraping Agent
def get_earnings_news():
    companies = ["TCS", "INFOSYS", "WIPRO", "HCLTECH"]
    base_url = "https://news.google.com/rss/search?q={company}+earnings+india"
    all_news = []

    for company in companies:
        feed = feedparser.parse(base_url.format(company=company))
        for entry in feed.entries:
            all_news.append(f"{company}: {entry.title}")
    return all_news or ["No recent earnings news found."]

# Language Agent
def generate_summary(exposure, news_list):
    model_name = "google/flan-t5-large"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    prompt = f"""Summarize this market update:

India Tech exposure is now {exposure['current_allocation']}, up from {exposure['previous_allocation']}.

Earnings news:
{chr(10).join(news_list[:3])}
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(**inputs, max_new_tokens=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# -- Streamlit UI --

st.set_page_config(page_title="Finance Assistant", layout="centered")
st.title("📊 India Tech Market Brief")

if st.button("🎙️ Get Market Brief"):
    with st.spinner("Generating summary..."):
        try:
            exposure = get_portfolio_exposure()["India_Tech"]
            news = get_earnings_news()
            summary = generate_summary(exposure, news)
            st.success("✅ Summary Ready!")
            st.markdown(f"**📝 Summary:** {summary}")

            tts = gTTS(summary)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                audio = AudioSegment.from_file(fp.name, format="mp3")
                play(audio)
                os.remove(fp.name)

        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
