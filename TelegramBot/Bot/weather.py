import requests

import os
from dotenv import load_dotenv


load_dotenv()
WEATHER_API_KEY = os.getenv('weather_api_key')


def get_weather_recommendation(weather_condition: str) -> str:
    recommendations = {
        "clear sky": "Es un día soleado. ¡No olvides usar protector solar!",
        "few clouds": "Hay pocas nubes, pero el sol aún está presente. ¡Protege tu piel!",
        "scattered clouds": "El cielo está parcialmente nublado. Es un buen día para actividades al aire libre.",
        "broken clouds": "Está bastante nublado. Puede que no veas mucho el sol hoy.",
        "overcast clouds": "El cielo está nublado. No olvides tu chaqueta por si refresca.",
        "shower rain": "Parece que hay chubascos. Un paraguas te será útil.",
        "moderate rain": "Lluvia moderada. No olvides tu paraguas y una chaqueta impermeable.",
        "light rain": "Lluvia ligera. No olvides tu paraguas.",
        "rain": "Está lloviendo. ¡No olvides tu paraguas y una chaqueta impermeable!",
        "thunderstorm": "Hay tormenta. Mejor quédate en un lugar seguro.",
        "snow": "Está nevando. ¡Abrígate bien y ten cuidado en la carretera!",
        "mist": "Hay neblina. Conduce con precaución y enciende las luces antiniebla."
    }
    # Devolver la recomendación si se encuentra, de lo contrario una recomendación general.
    return recommendations.get(weather_condition.lower(), "Disfruta tu día, sea cual sea el clima.")


translations = {
    "clear sky": "Cielo despejado",
    "few clouds": "Pocas nubes",
    "scattered clouds": "Nubes dispersas",
    "broken clouds": "Nubes rotas",
    "overcast clouds": "Nublado",
    "shower rain": "Lluvia",
    "moderate rain": "Lluvia moderada",
    "light rain": "Lluvia ligera",
    "rain": "Lluvia",
    "thunderstorm": "Tormenta",
    "snow": "Nieve",
    "mist": "Neblina"
}


def get_weather(city: str) -> str:
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "in"
    }
    full_url = f"{base_url}?q={params['q']}&appid={params['appid']}&units={params['units']}&lang={params['lang']}"
    try:
        response = requests.get(full_url)
        response.raise_for_status()
        data = response.json()

        description = data['weather'][0]['description']
        temp = data['main']['temp']
        city_name = data['name']

        recommendation = get_weather_recommendation(description)
        description = translations.get(description.lower(), description)

        weather_report = (
            f"El clima en {city_name} es {description} con una temperatura de {temp}°C.\n"
            f"{recommendation}"
        )
        return weather_report
    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 404:
            return "No se encontró la ciudad. Por favor, verifica el nombre."
    except requests.exceptions.RequestException as e:
        return f"Error al obtener al clima: {e}"
    except KeyError as e:
        return "No se pudo obtener la información del clima. Verifica el nombre de la ciudad."
    except Exception as e:
        return f"Error al obtener el clima: {e}"
    