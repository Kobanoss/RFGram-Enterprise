from application.config.db_conf import DB_CONF
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class APP_CONF:
    PARAMETERS = {'SECRET_KEY': '0eeff27f9c89ab975e01c1eb5aeef5148b1810e9b690a77bedd94a261b3d9b98',
                  'SQLALCHEMY_DATABASE_URI': f'{os.getenv("DATABASE_URL", "sqlite://")}',
                  'SQLALCHEMY_TRACK_MODIFICATIONS': True,
                  'FLASK_ADMIN_SWATCH': 'cerulean'}
