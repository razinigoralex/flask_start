from flask import Flask, render_template


def mars_colonisation(name):
    app = Flask(name)

    @app.route('/')
    @app.route('/index')
    def main_screen():
        return render_template('base.html', title='Заготовка')

    @app.route('/training/<prof>')
    def show_training(prof):
        return render_template('training.html', prof=prof)

    @app.route('/list_prof/<list>')
    def show_professions(list):
        return render_template('professions.html', list=list)

    return app


if __name__ == '__main__':
    app = mars_colonisation(__name__)
    app.run(port=8080, host='127.0.0.1')