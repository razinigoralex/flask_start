from flask import Flask


def mars_colonisation(name):
    app = Flask(name)

    @app.route('/')
    def main_screen():
        return '''Миссия Колонизация Марса'''

    @app.route('/index')
    def index():
        return '''И на Марсе будут яблони цвести!'''

    return app


if __name__ == '__main__':
    app = mars_colonisation(__name__)
    app.run(port=8080, host='127.0.0.1')
