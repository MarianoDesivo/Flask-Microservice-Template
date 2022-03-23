from flask import Flask
from multiprocessing import Process
import socket
from flask import request
from flask import jsonify

app = Flask(__name__)



@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.route("/")
def home():
    return socket.gethostbyname(socket.gethostname())

@app.route('/startheavy')
def startHeavyProcess():
    heavy_process = Process(target=heavyProcess, daemon=True)
    heavy_process.start()
    return 'process has started'


def heavyProcess():
    for x in range(1, 100):
        print(x)
