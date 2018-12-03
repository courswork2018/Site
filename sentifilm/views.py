import  numpy
# -*- coding: utf-8 -*-
from keras import backend as K
from keras.preprocessing import sequence
import keras.utils
from django.shortcuts import render

import codecs
from keras.models import model_from_yaml



def home(request):
    return render(request, 'index.html')

def about (request):
    return render(request, 'about.html')

def document(request):
    return render(request, 'document.html')

def predict_sentiment(fulltext):
    # with open('mnist_model.h5',encoding='cp251') as jsonfile:
    #     json_file = json.load(jsonfile)
 #  Загружаем данные об архитектуре сети
    yaml_file = codecs.open("mnist_model.yml", "r","utf_8_sig")
    loaded_model_yaml = yaml_file.read()
    yaml_file.close()
    # Создаем модель
    loaded_model = model_from_yaml(loaded_model_yaml)
    # Загружаем сохраненные веса в модель
    loaded_model.load_weights('model.h5')

    max_review_length = 250
    text=numpy.array([fulltext])
    tk = keras.preprocessing.text.Tokenizer(num_words=None, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~ ', lower=True,
                                            split=' ', char_level=False, oov_token=None, document_count=0)
    tk.fit_on_texts(text)
    score = loaded_model.predict(sequence.pad_sequences(tk.texts_to_sequences(text), maxlen=max_review_length))
    K.clear_session()
    return score

def text(fulltext):
    score = predict_sentiment(fulltext)
    return score

def analysis(request):

    fulltext = request.GET['fulltext']
    score = predict_sentiment(fulltext)


    if score > 0.5:
        sentiment = "позитивным"
    else:
        sentiment = "негативным"

    return render(request, 'analysis.html', {'sentiment': sentiment, 'score': score})


