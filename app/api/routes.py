from flask import request, jsonify

from app.api import bp


@bp.route("/test", methods=["GET"])
def test():
    return jsonify(message="Test"), 200