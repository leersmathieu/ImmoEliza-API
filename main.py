from flask import Flask, render_template, jsonify, request
import pickle
import pandas as pd
import random
import os

app = Flask(__name__)
house_model, house_scaler = pickle.load(open(f"./model_bin/house_model.p", "rb"))
apart_model, apart_scaler = pickle.load(open(f"./model_bin/apart_model.p", "rb"))

ratio_fb_convertor = pd.read_csv('./dataset/geocoding_data.csv', sep=',')



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
    if content['type_of_property'] == 0:  # House

        df_converter = ratio_fb_convertor[ratio_fb_convertor['postal_code'] == content['postal_code']]
        print(df_converter)
        content['ratio_free_build'] = df_converter['ratio_free_build'].values[0]
        print(type(content['ratio_free_build']))
        order = [[content['postal_code'],
                  content['number_of_bedroom'],
                  content['house_area'],
                  content['fully_equipped_kitchen'],
                  content['terrace'],
                  content['garden'],
                  content['number_of_facades'],
                  content['swimming_pool'],
                  content['is_new'],
                  content['ratio_free_build']]]
        print(order)

        content['PREDICTION'] = int(house_model.predict(house_scaler.transform(order))[0])
    else:  # Apartment
        order = [[content['postal_code'],
                  content['number_of_bedroom'],
                  content['house_area'],
                  content['fully_equipped_kitchen'],
                  content['terrace'],
                  content['is_new']]]
        print(order)

        content['PREDICTION'] = int(apart_model.predict(apart_scaler.transform(order))[0])
    return content


if __name__ == '__main__':
    app.run("0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
