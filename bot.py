from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import os

def get_url():
	contents = requests.get('https://random.dog/woof.json').json()
	image_url = contents['url']
	return image_url

def get_image_url():
	allowed_extensions = ['jpg','jpeg','png']
	file_extension = ''
	while file_extension not in allowed_extensions:
		url = get_url()
		file_extension = re.search("([^.]*)$",url).group(1).lower()
	return url

def bop(bot, update):
	url = get_image_url()
	chat_id = update.message.chat_id
	bot.send_photo(chat_id=chat_id, photo = url)

def main():
	TOKEN = os.get.environ("TOKEN")
	updater = Updater(TOKEN)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('bop', bop))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
