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
	print("Sending photo...")

def stfu(bot, update):
	chat_id = update.message.chat_id
	bot.send_messsage(chat_id = chat_id, text = "Shut The Fuck Up Subhrajit")

def main():
	TOKEN = os.getenv("TOKEN")
	print("Running bot")
	updater = Updater(TOKEN)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('bop', bop))
	dp.add_handler(CommandHandler('stfu', stfu))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
