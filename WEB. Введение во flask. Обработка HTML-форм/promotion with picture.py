from flask import Flask, url_for


def mars_colonisation(name):
    app = Flask(name)
    promote_list = ['Человечество вырастает из детства.',
                    'Человечеству мала одна планета.',
                    'Мы сделаем обитаемыми безжизненные пока планеты.',
                    'И начнем с Марса!',
                    'Присоединяйся!']

    @app.route('/')
    def main_screen():
        return '''Миссия Колонизация Марса'''

    @app.route('/index')
    def index():
        return '''И на Марсе будут яблони цвести!'''

    @app.route('/promotion')
    def promotion():
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
    
    @app.route('/promotion_image')
    def promotion_image():
        return f'''<!doctype html>
                   <html lang="en">
                    <head>
                     <meta charset="utf-8">
                     <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css' 
                                 rel='stylesheet' 
                                 integrity='sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl' 
                                 crossorigin='anonymous'>
                     <link rel='stylesheet' 
                           type='text/css'
                           href='{url_for('static', filename='css/promotion_image_style.css')}'>
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
                     <div class="alert alert-primary" role="alert">
                      {promotion()}
                     </div>
                    </body>
                   </html>'''
    
    return app


if __name__ == '__main__':
    app = mars_colonisation(__name__)
    app.run(port=8080, host='127.0.0.1')
