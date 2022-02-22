import telebot
from telebot import types
bot = telebot.TeleBot("5241764948:AAF8VcXiQcpSgxfoi72wYO-1IqOjJvxKkNU", parse_mode=None)

name = ""
surname = ""
age = 0

@bot.message_handler(commands=["start", "help"])
def start_hi(message):
    bot.send_message(message.from_user.id, 'Lets start!')


@bot.message_handler(func=lambda m:True)
def zxc(message):
    if message.text == 'Как дела?':
        bot.send_message(message.from_user.id, "Ok!")
    elif message.text == 'Что делаешь?':
        bot.send_message(message.from_user.id, "Уч")
    elif message.text == "reg":
        bot.send_message(message.from_user.id, "Как тебя зовут?")
    else:
        bot.reply_to(message.from_user.id, "????")
    bot.register_next_step_handler(message, q)
@bot.callback_query_handler(func=lambda q:True)
def q(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Фамилия?')
    bot.register_next_step_handler(message, surname_reg)

def surname_reg(message):
    global surname_reg
    surname_reg = message.text
    bot.send_message(message.from_user.id, 'age?')
    bot.register_next_step_handler(message, age_reg)

def age_reg(message):
    global age_reg
    while age_reg == 0:
        try:
            age_reg = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введите числами!!!!!!')
    shadowfiend = f"Я понял, что тебя зовут {name.title()} {surname_reg.title()} и твой возраст - {age_reg}, Верно ли?"
    zxc = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='yes', callback_data='yes')
    button_no = types.InlineKeyboardButton(text='no', callback_data='no')
    zxc.add(button_yes, button_no)
    # zxc.add(button_no)
    bot.send_message(message.from_user.id, text=shadowfiend, reply_markup=zxc)


bot.infinity_polling()
