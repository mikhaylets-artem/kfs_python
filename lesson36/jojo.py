import telebot
from telebot import types
bot = telebot.TeleBot("5292142983:AAGpnHQ6JvYjE4Cm4GDMF45fRF0yBiTP7Eg", parse_mode=None)

name_s = 0
name = ""
surname = ""


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Привет')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)


@bot.message_handler(commands=['start_registration'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Yes', callback_data="yes"))
    markup.add(telebot.types.InlineKeyboardButton(text='No', callback_data="no"))
    bot.send_message(message.chat.id, text="Are you sure you want to start registration ?", reply_markup=markup)


@bot.callback_query_handler(func=lambda gwe: True)
def query_callback(qwe):
    if qwe.data == "yes":
        bot.send_message(qwe.message.chat.id, "Оk let's start ! Please click 'start_registration' again")
        bot.register_next_step_handler(qwe.message, registr_name_s)
    elif qwe.data == "no":
        bot.send_message(qwe.message.chat.id, "Okay maybe another time.")


def registr_name_s(message):
    global name_s
    name_s = message.text
    bot.send_message(message.from_user.id, 'Lets start with an introduction, okay?')
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('okay')
    bot.send_message(message.chat.id, 'okay?', reply_markup=keyboard)
    bot.register_next_step_handler(message, registr_name)


def registr_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Как тебя зовут?')
    bot.register_next_step_handler(message, registr_surname)


def registr_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Введите вашу фамилию')
    bot.register_next_step_handler(message, name_inform)


def name_inform(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, f"Great,{surname.title()} now we are familiar . write 'start survey' ")
    bot.register_next_step_handler(message, start_message_a)


def start_message_a(message):
    shadowfiend = "Who do you like more?"
    zxc = telebot.types.InlineKeyboardMarkup()
    button_cats = telebot.types.InlineKeyboardButton(text='cats', callback_data='cats')
    button_dogs = telebot.types.InlineKeyboardButton(text='dogs', callback_data='dogs')
    zxc.add(button_cats, button_dogs)
    bot.send_message(message.from_user.id, text=shadowfiend, reply_markup=zxc)
    bot.register_next_step_handler(message, query_cd)


@bot.callback_query_handler(func=lambda qwe: True)
def query_cd(qwe):
    if qwe.data == 'cats':
        bot.send_message(qwe.message.chat.id, "Ok!")
    elif qwe.data == 'dogs':
        bot.send_message(qwe.message.chat.id, "Ok!")


bot.polling()
