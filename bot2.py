import telebot
from telebot import types
from dotenv import load_dotenv
import os
from questions import questionsDict

load_dotenv()
token = os.getenv("TG_TOKEN")
bot = telebot.TeleBot(token)

CategoriesMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
QueCat1 = types.KeyboardButton('Обучение')
QueCat2 = types.KeyboardButton('Льготы')
QueCat3 = types.KeyboardButton('Подача документов')
QueCat4 = types.KeyboardButton('Выбор направления')
QueCat5 = types.KeyboardButton('Вступительные испытания')
QueCat6 = types.KeyboardButton('Другие вопросы')

CategoriesMarkup.add(QueCat1, QueCat2, QueCat3, QueCat4, QueCat5, QueCat6)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет, задай вопрос прямо в чате или воспользуйся поиском по категориям ниже', reply_markup=CategoriesMarkup)


@bot.message_handler(content_types=["text"])
def any_msg(message):

    defaultMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if message.text == 'Обучение':
        for item in questionsDict:
            if item['category'] == 'education':
                itemBtn = types.KeyboardButton(item['question'])
                defaultMarkup.add(itemBtn)
        defaultMarkup.add(types.KeyboardButton('Главное меню'))
        bot.send_message(message.chat.id, 'Вопросы, связанные с обучением', reply_markup=defaultMarkup)
        return
    elif message.text == 'Льготы':
        for item in questionsDict:
            if item['category'] == 'privileges':
                itemBtn = types.KeyboardButton(item['question'])
                defaultMarkup.add(itemBtn)
        defaultMarkup.add(types.KeyboardButton('Главное меню'))
        bot.send_message(message.chat.id, 'Вопросы, связанные с льготами', reply_markup=defaultMarkup)
        return
    elif message.text == 'Подача документов':
        for item in questionsDict:
            if item['category'] == 'docs':
                itemBtn = types.KeyboardButton(item['question'])
                defaultMarkup.add(itemBtn)
        defaultMarkup.add(types.KeyboardButton('Главное меню'))
        bot.send_message(message.chat.id, 'Вопросы, связанные с подачей документов', reply_markup=defaultMarkup)
        return
    elif message.text == 'Выбор направления':
        for item in questionsDict:
            if item['category'] == 'choice':
                itemBtn = types.KeyboardButton(item['question'])
                defaultMarkup.add(itemBtn)
        defaultMarkup.add(types.KeyboardButton('Главное меню'))
        bot.send_message(message.chat.id, 'Вопросы, связанные с выбором направления', reply_markup=defaultMarkup)
        return
    elif message.text == 'Вступительные испытания':
        for item in questionsDict:
            if item['category'] == 'test':
                itemBtn = types.KeyboardButton(item['question'])
                defaultMarkup.add(itemBtn)
        defaultMarkup.add(types.KeyboardButton('Главное меню'))
        bot.send_message(message.chat.id, 'Вопросы, связанные с вступительными испытаниями', reply_markup=defaultMarkup)
        return
    elif message.text == 'Другие вопросы':
        for item in questionsDict:
            if item['category'] == 'other':
                itemBtn = types.KeyboardButton(item['question'])
                defaultMarkup.add(itemBtn)
        defaultMarkup.add(types.KeyboardButton('Главное меню'))
        bot.send_message(message.chat.id, 'Остальные вопросы', reply_markup=defaultMarkup)
        return
    elif message.text == 'Главное меню':
        bot.reply_to(message, 'Категории:', reply_markup=CategoriesMarkup)
        return





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
        bot.send_message(message.chat.id, 'По запросу ничего не найдено.Воспользуйтесь поиском по категориям', reply_markup=CategoriesMarkup)
    else:
        defaultMarkup.add('Главное меню')
        bot.send_message(message.chat.id, 'Выбери вопрос', reply_markup=defaultMarkup)            




bot.polling(none_stop=True)