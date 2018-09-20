import telebot

bot_token="619906643:AAFm35_yCfkNisZ9b6ACvA1ohuvUAsHX_rU"

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_greetings(message):
	bot.reply_to(message, 'Hello, World!')

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, 'Help has arrived! Meep Meep')

@bot.message_handler(commands=['info'])
def send_info(message):
	bot.reply_to(message, 'I have the info that you need')

bot.polling()
