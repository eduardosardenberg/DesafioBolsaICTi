import openai
import os
from agents.prompts import planner_prompt_ptbr
from dotenv import load_dotenv

load_dotenv()


class PlannerAgent:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=self.api_key)

    def analyze_news(self, asset_name, news_list):
        if not news_list:
            return "MANTER", ["Nenhuma notícia recente encontrada."]

        prompt = planner_prompt_ptbr(asset_name, news_list)

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.2,
        )
        answer = response.choices[0].message.content.strip()

        rec = "MANTER"
        answer_upper = answer.upper()
        if answer_upper.startswith("COMPRAR"):
            rec = "COMPRAR"
        elif answer_upper.startswith("VENDER"):
            rec = "VENDER"
        elif answer_upper.startswith("MANTER"):
            rec = "MANTER"
        return rec, [answer]
