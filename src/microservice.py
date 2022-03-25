from flask import Flask
from multiprocessing import Process
import socket
from flask import request
from flask import jsonify
from flask import make_response

app = Flask(__name__)



@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    name = request.args.get("name")
    if(name):
        return jsonify({'ip': request.remote_addr, 'greeting': "Welcome, " + name + "!!"}), 200)
    else:
        return jsonify({'ip': request.remote_addr}), 200)

@app.route("/")
def home():
    name = request.args.get("name")
    if(name):
        response = make_response(jsonify({'ip': request.remote_addr, 'greeting': "Welcome, " + name + "!!"}), 200
    else:
        response = make_response(jsonify({'ip': request.remote_addr}), 200
    
    response.headers["x-hello-world"] = "MD"
    return response

@app.route('/startheavy')
def startHeavyProcess():
    heavy_process = Process(target=heavyProcess, daemon=True)
    heavy_process.start()
    return 'process has started'


def heavyProcess():
    for x in range(1, 100):
        print(x)
