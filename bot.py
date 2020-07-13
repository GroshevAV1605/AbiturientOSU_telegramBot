import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TG_TOKEN")
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def any_msg(message):
    mainMarkup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    itemBtn1 = types.KeyboardButton('Категория 1')
    itemBtn2 = types.KeyboardButton('Категория 2')
    itemBtn3 = types.KeyboardButton('Категория 3')
    itemBtn4 = types.KeyboardButton('Категория 4')
    itemBtn5 = types.KeyboardButton('Категория 5')
    mainMarkup.add(itemBtn1, itemBtn2, itemBtn3, itemBtn4, itemBtn5)

    if message.text == 'Категория 1':
        cat1Markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        cat1Q1 = types.KeyboardButton('Кат 1, Вопр 1')
        cat1Q2 = types.KeyboardButton('Кат 1, Вопр 2')
        cat1Q3 = types.KeyboardButton('Кат 1, Вопр 3')
        cat1Q4 = types.KeyboardButton('Кат 1, Вопр 4')
        cat1Q5 = types.KeyboardButton('Кат 1, Вопр 5')
        cat1Markup.add(cat1Q1, cat1Q2, cat1Q3, cat1Q4, cat1Q5)
        cat1Markup.row(types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, 'Категория 1', reply_markup=cat1Markup)
    elif message.text == 'Кат 1, Вопр 1':
        bot.send_message(message.chat.id, 'Ответ на вопрос 1 категории 1')
    elif message.text == 'Кат 1, Вопр 2':
        bot.send_message(message.chat.id, 'Ответ на вопрос 2 категории 1')
    elif message.text == 'Кат 1, Вопр 3':
        bot.send_message(message.chat.id, 'Ответ на вопрос 3 категории 1')
    elif message.text == 'Кат 1, Вопр 4':
        bot.send_message(message.chat.id, 'Ответ на вопрос 4 категории 1')
    elif message.text == 'Кат 1, Вопр 5':
        bot.send_message(message.chat.id, 'Ответ на вопрос 5 категории 1')
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=mainMarkup)
    else :
        bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=mainMarkup)

bot.polling(none_stop=True)