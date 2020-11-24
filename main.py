from flask import Flask, render_template, jsonify, request
import random
import os

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Distant API for price prediction</h1><p>This site is a prototype API for predict price from a real " \
           "estate.</p> "


@app.route('/status')
def status():
    return {'server_status': "Alive!"}


@app.route('/predict/', methods=['POST'])
def predict():

    content = request.get_json()
    content['PREDICTION'] = random.randint(200_000, 500_000)

    return content




if __name__ == '__main__':
    app.run("0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
