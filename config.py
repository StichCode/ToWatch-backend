import os


class Config(object):
    LOGIN = ''
    PASS = ''
    URL = ''
    PORT = ''
    DATABASE = ''
    url = f"postgresql+psycopg2://{LOGIN}:{PASS}@{URL}:{PORT}/{DATABASE}"
    SQLALCHEMY_DATABASE_URI = os.environ.setdefault("DATABASE_URL",
                                                    url)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "1"
