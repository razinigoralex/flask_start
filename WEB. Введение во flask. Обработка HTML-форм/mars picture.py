from flask import Flask, url_for


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

    @app.route('/image_mars')
    def mars_image():
        return f'''<!doctype html>
                   <html lang="en">
                    <head>
                     <meta charset="utf-8">
                     <title>Привет, Марс!</title>
                    </head>
                    <body>
                     <h1>Жди нас, Марс!</h1>
                     <figure>
                      <img src='{url_for('static', filename='img/mars.png')}'>
                      <figcaption>
                       Вот она какая, красная планета.
                      </figcaption>
                     </figure>
                    </body>
                   </html>'''

    return app


if __name__ == '__main__':
    app = mars_colonisation(__name__)
    app.run(port=8080, host='127.0.0.1')
