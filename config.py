import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.setdefault("DATABASE_URL",
                                                    'postgresql+psycopg2://tasksnote:12345@localhost:5432/tasksnote')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "1"
