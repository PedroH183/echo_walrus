from google import genai
from app.ia_models.prompt_text import assistente_vendas


import os
from .base import AIModel


class GeminiModel(AIModel):
    """
        Implementation of the Gemini AI model.

        Please read the docs :: https://ai.google.dev/gemini-api/docs/quickstart?lang=python
    """

    def __init__(self):
        """Initialize the Gemini model with an API key. """

        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("No Gemini API key provided. Set the GEMINI_API_KEY environment variable.")

        self.gemini_client = genai.Client(api_key=self.api_key)

    async def get_response(self, message: str) -> str:
        """Get reponse from Gemini model"""
        try:
            response = self.gemini_client.models.generate_content(
                model="gemini-2.0-flash", contents=[
                    assistente_vendas,
                    message
                ]
            )
            return response.text
        except Exception as e:
            return f"Error getting response from Gemini: {str(e)}", "Sorry i can't understand your message"