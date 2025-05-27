# agents/language_agent.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class LanguageAgent:
    def __init__(self):
        self.model_name = "google/flan-t5-large"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

    def generate_summary(self, exposure_data, earnings_texts):
        exposure = f"India tech exposure is currently {exposure_data['current_allocation']}, up from {exposure_data['previous_allocation']} yesterday."
        earnings = "\n".join([f"- {line}" for line in earnings_texts])

        prompt = f"""Summarize this financial update into a professional spoken market brief:

{exposure}

Earnings reports:
{earnings}
"""

        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        output = self.model.generate(**inputs, max_new_tokens=150)

        return self.tokenizer.decode(output[0], skip_special_tokens=True)

# Test
if __name__ == "__main__":
    from api_agent import APIAgent

    api = APIAgent()
    exposure = api.get_portfolio_exposure()
    earnings_texts = [
        "TCS Q4 earnings beat expectations with 9% profit growth.",
        "Infosys misses revenue targets in Q1 due to global slowdown.",
        "Wipro posts strong Q3 results backed by cloud deals."
    ]

    lang_agent = LanguageAgent()
    brief = lang_agent.generate_summary(exposure["India_Tech"], earnings_texts)
    print("🗣️ Market Brief:\n", brief)


class LanguageAgent:
    def __init__(self, model_name="google/flan-t5-large"):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

    def generate_summary(self, exposure_data, earnings_texts, max_length=512, max_new_tokens=150):
        exposure = f"India tech exposure is currently {exposure_data['current_allocation']}, up from {exposure_data['previous_allocation']} yesterday."
        earnings = "\n".join([f"- {line}" for line in earnings_texts])

        prompt = f"""Summarize this financial update into a professional spoken market brief:

{exposure}

Earnings reports:
{earnings}
"""

        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
        output = self.model.generate(**inputs, max_new_tokens=max_new_tokens)

        return self.tokenizer.decode(output[0], skip_special_tokens=True)

    def generate_summary_from_api(self, api_agent, portfolio_name="India_Tech"):
        exposure = api_agent.get_portfolio_exposure()
        earnings_texts = api_agent.get_earnings_reports()
        return self.generate_summary(exposure[portfolio_name], earnings_texts)

# Test
if __name__ == "__main__":
    from api_agent import APIAgent

    api = APIAgent()
    lang_agent = LanguageAgent()
    brief = lang_agent.generate_summary_from_api(api)
    print("🗣️ Market Brief:\n", brief)