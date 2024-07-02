from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index/')
def html_index():
    return render_template('catalog.html')


if __name__ == '__main__':
    app.run(debug=True)