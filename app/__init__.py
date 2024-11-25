from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Ubah ini

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    # Daftarkan blueprint
    from app.routes import auth, main
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(main)

    return app