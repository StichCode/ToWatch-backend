import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or 'postgresql+psycopg2://watcher:12345@localhost:5432/whattosee'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "1"
