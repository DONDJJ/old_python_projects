import telebot

keyboard1=telebot.types.ReplyKeyboardMarkup()
item1=telebot.types.KeyboardButton("Привет")
item2=telebot.types.KeyboardButton("Пока")
item3=telebot.types.KeyboardButton("Случайное число")
item4=telebot.types.KeyboardButton("Погода")
item5=telebot.types.KeyboardButton("Установить город")
item6=telebot.types.KeyboardButton("Курс $")
item7=telebot.types.KeyboardButton("Курс €")
item8=telebot.types.KeyboardButton("Узнать новости")
keyboard1.add(item1,item2,item3,item4, item5, item6, item7, item8)