from flask import Flask
from flask import request
import random
import os

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World !"


@app.route('/status')
def status():
    return {'server_status': "Alive!"}


@app.route('/predict/<int:number_of_room>/<int:surface>')
def predict(number_of_room, surface):
    return f"Prediction (Chamber :{number_of_room},  surface :{surface}) =  {random.randint(200000, 500000)} €"


if __name__ == '__main__':
    app.run("0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)