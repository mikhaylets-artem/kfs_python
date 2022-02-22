import telebot
from telebot import types
bot = telebot.TeleBot("5180095537:AAGEX6yTbAH9acJovbaFqG3hqSIBZ_7Dz9Y", parse_mode=None)
name = ""
surname = ""
age = 0
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 bot.reply_to(message, "Я твой персональный бот, давай знакомиться!")
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == "privet":
        bot.reply_to(message, "Я рад тебя видеть, Добро пожаловать!")
    elif message.text == "/reg":
        bot.send_message(message.from_user.id, "Привет, давай с тобой познакомимся! Как тебя зовут?")
        bot.register_next_step_handler(message, registr_name)
    else:
        bot.reply_to(message, 'i dont understand u)')
def registr_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Введите вашу фамилию')
    bot.register_next_step_handler(message, registr_surname)
def registr_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Введите ваш возраст')
    bot.register_next_step_handler(message, registr_age)
def registr_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введите числами!!!!!!')
    shadowfiend = f"Я понял, что тебя зовут {name.title()} {surname.title()} и твой возраст - {age}, Верно ли?"
    zxc = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='yes', callback_data='yes')
    button_no = types.InlineKeyboardButton(text='no', callback_data='no')
    zxc.add(button_yes)
    zxc.add(button_no)
    bot.send_message(message.from_user.id, text=shadowfiend, reply_markup=zxc)
@bot.callback_query_handler(func=lambda qwe: True)
def query_callback(qwe):
    if qwe.data == 'yes':
        bot.send_message(qwe.message.chat.id  ,' вы записаны ' )
    elif qwe.data == "no":
        bot.send_message(qwe.message.chat.id, ' вы He записаны  ,  как вас зовут ? ')
        bot.register_next_step_handler(qwe.message, registr_name)
bot.infinity_polling()
