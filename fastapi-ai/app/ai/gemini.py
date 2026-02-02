import google.generativeai as genai
from .base import AIPlatform

class GeminiPlatform(AIPlatform):
    def __init__(self, api_key: str, model_name: str = None):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def chat(self, prompt: str) -> str:
        if self.system_promt:
            prompt= f"{self.system_promt}\n\n{prompt}"
        response = self.model.generate_content(prompt)
        return response.text
