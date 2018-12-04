import  numpy
# -*- coding: utf-8 -*-
from keras import backend as K
from keras.preprocessing import sequence
import keras.utils
from django.shortcuts import render

import codecs
from keras.models import model_from_yaml


#Переход на 'index.html'
def home(request):
    return render(request, 'index.html')

#Переход на about.html
def about (request):
    return render(request, 'about.html')

#Переход на document.html
def document(request):
    return render(request, 'document.html')

# Функция предсказания
def predict_sentiment(fulltext):
    # Загружаем данные об архитектуре сети
    yaml_file = codecs.open("mnist_model.yml", "r","utf_8_sig")
    loaded_model_yaml = yaml_file.read()
    yaml_file.close()
    # Создаем модель
    loaded_model = model_from_yaml(loaded_model_yaml)
    # Загружаем сохраненные веса в модель
    loaded_model.load_weights('model.h5')
    # Выставляем максимальную длинну отзыва
    max_review_length = 250
    # В переменную text добавляем fulltext в виде массива
    text=numpy.array([fulltext])
    #Векторизуем текстовый корпус, превращая каждый текст в последовательность целых чисел
    tk = keras.preprocessing.text.Tokenizer(num_words=None, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~ ', lower=True, split=' ', char_level=False, oov_token=None, document_count=0)
    tk.fit_on_texts(text)
    # Генерирует выходные предсказания для входных выборок
    score = loaded_model.predict(sequence.pad_sequences(tk.texts_to_sequences(text), maxlen=max_review_length))
    K.clear_session()
    return score

#Функция анализа тональности текста
def analysis(request):

    fulltext = request.GET['fulltext']
    if not fulltext:
        sentiment = "некорректные"
        return render(request, 'analysis.html', {'sentiment': sentiment})
    score = predict_sentiment(fulltext)
    if score >= 0.5:
        sentiment = "позитивным"
    else:
        sentiment = "негативным"
    return render(request, 'analysis.html', {'sentiment': sentiment, 'score': score})


