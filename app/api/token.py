import base64
import os
import random
from datetime import datetime, timedelta

import jwt
from werkzeug.security import check_password_hash

from app import db
from app.models import Users
from config import Config


class Token(object):

    def __init__(self, user: Users, old_token=None):
        self.user = user
        self.old_token = old_token
        self.db_token = user.token
        self.new_token = self.__new_token__()

    def __repr__(self):
        res = self.decode_token()
        print(res, type(res))
        return res

    def __new_token__(self):
        new_token = base64.b64encode(os.urandom(random.randint(15, 100))).decode('utf-8')
        self.user.token = jwt.encode(new_token, Config.SECRET_KEY, algorithm='HS256')
        self.user.token_expiration = datetime.utcnow() + timedelta(seconds=3600)
        db.session.add(self.user)
        db.session.commit()
        return new_token

    def decode_token(self):
        return jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])

    def revoke_token(self):
        self.user.token = 'nothing'
        self.user.token_expiration = datetime.utcnow() - timedelta(seconds=1)
        db.session.add(self.user)
        return

    def refresh_token(self):
        if self.old_token is None or not self.verify_token():
            return
        if self.decode_token(self.db_token) == self.user.token:
            return self.decode_token()

    def verify_token(self):
        if self.user.token_expiration < datetime.utcnow():
            return False
        return True


def get_token(username, password=None, token=None):
    user = Users.query.filter_by(username=username).first()
    if user is None:
        return None

    if token is not None:
        # This rule will work if user need to refresh password
        new_tok = Token(user, old_token=token)
        if new_tok.verify_token():
            return new_tok.refresh_token()
    if password is not None and check_password_hash(user.password_hash, password):
        tokens = Token(user)
        print(tokens)
        return tokens
    return None
