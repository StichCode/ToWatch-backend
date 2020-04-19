from flask import request, jsonify

from app.api import bp
from app.database.models import Films


@bp.route("/films", methods=["GET"])
def get_films():
    data = Films.all_to_dict()
    if not data:
        return jsonify(message="fuck u"), 404
    return jsonify(data), 200


@bp.route("/films", methods=["POST"])
def create_films():
    data = request.args.to_dict()
    film = Films.from_dict(data)
    if not film:
        return jsonify(message="fuck u"), 404
    return jsonify(message="All ok"), 201