from flask import Flask, url_for, request, render_template, redirect
import json
from loginform import LoginForm

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
