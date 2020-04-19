import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.setdefault("DATABASE_URL",
                                                    'postgresql+psycopg2://tasknote:12345@localhost:5432/tasknote')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "1"
