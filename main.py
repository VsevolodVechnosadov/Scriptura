import telebot
from creatoror import create_dir
from parserer_ii import download_images
from converterer import convert_pdf

bot = telebot.TeleBot(' ')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Дух возвратит вам рукопись, если вы предоставите ему ссылку на книгу из библиотеки https://lib-fond.ru.")

@bot.message_handler(regexp='https://lib-fond.ru')
def url_check(message):
	final_file = open(convert_pdf(download_images(create_dir(message.text), message.text)))
	bot.send_document(message, final_file)

bot.infinity_polling()
