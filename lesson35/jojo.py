import telebot
bot = telebot.TeleBot("5168526686:AAFz6iNgTXZZ_o2rhybilYnh3Aq90o2b_7c", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Я твой персональный бот, давай знакомиться! If you would like to get started please email")

@bot.message_handler(commands=[ "lets start the survey"])
def send_welcome(message):
    bot.reply_to(message, "Enter your first and last name.")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
# bot.reply_to(message, "Privet, bebrik")
    if message.text == "privet":
        bot.reply_to(message, "Я рад тебя видеть, Добро пожаловать!")
    else:
        bot.reply_to(message, 'i dont understand u)')




bot.infinity_polling()
