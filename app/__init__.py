#-*-coding:utf-8-*-
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from config import config

bootstrap=Bootstrap()
mail=Mail()
db=SQLAlchemy()
cache=Cache()


def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    cache.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .book import book_blueprint
    app.register_blueprint(book_blueprint,url_prefix='/book')
    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app