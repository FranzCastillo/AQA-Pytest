from flask import Blueprint, jsonify, request
from app.auth import login, register_user

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)


@main_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@main_bp.route("/users", methods=["GET"])
def get_users():
    from app.auth import get_users_list
    return jsonify({"users": get_users_list()}), 200


@auth_bp.route("/login", methods=["POST"])
def login_endpoint():
    data = request.json
    if not data:
        return jsonify({"message": "Missing request body"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password required"}), 400

    if login(username, password):
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401


@auth_bp.route("/register", methods=["POST"])
def register_endpoint():
    data = request.json
    if not data:
        return jsonify({"message": "Missing request body"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password required"}), 400

    if register_user(username, password):
        return jsonify({"message": "User registered successfully"}), 201
    return jsonify({"message": "Username already exists"}), 409
