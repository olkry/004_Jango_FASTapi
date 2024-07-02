from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('index.html', **context)


@app.route('/contacts/')
def contacts():
    context = {'title': 'Контакты'}
    return render_template('contacts.html', **context)


@app.route('/catalog/')
def catalog():
    context = {'title': 'Каталог'}
    return render_template('catalog.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
