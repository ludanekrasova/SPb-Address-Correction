from flask import Flask, request, render_template, session
import pandas as pd

app = Flask(__name__, template_folder='templates')
app.secret_key = "secret secret key"

menu = [{"name": "Поиск адреса", "url": ""},
        {"name": "Результат", "url": "main"}]

data = pd.read_csv("data/building_20230808.csv")


def predict_type(text):
    '''Предсказание типа письма и типа заявки'''
    data = pd.DataFrame(data={'text': [text]}, index=[0])

    #prediction = model.predict(data)
    #prediction = {"success": true, "query:": ["address": text], "result": [{"target_building_id": 209676 ,"target_address":  "г.Санкт-Петербург, Аптекарский проспект, дом 18, литера А" }]}
    prediction = {"success": "true", "query:": ["address", text], "result": [{"target_building_id", 209676 ,"target_address",  "г.Санкт-Петербург, Аптекарский проспект, дом 18, литера А" }]}

    return prediction



@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('main.html', title="Проверка адреса", menu=menu)

    if request.method == 'POST':
        text = request.form['text']
        session['text'] = text

        prediction = predict_type(text)

        return render_template('main.html', result=prediction,
                               menu=menu)

if __name__ == '__main__':
    app.run()
