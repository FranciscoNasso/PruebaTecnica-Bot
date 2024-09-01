import openai
import os
from dotenv import load_dotenv


# API Key de OpenAI
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


# Función para obtener una recomendación
def get_recomendation(prompt: str, category: str) -> str:
    try:
        recomendation_prompt = f"Based on these preferences: {prompt}, recommend a {category}. Provide the title and a brief description explaining why this movie fits the preferences."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a recommendation assistant."},
                {"role": "user", "content": recomendation_prompt}
            ],
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.0,
        )
        recomendation = response.choices[0].message['content'].strip()
        return recomendation

    except openai.error.OpenAIError as e:
        if "You exceeded your current quota" in str(e):
            return (
                "Error: Se ha excedido la cuota de OpenAI. Por favor, inténtalo más tarde o contacta al administrador.")

    except Exception as e:
        return f"Error al obtener la recomendación: {e}"
