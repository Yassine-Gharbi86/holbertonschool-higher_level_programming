from flask import Flask, request, jsonify
"""
This module provides a simple Flask API that returns a simple response.
"""


app = Flask(__name__)
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route("/")
def home():
    """
    Returns a simple response.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """
    Returns a list of all users.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    Returns a simple response.
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Returns a user by username.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user.
    """
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    """
    Starts the Flask API on port 5000.
    """
    app.run()
