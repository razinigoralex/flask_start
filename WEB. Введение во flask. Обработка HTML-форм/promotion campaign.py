from flask import Flask


def mars_colonisation(name):
    app = Flask(name)

    @app.route('/')
    def main_screen():
        return '''Миссия Колонизация Марса'''

    @app.route('/index')
    def index():
        return '''И на Марсе будут яблони цвести!'''

    @app.route('/promotion')
    def promotion():
        promote_list = ['Человечество вырастает из детства.',
                        'Человечеству мала одна планета.',
                        'Мы сделаем обитаемыми безжизненные пока планеты.',
                        'И начнем с Марса!',
                        'Присоединяйся!']

        return '</br>'.join(promote_list)

    return app


if __name__ == '__main__':
    app = mars_colonisation(__name__)
    app.run(port=8080, host='127.0.0.1')
