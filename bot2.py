import telebot
from telebot import types
from dotenv import load_dotenv
import os
from questions import questionsDict

load_dotenv()
token = os.getenv("TG_TOKEN")
bot = telebot.TeleBot(token)

QuestionsMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
QueCat1 = types.KeyboardButton('Cat1')
QueCat2 = types.KeyboardButton('Cat2')
QueCat3 = types.KeyboardButton('Cat3')
QuestionsMarkup.row(QueCat1, QueCat2, QueCat3)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет, задай вопрос прямо в чате или воспользуйся поиском по категориям ниже', reply_markup=QuestionsMarkup)


@bot.message_handler(content_types=["text"])
def any_msg(message):
    defaultMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    i= 0
    for item in questionsDict:
        if item['question'] == message.text:
            bot.reply_to(message, item['answer'])
            return

        for keyword in item['keywords']:
            if keyword in message.text:
                itemBtn = types.KeyboardButton(item['question'])
                defaultMarkup.add(itemBtn)
                i+=1
                break
    if i == 0:
        bot.send_message(message.chat.id, 'По запросу ничего не найдено.Воспользуйтесь поиском по категориям', reply_markup=QuestionsMarkup)
    else:
        defaultMarkup.add('Главное меню')
        bot.send_message(message.chat.id, 'Выбери вопрос', reply_markup=defaultMarkup)            




bot.polling(none_stop=True)