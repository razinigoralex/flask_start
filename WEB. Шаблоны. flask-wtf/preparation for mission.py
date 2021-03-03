from flask import Flask, render_template


def mars_colonisation(name):
    app = Flask(name)

    @app.route('/')
    @app.route('/index')
    def main_screen():
        return render_template('base.html', title='Заготовка')

    return app


if __name__ == '__main__':
    app = mars_colonisation(__name__)
    app.run(port=8080, host='127.0.0.1')
