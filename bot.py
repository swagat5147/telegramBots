from flask import Flask, request, jsonify, render_template
from gevent.pywsgi import WSGIServer
import requests
import re
import os

app = Flask(__name__, static_folder="/static")

TOKEN = os.environ.get('TOKEN')
BASE_URL = "https://api.telegram.org/bot{}/".format(TOKEN)

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

@app.route("/update", methods=["GET","POST"])
def update():
	print("Running bot")
	if request.method == 'GET':
		return jsonify(request.get_json())
	else:
		print(request.get_json())
		data = request.get_json()
		if data['message']['text'].startswith("/bop"):
			chat_id = data['message']['chat']['id']
			r = requests.post(BASE_URL+ "sendPhoto", data={'chat_id': chat_id, 'photo' : get_image_url(), 'caption' : "Bhow bhow!"})
			print(r.status_code)
		return jsonify(request.get_json())

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	http_server = WSGIServer(('',port),app)
	http_server.serve_forever()
