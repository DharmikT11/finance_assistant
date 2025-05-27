# agents/voice_agent.py

import whisper
from gtts import gTTS
import os
from playsound import playsound
import tempfile

class VoiceAgent:
    def __init__(self):
        self.model = whisper.load_model("base")  # or "tiny" for faster
        print("✅ Whisper model loaded.")

    def transcribe_audio(self, file_path):
        result = self.model.transcribe(file_path)
        return result['text']

    def speak_text(self, text):
        tts = gTTS(text)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            playsound(fp.name)
            os.remove(fp.name)

# Test
if __name__ == "__main__":
    agent = VoiceAgent()
    
    print("🎙️ Listening to sample file...")
    transcript = agent.transcribe_audio("sample_voice.mp3")  # You can record this
    print("📝 Transcribed:", transcript)

    reply = "Today, India tech exposure is 25%. TCS beat earnings expectations."
    print("🔊 Speaking response...")
    agent.speak_text(reply)
