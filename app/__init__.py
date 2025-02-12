from flask import Flask

from .routes.main import main
from .config import Config
from .extensions import db, migrate, login_manager


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # регистрация блупринт
    app.register_blueprint(main)

    login_manager.init_app(app)
    # логин менеджер

    login_manager.login_view = 'main.login'
    login_manager.login_message = 'Необходима авторизация'
    login_manager.login_message_category = 'info'

    with app.app_context():
        db.create_all()

    return app