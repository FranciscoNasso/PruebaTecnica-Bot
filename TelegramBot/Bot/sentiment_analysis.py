import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def analyze_sentiment(prompt: str) -> str:
    try:
        sentiment_prompt = f"Analyze the sentiment of this text: '{prompt}'. Is it Positive, Negative, or Neutral?"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=sentiment_prompt,
            max_tokens=15,
            n=1,
            stop=None,
            temperature=0.0,
        )
        sentiment = response.choices[0].text.strip()
        return sentiment


    except openai.error.OpenAIError as e:
        if "You exceeded your current quota" in str(e):
            return (
                "Error: Se ha excedido la cuota de OpenAI. Por favor, inténtalo más tarde o contacta al administrador.")
    except Exception as e:
        return f"Error al analizar el sentimiento: {e}"
