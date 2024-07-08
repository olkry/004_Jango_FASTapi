from pathlib import PurePath, Path
import logging
from flask import Flask, url_for, request, render_template
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)
logger = logging.getLogger(__name__)

@app.route('/main/')
@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'


# @app.route('/<path:file>/')
# def get_file(file):
#     print(file)
#     # return f'Ваш файл находится в: {file}!'
#     return f'Ваш файл находится в: {escape(file)}!'


@app.route('/test_url_for/<int:num>/')
def url_test(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("url_test", num=42) = }<br>'
    text += f'Функция {url_for("url_test", num=42, data="new_data") = }<br>'
    text += f'Функция {url_for("url_test", num=42, data="new_data", pi=3.14515) = }<br>'
    return text


@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок.<br>'
    return text + f'{request.args}'


# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         return f'Hello {name}!'
#     return render_template('submit_post.html')


@app.get('/submit')
def submit_get():
    return render_template('submit_post.html')


@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


if __name__ == '__main__':
    app.run(debug=True)
