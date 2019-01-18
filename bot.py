from flask import Flask, request, jsonify, render_template
from gevent.pywsgi import WSGIServer
import requests
import re
import os

app = Flask(__name__, static_folder="/static")

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
	return render_template("index.html")

@app.route("/recieve", methods=["GET","POST"])
def receive():
	print("Running bot")
	if request.method = 'GET':
		return jsonify(request.get_json())
	else:
		print(request.get_json())
		return jsonify(request.get_json())

if __name__ == '__main__':
	TOKEN = os.environ.get('TOKEN')
	r = requests.post("https://api.telegram.org/bot{}/setWebhook?url=https://kutta-bot.herokuapp.com/receive".format(TOKEN))
	print(r.content)
	port = int(os.environ.get('PORT', 5000))
	http_server = WSGIServer(('',port),app)
	http_server.serve_forever()
