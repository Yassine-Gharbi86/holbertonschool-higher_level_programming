from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended.exceptions import (
    NoAuthorizationError, InvalidHeaderError, JWTExtendedException
)
from werkzeug.exceptions import Unauthorized

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here_for_jwt'
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify password"""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Protected route"""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Login route"""
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 401

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 401

    user = users.get(username, None)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Bad username or password"}), 401

    access_token = create_access_token(identity={
        'username': username,
        'role': user['role']
        }
    )
    return jsonify({"access_token": access_token}), 200


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Protected route"""
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Protected route"""
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@app.errorhandler(Unauthorized)
def handle_unauthorized(e):
    """Handle unauthorized error"""
    return jsonify({"error": "Unauthorized"}), 401


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle unauthorized error"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token error"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired token error"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle needs fresh token error"""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    """Run the app"""
    app.run(port=5000, debug=False)
