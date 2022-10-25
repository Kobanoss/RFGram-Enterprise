from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from .config import DB_CONF
from .config import APP_CONF

app = Flask(__name__)
for param, value in APP_CONF.PARAMETERS.items():
    app.config[param] = value

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from .routes import views
from .models.models import User

app.register_blueprint(views, url_prefix='/')

if not path.exists(APP_CONF.PARAMETERS['SQLALCHEMY_DATABASE_URI']):
    with app.app_context():
        db.create_all()

