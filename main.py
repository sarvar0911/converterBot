import telebot

bot = telebot.TeleBot("UR OWN BOT_TOKEN")

USD = 12495.04
EUR = 13531.07


# /start - choose currency - enter in sums
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('€')
        markup.row('$')
        msg = bot.send_message(message.chat.id, 'Choose a currency (USD, EUR)', reply_markup=markup)
        bot.register_next_step_handler(msg, currency)


def currency(message):
    if message.text == '€':
        msg = bot.send_message(message.chat.id, 'Enter the amount in sums')
        bot.register_next_step_handler(msg, eur)
    elif message.text == '$':
        msg = bot.send_message(message.chat.id, 'Enter the amount in sums')
        bot.register_next_step_handler(msg, usd)
    else:
        msg = bot.send_message(message.chat.id, 'Enter a valid currency (USD, EUR)')
        bot.register_next_step_handler(msg, currency)


def eur(message):
    try:
        bot.send_message(message.chat.id, float(message.text) / EUR)
    except ValueError:
        bot.send_message(message.chat.id, 'Please enter a number!')


def usd(message):
    try:
        bot.send_message(message.chat.id, float(message.text) / USD)
    except ValueError:
        bot.send_message(message.chat.id, 'Please enter a number!')


bot.polling()
