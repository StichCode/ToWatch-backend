from flask import jsonify, request, url_for
from werkzeug.security import generate_password_hash

from app import db
from app.api import bp
from app.api.token import get_token
from app.models import Users


@bp.route('/login', methods=['POST'])
def auth_user():
    data = request.get_json() or {}
    print(data)
    username = data['username']
    password = data['password']
    result = get_token(username, password)
    print(result)
    return jsonify({'API_KEY': result})


@bp.route('/create_user', methods=['GET'])
def start():
    user = Users('rabbit2', generate_password_hash('12345'), 'rabbit2@pidor.ru')
    db.session.add(user)
    db.session.commit()
    return 200
