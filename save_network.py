from keras.models import model_from_json
import numpy
from keras.preprocessing import sequence
import keras.utils

def loading_rnn():
    print("Загружаю сеть из файлов")
    # Загружаем данные об архитектуре сети
    json_file = open("models/mnist_model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    # Создаем модель
    loaded_model = model_from_json(loaded_model_json)
    # Загружаем сохраненные веса в модель
    loaded_model.load_weights("models/mnist_model.h5")
    print("Загрузка сети завершена")
    return loaded_model

def work_rnn(text, loaded_model):
    max_review_length = 250
    text = numpy.array([text])
    # print(text.shape)
    tk = keras.preprocessing.text.Tokenizer(num_words=None, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~ ', lower=True,
                                            split=' ', char_level=False, oov_token=None, document_count=0)
    tk.fit_on_texts(text)
    prediction = loaded_model.predict(sequence.pad_sequences(tk.texts_to_sequences(text), maxlen=max_review_length))
    print(prediction)
    return prediction

def input_text():
    print('Введите отзыв')
    text = input()
    return  text

if __name__=="__main__":
    loaded_model = loading_rnn()
    text = input_text()
    work_rnn(text, loaded_model)