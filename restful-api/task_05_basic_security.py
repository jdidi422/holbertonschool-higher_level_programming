#!/usr/bin/python3
'''This module is for basic security in Flask'''

from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_jwt_extended import JWTManager, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
import datetime

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        if check_password_hash(users[username]['password'], password):
            return username


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protected by basic authentication."""
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route("/login", methods=["POST"])
def login():
    """Handles login and generates a JWT token."""
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if (username in users
            and check_password_hash(users[username]['password'], password)):
        token = create_access_token(identity=username)
        return jsonify(token=token)
    else:
        return jsonify({"error": "Invalid username or password"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Route protected by JWT."""
    return "JWT Auth: Access Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handles errors for missing token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handles errors for invalid token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handles errors for expired token."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handles errors for revoked token."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handles errors requiring a fresh token."""
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route restricted to administrators only."""
    current_user = get_jwt_identity()
    if users[current_user]['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200


@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    """Refreshes the JWT token."""
    pass


if __name__ == "__main__":
    app.run(debug=True)
