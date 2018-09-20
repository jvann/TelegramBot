import telebot

bot_token="619906643:AAFm35_yCfkNisZ9b6ACvA1ohuvUAsHX_rU"

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_greetings(message):
	bot.reply_to(message, 'Hello, World!')

bot.polling()