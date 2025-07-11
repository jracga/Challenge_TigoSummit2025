from flask import Blueprint, request, jsonify
from mocks.manager import add_mock, get_mocks
from mocks.mock_handler import match_mock

mock_blueprint = Blueprint('mock_api', __name__)

@mock_blueprint.route("/mocks", methods=["POST"])
def create_mock():
    data = request.json
    result = add_mock(data)
    return jsonify(result), 201

@mock_blueprint.route("/mocks", methods=["GET"])
def list_mocks():
    return jsonify(get_mocks())

@mock_blueprint.route("/mock/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def handle_mock(path):
    method = request.method
    params = request.args.to_dict()
    body = request.get_json(silent=True)
    matched = match_mock("/" + path, method, params)
    if matched:
        return jsonify(matched["response"].get("body", {})), matched["response"].get("status", 200)
    return jsonify({"error": "Mock no encontrado"}), 404
