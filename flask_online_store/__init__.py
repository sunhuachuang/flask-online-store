from flask import Flask, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from .models import db, cache


__version__ = '0.1'
__status__ = 'dev'
__description__ = 'Simple shopsite system powered by Flask'
__github__ = 'https://github.com/sunhuachuang/flask-online-store'
__license__ = "MIT License"


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config')

    # you must create a file: ../instance/config.py
    # a new config.py in instance to reload the config.py
    app.config.from_pyfile('config.py')

    register_debug(app)
    register_database(app)
    register_blueprint(app)
    init_login(app)

    return app

def register_debug(app):
    toolbar = DebugToolbarExtension()  # Setting up the debug toolbar step1
    toolbar.init_app(app)  # Setting up the debug toolbar step2

def register_log():
    import logging
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)


def register_database(app):
    db.init_app(app)
    db.app = app
    #cache.init_app(app)
    # db.create_all() #create tables;


def register_blueprint(app):
    from .views import register_blueprints
    register_blueprints(app)


def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(user_id)

    def unauthorized():
        return redirect(url_for('admin_security.login'))

    login_manager.unauthorized = unauthorized
