import os
import telebot
from translator import to_latin, to_cyrillic

token = '1771133351:AAH5-1OI4UBQaVeawkvGbEq__4c6MoI36gI'
bot = telebot.TeleBot(token, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	ans = f"Assalomu alaykum {message.from_user.first_name}\nTarjima qilish uchun matn kiriting: ✍️"
	bot.reply_to(message, ans)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	msg = message.text
	# javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
	if msg.isascii():
		javob = to_cyrillic(msg)
	else:
		javob = to_latin(msg)
	bot.reply_to(message, javob)

bot.polling()