from flask import Flask, request, jsonify

app = Flask(__name__)

# Users dictionary without 'username' in the user data
users = {
    "jane": {
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
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
        user_data = user.copy()
        user_data["username"] = username
        return jsonify(user_data)
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

    # Store user data without 'username' key
    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    user_data = users[username].copy()
    user_data["username"] = username
    return jsonify({"message": "User added", "user": user_data}), 201

if __name__ == "__main__":
    app.run(port=5000, debug=False)
