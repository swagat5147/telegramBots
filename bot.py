from flask import Flask, request, jsonify, render_template
from gevent.pywsgi import WSGIServer
import requests
import re
import os

app = Flask(__name__)

TOKEN = os.environ.get('TOKEN')
BASE_URL = "https://api.telegram.org/bot{}/".format(TOKEN)

@app.route("/", methods = ["GET"])
def index():
	return render_template("index.html")

@app.route("/update", methods = ["POST"])
def update():
	print("RunningBot.......")
	print(request.get_json())
	return "200, OK"

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	http_server = WSGIServer(('', port),app)
	http_server.serve_forever() 
