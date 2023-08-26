from flask import Flask, request, render_template, session
from utils import predict_type

app = Flask(__name__, template_folder='templates')
app.secret_key = "secret secret key"

menu = [{"name": "Поиск адреса", "url": ""},
        {"name": "Результат", "url": "main"}]

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
