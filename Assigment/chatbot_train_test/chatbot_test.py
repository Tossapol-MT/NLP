import pickle
from colorama import Fore, Style, Back
import json
import numpy as np
from tensorflow import keras

import colorama
colorama.init()


with open("json/intents.json", encoding="utf-8") as file:
    data = json.load(file)

    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20


def chat(text):
    result = model.predict(keras.preprocessing.sequence.pad_sequences(
        tokenizer.texts_to_sequences([text]), truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])
    for i in data['intents']:
        if i['tag'] == tag:
            return np.random.choice(i['responses'])
        
