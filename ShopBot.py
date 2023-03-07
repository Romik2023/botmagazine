import telebot
from telebot import types
from telebot.types import KeyboardButton

bot = telebot.TeleBot('5693916134:AAG9QpBzuuY3WoBNMpLEVr0D3bkBzqBniVU')

@bot.message_handler(commands=['start'])
def start(message):
    kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton("Компютери")
    btn2 = types.KeyboardButton("Телефони")
    btn3 = types.KeyboardButton("Телевізори")
    kb.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, text='Hello', reply_markup=kb)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "Компютери":
            kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
            pc1 = types.KeyboardButton("Asus")
            pc2 = types.KeyboardButton("Lenovo")
            back = types.KeyboardButton("Назад")
            kb.add(pc1, pc2, back)

            bot.send_message(message.chat.id, "Компютери", reply_markup=kb)

        elif message.text == 'Телефони':
           kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
           phone1 = KeyboardButton(text="Xiaomi")
           phone2 = KeyboardButton(text="Asus")
           phone3 = KeyboardButton(text="Iphone")
           phone4 = KeyboardButton(text='Samsung')
           back = KeyboardButton(text='Назад')
           kb.add(phone1, phone2, phone3, phone4, back)

           bot.send_message(message.chat.id, 'Телефони', reply_markup=kb)

        elif message.text == 'Телевізори':
            kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
            tv1 = KeyboardButton(text="LG")
            tv2 = KeyboardButton(text="Sony")
            tv3 = KeyboardButton(text="Philips")
            tv4 = KeyboardButton(text='Panasonic')
            back = KeyboardButton(text='Назад')
            kb.add(tv1, tv2, tv3, tv4, back)

            bot.send_message(message.chat.id, 'Телевізори', reply_markup=kb)

        elif message.text == "Назад":
            kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton("Компютери")
            btn2 = types.KeyboardButton("Телефони")
            btn3 = types.KeyboardButton("Телевізори")
            kb.add(btn1, btn2, btn3)

            bot.send_message(message.chat.id, "Назад", reply_markup=kb)





bot.infinity_polling()