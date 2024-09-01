import telebot
from telebot import types
from dotenv import load_dotenv
import os

from weather import get_weather as get_weather_service
from counter import increment_counter as increment_counter_service
from sentiment_analysis import analyze_sentiment as analyze_sentiment_service

# Token
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    clima = types.KeyboardButton('Quiero saber el clima! 🌦️')
    contador = types.KeyboardButton('Quiero Contar! 🔢')
    openai = types.KeyboardButton('Quiero analizar sentimiento! 🧠')
    option = [[clima], [contador], [openai]]
    markup = types.ReplyKeyboardMarkup(option)

    bot.send_message(message.chat.id, 'Bienvenido', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def callback_query(message):
    user_id = message.from_user.id
    if message.text == 'Quiero saber el clima! 🌦️':
        bot.send_message(message.chat.id, 'Ingrese la ciudad para obtener el clima: ')
        bot.register_next_step_handler(message, get_weather)

    elif message.text == 'Quiero Contar! 🔢':
        new_count = increment_counter_service(user_id)
        bot.send_message(message.chat.id, f'Contador: {new_count}')

    elif message.text == 'Quiero analizar sentimiento! 🧠':
        bot.send_message(message.chat.id, 'Ingrese el texto para analizar el sentimiento: ')
        bot.register_next_step_handler(message, get_analyze_sentiment)

    else:
        bot.send_message(message.chat.id, 'Por favor, seleccione una opción válida.')


def get_weather(message):
    city = message.text.split()[0]
    weather = get_weather_service(city)
    bot.send_message(message.chat.id, weather)


def get_analyze_sentiment(message):
    sentiment = analyze_sentiment_service(message.text)
    bot.send_message(message.chat.id, sentiment)


if __name__ == '__main__':
    bot.polling(none_stop=True)
