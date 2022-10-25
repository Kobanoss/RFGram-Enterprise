from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from application.config import DB_CONF
from application.config import APP_CONF

app = Flask(__name__)
for param, value in APP_CONF.PARAMETERS.items():
    app.config[param] = value

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
admin = Admin(app, name='RFGram', template_mode='bootstrap3')

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from application.routes import views
from application.models.models import User, Post, Comment, Notif

app.register_blueprint(views, url_prefix='/')

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Comment, db.session))
admin.add_view(ModelView(Notif, db.session))


with app.app_context():
    db.create_all()
    db.session.commit()

