import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TG_TOKEN")
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def any_msg(message):
    defaultMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)

bot.polling(none_stop=True)