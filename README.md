# DeltoBot - Telegram Bot

## Descripción

**DeltoBot** es un bot de Telegram diseñado para ofrecer varias funcionalidades útiles y entretenidas. Estas incluyen recomendaciones personalizadas de películas, libros y música, análisis de sentimiento de texto, información meteorológica y un contador personalizable. El bot aprovecha las capacidades de OpenAI para generar respuestas inteligentes y relevantes según las preferencias del usuario.

## Funcionalidades

- **Recomendaciones Personalizadas**: El bot puede recomendar películas, libros o música según los gustos del usuario. Los usuarios pueden especificar géneros, estilos, actores, o emociones para obtener recomendaciones más precisas.
- **Análisis de Sentimiento**: Analiza el sentimiento de un texto proporcionado por el usuario (positivo, negativo o neutral) utilizando el motor GPT-3.5-turbo de OpenAI.
- **Información Meteorológica**: Proporciona la previsión del tiempo para cualquier ciudad que el usuario elija.
- **Contador Personal**: Permite a los usuarios llevar un contador personal que se incrementa cada vez que se solicita.

## Instalación

### Prerrequisitos

- Python 3.7 o superior
- [Telegram Bot API Token](https://core.telegram.org/bots#6-botfather)
- OpenAI API Key
- Open Weather Map API Key

### Configuración

1. **Clonar el repositorio:**

git clone  https://github.com/FranciscoNasso/PruebaTecnica-Bot.git
cd PruebaTecnica-Bot

2. **Crear un entorno virtual e instalar las dependencias:**

python3 -m venv .venv
Source .venv\Scripts\activate
pip install -r requirements.txt

3. **Configurar el archivo .env:**

Crea un archivo .env en la raíz del proyecto con el siguiente contenido:

TOKEN="your-telegram-bot-token"

weather_api_key = "your-weather-api-key"

DB_HOST="your-datbase-host"
DB_NAME="your-database-name"
DB_USER="your-database-use"
DB_PASSWORD="your-databe-password"

OPENAI_API_KEY="your-openai-api-key"

## Uso

1. **Ejecutar el bot:**

python Bot/main.py

2.**Comandos Disponibles:**

- /start: Inicia la interacción con el bot y muestra el menú principal.
- Opciones del Menú:
    - Quiero saber el clima! 🌦️: Solicita el nombre de una ciudad para proporcionar la previsión meteorológica.
    - Quiero Contar! 🔢: Incrementa y muestra el contador personal del usuario.
    - Quiero analizar sentimiento! 🧠: Analiza el sentimiento de un texto proporcionado por el usuario.
    - Quiero recomendaciones! 📝: Proporciona recomendaciones personalizadas de películas, libros o música según las preferencias del usuario.

## Estructura del Proyecto

- Bot/: Contiene el código fuente principal del bot.
    - main.py: El archivo principal donde se manejan todas las interacciones con el bot.
    - counter.py: Implementa la lógica del contador personal.
    - weather.py: Implementa la lógica para obtener la información meteorológica.
    - sentiment.py: Implementa la lógica para el análisis de sentimiento.
    - recommendation.py: Implementa la lógica para las recomendaciones personalizadas.

- data/: Contiene la configuración de la base de datos y los modelos.
    - db.py: Configuración de la conexión a la base de datos utilizando SQLAlchemy.
    - counterModel.py: Modelo del contador almacenado en la base de datos.
    - initDB.py: Script para inicializar la base de datos.

- requirements.txt: Lista de dependencias del proyecto.
- README.md: Este archivo, con la documentación del proyecto.

## Funcionalidad Adicional
### Recomendación Personalizada

Se añadió una funcionalidad de recomendación personalizada, donde el bot pregunta al usuario por sus preferencias en cuanto a películas, libros o música, y luego utiliza OpenAI para generar una recomendación basada en esos criterios.

Motivación: Esta funcionalidad mejora la experiencia del usuario al proporcionar recomendaciones que se alinean con sus gustos personales, haciendo que la interacción con el bot sea más atractiva y personalizada.

## Notas Técnicas

- Persistencia de Datos: El bot utiliza una base de datos MySQL para almacenar y manejar contadores personalizados por usuario.
- Manejo de Excepciones: El bot está diseñado para manejar errores comunes como la falta de conexión a la API o entradas inválidas, asegurando una experiencia de usuario fluida.
