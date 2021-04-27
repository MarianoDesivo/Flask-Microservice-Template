from flask import Flask
from multiprocessing import Process

app = Flask(__name__)

@app.route("/")
def home():
    return 'hello'

@app.route('/startheavy')
def startHeavyProcess():
    heavy_process = Process(target=heavyProcess, daemon=True)
    heavy_process.start()
    return 'process has started'


def heavyProcess():
    for x in range(1, 100):
        print(x)
