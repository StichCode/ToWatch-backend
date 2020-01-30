import os


class Config(object):
    DATABASE_URL = os.environ.get("DATABASE_URL") or 'postgresql+psycopg2://watcher:1234@localhost:5432/w2s'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ''