import telebot
from translate import to_cyrillic, to_latin

token = '5636098289:AAGdvsl9w6S3U2DTRKO2lj_FvBvluFtLg8s'
bot = telebot.TeleBot(token , parse_mode=None)



@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    javob = "Assalomu aleykum Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message,javob)
    
@bot.message_handler(func=lambda message:True)
def echo_all(message):
    xabar = str(message.text)
    # javob = lambda xabar: to_cyrillic(xabar)  if xabar.isascii() else to_latin(xabar)
    if xabar.isascii():
        javob = to_cyrillic(xabar)
    else:
        javob = to_latin(xabar)
    bot.reply_to(message, javob)
bot.polling()
