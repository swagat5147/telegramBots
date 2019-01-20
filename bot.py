from flask import Flask, request, jsonify, render_template
from gevent.pywsgi import WSGIServer
import requests
import re
import os

app = Flask(__name__)

TOKEN = os.environ.get('TOKEN')
BASE_URL = "https://api.telegram.org/bot{}/".format(TOKEN)
group_chat_id = os.get.environ.get('group_chat_id')

@app.route("/", methods = ["GET"])
def index():
	return render_template("index.html")

@app.route("/update", methods = ["POST"])
def update():
	print("RunningBot.......")
	print(request.get_json())
	data = request.get_json()

	if data['message']['chat']['id'] == group_chat_id:

		if 'left_chat_member' in data['message']:
			print(data['message']['left_chat_member']['first_name'])
			name = data['message']['left_chat_member']['first_name']
			chat_id = data['message']['chat_id']['id']
			r = requests.post(BASE_URL+ "sendMessage", data={'chat_id': chat_id, 'text': name + " Left Codex" })


		if 'new_chat_member' in data['message']:
			print(data['message']['new_chat_member']['first_name'])
			name = data['message']['new_chat_member']['first_name']
			chat_id = data['message']['chat']['id']
			r = requests.post(BASE_URL+ "sendMessage", data={'chat_id': chat_id, 'text': "Welcome to Codex " + name})
		
	return "200, OK"

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	http_server = WSGIServer(('', port),app)
	http_server.serve_forever() 
