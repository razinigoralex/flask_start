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

    @app.route('/astronaut_selection', methods=['GET'])
    def get_astronaut_form():
        return f'''<!doctype html>
                   <html lang='en'>
                    <head>
                     <meta charset='utf-8'>
                     <meta name='viewport' 
                           content='width=device-width, initial-scale=1, shrink-to-fit=no'>
                     <link rel='stylesheet'
                           href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css'
                           integrity='sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1'
                           crossorigin='anonymous'>
                     <title>Анкета претендента на участие в миссии</title>
                    </head>
                    <body>
                     <h1>Анкета претендента на участие в миссии</h1>
                     <div>
                      <form class='login_form' method='post'>
                       <input type='text' 
                              class='form-control' 
                              id='surname' 
                              placeholder='Введите фамилию' 
                              name='surname'>
                       <input type='text' 
                              class='form-control' 
                              id='name' 
                              placeholder='Введите имя' 
                              name='name'>
                       <input type='email'
                              class='form-control'
                              id='email'
                              placeholder='Введите адрес электронной почты'
                              name='email'>
                       <div class='form-group'>
                        <label for='classSelect'>Какое у вас образование?</label>
                        <select class='form-control' 
                                id='educationSelect' 
                                name='education'>
                         <option>Начальное</option>
                         <option>Среднее</option>
                         <option>Среднее профессиональное</option>
                         <option>Высшее</option>
                        </select>
                       </div>
                       <div class='form-group'>
                        <label for='about'>Какие у вас есть профессии?</label>
                        <div class='form-group form-check'>
                         <input type='checkbox' class='form-check-input' id='engineer_explorer' name='engineer_explorer'>
                         <label class='form-check-label' for='engineer_explorer'>Инженер-исследователь</label>
                        </div>
                        <div class='form-group form-check'>
                         <input type='checkbox' class='form-check-input' id='pilot' name='pilot'>
                         <label class='form-check-label' for='pilot'>Пилот</label>
                        </div>
                        <div class='form-group form-check'>
                         <input type='checkbox' class='form-check-input' id='builder' name='builder'>
                         <label class='form-check-label' for='builder'>Строитель</label>
                        </div>
                        <div class='form-group form-check'>
                         <input type='checkbox' class='form-check-input' id='exobiologist' name='exobiologist'>
                         <label class='form-check-label' for='exobiologist'>Экзобиолог</label>
                        </div>
                        <div class='form-group form-check'>
                         <input type='checkbox' class='form-check-input' id='medic' name='medic'>
                         <label class='form-check-label' for='medic'>Врач</label>
                        </div>
                        <div class='form-group form-check'>
                         <input type='checkbox' class='form-check-input' id='engineer_terraforer' name='engineer_terraformer'>
                         <label class='form-check-label' for='engineer'>Инженер по терраформированию</label>
                        </div>
                        <div class='form-group form-check'>
                         <input type='checkbox' class='form-check-input' id='climatolog' name='climatolog'>
                         <label class='form-check-label' for='climatolog'>Климатолог</label>
                        </div>
                       </div>
                       <div class='form-group'>
                        <label for='form-check'>Укажите пол</label>
                        <div class='form-check'>
                         <input class='form-check-input' 
                                type='radio' 
                                name='sex' 
                                id='male' 
                                value='male' 
                                checked>
                         <label class='form-check-label' for='male'>Мужской</label>
                        </div>
                        <div class='form-check'>
                         <input class='form-check-input' 
                                type='radio' 
                                name='sex' 
                                id='female' 
                                value='female'>
                         <label class='form-check-label' for='female'>Женский</label>
                        </div>
                       </div>
                       <div class='form-group'>
                        <label for='motivation'>Какова ваша мотивация?</label>
                        <textarea class='form-control' id='motivation' name='motivation' rows='5'></textarea>
                       </div>
                       <div class='form-group form-check'>
                        <input type='checkbox' class='form-check-input' id='acceptStay' name='accept'>
                        <label class='form-check-label' for='acceptRules'>Готовы остаться на Марсе?</label>
                       </div>
                       <button type='submit' class='btn btn-primary'>Записаться</button>
                      </form>
                     </div>
                    </body>
                   </html>'''

    @app.route('/astronaut_selection', methods=['POST'])
    def post_astronaut_form():
        return '''Поздравляем! Вы успешно записались.'''

    return app


if __name__ == '__main__':
    app = mars_colonisation(__name__)
    app.run(port=8080, host='127.0.0.1')
