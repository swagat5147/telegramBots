from flask import Flask, request, jsonify
from gevent.pywsgi import WSGIServer
import requests
import re
import os

app = Flask(__name__)

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

@app.route("/", methods=["GET"])
def index():
	return "Hello user!"

@app.route("/recieve", methods=["POST"])
def receive():
	print("Running bot")
	print(request)

	return jsonify({"status":"200, OK"})

if __name__ == '__main__':
	TOKEN = os.environ.get('TOKEN')
	r = requests.post("https://api.telegram.org/bot{}/setWebhook?url=https://kutta-bot.herokuapp.com/receive".format(TOKEN))
	print(r.content)
	port = int(os.environ.get('PORT', 5000))
	http_server = WSGIServer(('',port),app)
	http_server.serve_forever()
