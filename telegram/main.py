import telebot
import random

from KeyBoards import keyboard1
from consts import *
from weather import get_weather
from config import API_TOKEN
from course import currency_chech
from news import news_check

bot = telebot.TeleBot(API_TOKEN)
location='Kazan'

def set_location(message):
    global location
    location = message.text
    bot.send_message(message.chat.id, "Текущий город: {}".format(location))

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Приветствую!!!", reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def ehco_message(message):

    if message.chat.type=='private':
        if message.text=='Случайное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text=='Погода':
            bot.send_message (message.chat.id, "Погода в {} {}".format(location, get_weather(location)))
        elif message.text=='Установить город':
            msg = bot.reply_to(message, "Введите свой город")
            bot.register_next_step_handler(msg, set_location)
        elif message.text=='Курс $':
            bot.send_message(message.chat.id, currency_chech('USD'))

        elif message.text=='Курс €':
            bot.send_message(message.chat.id, currency_chech('EUR'))
        elif message.text=='Узнать новости':
            news_res=news_check()



            for i in range(0,3,2):
                message_news = ''
                for i,j in zip(news_res[i],news_res[i+1]):
                    message_news+=i
                    message_news+='\n'
                    message_news+=j
                    message_news+='\n\n'
                bot.send_message(message.chat.id, message_news)
    if message.text in hello_list:
        bot.send_sticker(message.chat.id, hi_optimus)

    elif message.text in bye_list:
        bot.send_sticker(message.chat.id, bye_optimus)





    # popug
    # else:
    #     bot.send_message(message.chat.id, message.text)

# '''Узнать ID стикера'''
# @bot.message_handler(content_types=['sticker'])
# def get_stick_id(message):
#
#         print (message)



bot.polling(none_stop=True)

