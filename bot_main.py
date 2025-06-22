import os
from dotenv import load_dotenv
from telebot.types import Message
import telebot
import requests

load_dotenv()
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

API_URL = 'http://127.0.0.1:8000/api/'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    data = {
        "user_id": message.from_user.id,
        "username": message.from_user.username
    }
    response = requests.post(API_URL + "register/", json=data)
    resp_json = response.json()
    if 'message' in resp_json:
        bot.send_message(message.chat.id, "Пользователь уже зарегистрирован")
    elif 'id' in resp_json or 'user_id' in resp_json:
        # В зависимости от того, какой ключ возвращает ваш сериализатор
        bot.send_message(message.chat.id, f"Вы успешно зарегистрированы! Ваш user_id: {resp_json.get('user_id', resp_json.get('id'))}")
    else:
        bot.send_message(message.chat.id, "Произошла ошибка при регистрации!")
        print(resp_json)
        print(response.status_code)
        print(response.text)

@bot.message_handler(commands=['myinfo'])
def user_info(message: Message):
    response = requests.get(f"{API_URL}user/{message.from_user.id}/")
    if response.status_code == 200:
        bot.reply_to(message, f"Информация о пользователе:\n{response.text}")
    elif response.status_code == 404:
        bot.reply_to(message, "Пользователь не зарегистрирован")
    else:
        bot.reply_to(message, "Произошла ошибка при получении информации о пользователе")

if __name__ == '__main__':
    print("Бот запущен и ожидает сообщений...")
    bot.infinity_polling()