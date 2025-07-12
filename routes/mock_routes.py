from flask import Blueprint, request, jsonify
from mocks.manager import (
    add_mock, get_mocks, get_mock_by_id, update_mock, delete_mock
    ) 
from mocks.mock_handler import match_mock

mock_blueprint = Blueprint('mock_api', __name__)


@mock_blueprint.route("/mocks", methods=["POST"])
def create_mock(): # It creates a new mock
    data = request.json
    result = add_mock(data)
    return jsonify(result), 201 # Created. 201 is the HTTP status code for a successful creation

@mock_blueprint.route("/mocks", methods=["GET"])
def list_mocks(): # It list all mocks
    return jsonify(get_mocks())  

@mock_blueprint.route("/mocks/<mock_id>", methods=["PUT"])
def edit_mock(mock_id): # It updates an existing mock
    data = request.json
    updated = update_mock(mock_id, data)
    if updated:
        return jsonify(updated)
    return jsonify({"error": "Mock no encontrado"}), 404

@mock_blueprint.route("/mocks/<mock_id>", methods=["DELETE"])
def remove_mock(mock_id):
    if delete_mock(mock_id):
        return jsonify({"message": "Mock eliminado"})
    return jsonify({"error": "Mock no encontrado"}), 404


@mock_blueprint.route("/mock/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def handle_mock(path): # It handles requests to the mock endpoint
    # path is the URL path after /mock/
    method = request.method
    params = request.args.to_dict()
    body = request.get_json(silent=True)
    matched = match_mock("/" + path, method, params)
    if matched:
        return jsonify(matched["response"].get("body", {})), matched["response"].get("status", 200)
    return jsonify({"error": "Mock no encontrado"}), 404