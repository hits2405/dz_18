

class Config(object):
    DEBUG = True
    SECRET_HERE = "123456789q"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}

