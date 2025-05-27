import streamlit as st
import requests
from gtts import gTTS
from playsound import playsound
import tempfile
import os

API_URL = "http://127.0.0.1:8000/market_brief"

st.set_page_config(page_title="Finance Assistant", layout="centered")
st.title("📊 Morning Market Brief – India Tech Stocks")

st.markdown("Click the button to fetch today's market exposure and earnings summary. The assistant will also read it aloud.")

if st.button("🎙️ Get Market Brief"):
    with st.spinner("Fetching data from agents..."):
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                summary = response.json().get("summary", "No data received.")
                st.success("✅ Summary generated!")
                st.markdown(f"**📝 Summary:** {summary}")

                # Text-to-speech using gTTS + playsound
                tts = gTTS(summary)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                    tts.save(tmp.name)

                playsound(tmp.name)
                os.remove(tmp.name)

            else:
                st.error(f"❌ Failed to get summary: {response.status_code}")
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
