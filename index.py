from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Домашняя страница')


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<mark>')
def list_prof(mark):
    proffesions = ['инженер - исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
                   'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
                   'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']

    return render_template('list_prof.html', professions=proffesions, mark=mark)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
