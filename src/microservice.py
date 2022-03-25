from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name")
    if(name):
        response = make_response(jsonify({'ip': request.remote_addr, 'greeting': "Welcome, " + name + "!!"}), 200)
    else:
        response = make_response(jsonify({'ip': request.remote_addr}), 200)
    
    response.headers["x-hello-world"] = "MD"
    return response

