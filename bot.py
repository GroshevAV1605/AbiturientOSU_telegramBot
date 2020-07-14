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
    itemBtn1 = types.KeyboardButton('Выбор специальности')
    itemBtn2 = types.KeyboardButton('Правила приема')
    itemBtn3 = types.KeyboardButton('Подача документов')
    itemBtn4 = types.KeyboardButton('Вступительные испытания')
    itemBtn5 = types.KeyboardButton('Участие в кокурсе')
    mainMarkup.add(itemBtn1, itemBtn2, itemBtn3, itemBtn4, itemBtn5)

    if message.text == 'Выбор специальности':
        cat1Markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        cat1Q1 = types.KeyboardButton('Кат 1, Вопр 1')
        cat1Q2 = types.KeyboardButton('Кат 1, Вопр 2')
        cat1Q3 = types.KeyboardButton('Кат 1, Вопр 3')
        cat1Q4 = types.KeyboardButton('Кат 1, Вопр 4')
        cat1Q5 = types.KeyboardButton('Кат 1, Вопр 5')
        cat1Markup.add(cat1Q1, cat1Q2, cat1Q3, cat1Q4, cat1Q5)
        cat1Markup.row(types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, 'Выбор специальности', reply_markup=cat1Markup)

    elif message.text == 'Правила приема':
        cat2Markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        cat2Q1 = types.KeyboardButton('Кат 2, Вопр 1')
        cat2Q2 = types.KeyboardButton('Кат 2, Вопр 2')
        cat2Q3 = types.KeyboardButton('Кат 2, Вопр 3')
        cat2Markup.add(cat2Q1, cat2Q2, cat2Q3)
        cat2Markup.row(types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, 'Правила приема', reply_markup=cat2Markup)

    elif message.text == 'Подача документов':
        cat3Markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        cat3Q1 = types.KeyboardButton('Перечень документов')
        cat3Q2 = types.KeyboardButton('Как добраться до ОГУ?')
        cat3Q3 = types.KeyboardButton('Бланки заявлений')
        cat3Q4 = types.KeyboardButton('Сроки приема')
        cat3Markup.add(cat3Q1, cat3Q2, cat3Q3, cat3Q4)
        cat3Markup.row(types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, 'Подача документов\nВ данном разделе можно ознакомиться со сроками приема документов, режимом работы приемной комиссии, перечнем необходимых документов.\nТакже при личной подаче документов Вы сразу сможете подать заявление на предоставление общежития.\n- Личный кабинет обучающегося: https://osu.ru/iss/abiturient/', 
            reply_markup=cat3Markup)
        

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

    elif message.text == 'Кат 2, Вопр 1':
        bot.send_message(message.chat.id, 'Ответ на вопрос 1 категории 2')
    elif message.text == 'Кат 2, Вопр 2':
        bot.send_message(message.chat.id, 'Ответ на вопрос 2 категории 2')
    elif message.text == 'Кат 2, Вопр 3':
        bot.send_message(message.chat.id, 'Ответ на вопрос 3 категории 2')

    elif message.text == 'Кат 3, Вопр 1':
        bot.send_message(message.chat.id, 'Ответ на вопрос 1 категории 3')
    elif message.text == 'Кат 3, Вопр 2':
        bot.send_message(message.chat.id, 'Ответ на вопрос 2 категории 3')
    elif message.text == 'Кат 3, Вопр 3':
        bot.send_message(message.chat.id, 'Ответ на вопрос 3 категории 3')
    elif message.text == 'Кат 3, Вопр 4':
        bot.send_message(message.chat.id, 'Ответ на вопрос 4 категории 3')

    elif message.text == 'Перечень документов':
        bot.send_message(message.chat.id, 'Ответ на вопрос 1 категории 3')
    elif message.text == 'Как добраться до ОГУ?':
        bot.send_message(message.chat.id, 'Ответ на вопрос 2 категории 3')
    elif message.text == 'Бланки заявлений':
        bot.send_message(message.chat.id, 'Ответ на вопрос 3 категории 3')
    elif message.text == 'Сроки приема':
        bot.send_message(message.chat.id, 'Ответ на вопрос 4 категории 3')

    elif message.text == 'Назад':
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=mainMarkup)
    else :
        bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=mainMarkup)

bot.polling(none_stop=True)