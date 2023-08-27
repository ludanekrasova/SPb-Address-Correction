from flask import Flask, request, render_template, session
import pandas as pd
from sentence_transformers import SentenceTransformer
from annoy import AnnoyIndex

app = Flask(__name__, template_folder='templates')
app.secret_key = "secret secret key"

menu = [{"name": "Поиск адреса", "url": ""},
        {"name": "Результат", "url": "main"}]

data = pd.read_csv("data/building_20230808.csv")[['id', 'full_address']]

model = SentenceTransformer('intfloat/multilingual-e5-small')
#model = SentenceTransformer('model/multilingual-e5-small')

t = AnnoyIndex(384, 'angular')
t.load('model/train.ann') 

def predict_type(text, data):
    '''Предсказание'''

    embedding = model.encode(text, convert_to_tensor=False)
    prediction = t.get_nns_by_vector(embedding, 1)[0]
    building_id = data['id'][prediction]#.values[0]
    target_address = data['full_address'][prediction]#.values[0]

    return building_id, target_address


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('main.html', title="Проверка адреса", menu=menu)

    if request.method == 'POST':
        text = request.form['text']
        session['text'] = text
        success = "true"

        building_id, target_address = predict_type(text, data)

        return render_template('main.html', predict_text =text, result='"success": {}, "query:": ["address": {}], "result": ["target_building_id": {},"target_address": {}]'.format(success, text, building_id, target_address), menu=menu)


@app.route('/upload', methods=['POST'])
def upload():
    # Обработка загрузки файла и проверка
    # Ваш код для обработки загрузки файла и получения результатов

    return render_template('upload_result.html', predict_text="Результат загрузки",
                           result="Результаты проверки", menu=menu)


if __name__ == '__main__':
    app.run(debug=True, port=5005)
