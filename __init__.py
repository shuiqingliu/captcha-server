import functools
from flask import Flask,render_template
import captcha
from config import GLOBAL

def create_app():
    app = Flask(__name__)  #create app instance
    app.register_blueprint(captcha.bp)  #register blueprint

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == '__main__':
    create_app().run(port=int(GLOBAL["Port"]))
