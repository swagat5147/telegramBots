from flask import Flask, request, jsonify, render_template
from gevent.pywsgi import WSGIServer
from xkcd import url, text
import requests
import re
import os

app = Flask(__name__)

TOKEN = os.environ.get('TOKEN')
BASE_URL = "https://api.telegram.org/bot{}/".format(TOKEN)
group_chat_id = int(os.environ.get('group_chat_id'))

@app.route("/", methods = ["GET"])
def index():
	return render_template("index.html")

@app.route("/update", methods = ["POST"])
def update():
	print("RunningBot.......")
	print(request.get_json())
	data = request.get_json()
	group_data = int(data['message']['chat']['id'])

	if group_data == group_chat_id:

		print("Working>>>>")

		if 'left_chat_member' in data['message']:
			print(data['message']['left_chat_member']['first_name'])
			Left_member_name = data['message']['left_chat_member']['first_name']
			r = requests.post(BASE_URL+ "sendMessage", data={'chat_id': group_chat_id, 'text': Left_member_name + " Left Codex" })


		if 'new_chat_member' in data['message']:
			print(data['message']['new_chat_member']['first_name'])
			New_member_name = data['message']['new_chat_member']['first_name']
			r = requests.post(BASE_URL+ "sendMessage", data={'chat_id': group_chat_id, 'text': "Welcome to Codex " + New_member_name})

		if data['message']['text'] == 'xkcd':
			r = requests.post(BASE_URL+ "sendPhoto", data={'chat_id': group_chat_id, 'photo': url, 'caption': text })


		
	return "200, OK"

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	http_server = WSGIServer(('', port),app)
	http_server.serve_forever() 
