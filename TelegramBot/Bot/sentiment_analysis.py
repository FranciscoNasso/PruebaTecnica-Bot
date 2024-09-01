import openai
import os
from dotenv import load_dotenv

# API Key de OpenAI
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


# Función para analizar el sentimiento de un texto
def analyze_sentiment(prompt: str) -> str:
    try:
        # Construir el prompt para el análisis de sentimiento
        sentiment_prompt = (f"Analyze the sentiment of this text: '{prompt}'. Is it Positive, Negative, or Neutral? Please explain briefly")
        # Llamada a la API de OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a sentiment analysis assistant."},
                {"role": "user", "content": sentiment_prompt}
            ],
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.0,
        )
        # Obtener el texto de la respuesta
        sentiment = response.choices[0].message['content'].strip()
        return sentiment

    except openai.error.OpenAIError as e:
        if "You exceeded your current quota" in str(e):
            return (
                "Error: Se ha excedido la cuota de OpenAI. Por favor, inténtalo más tarde o contacta al administrador.")
    except Exception as e:
        return f"Error al analizar el sentimiento: {e}"


# Función para obtener datos interesantes sobre una ciudad
def get_city_interesting_facts(city: str) -> str:
    try:
        prompt = f"Get interesting facts about {city}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a fact assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.0,
        )
        facts = response.choices[0].message['content'].strip()
        return facts

    except openai.error.OpenAIError as e:
        if "You exceeded your current quota" in str(e):
            return (
                "Error: Se ha excedido la cuota de OpenAI. Por favor, inténtalo más tarde o contacta al administrador.")
    except Exception as e:
        return f"Error al obtener datos interesantes: {e}"
