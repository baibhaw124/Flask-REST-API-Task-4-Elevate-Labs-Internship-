from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = [
    {"id": 1, "name": "Baibhaw", "email": "baibhaw123@gmail.com"},
]

@app.route('/')
def home():
    return "Welcome to the Flask REST API!."


# GET - (Fetch all users)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# POST -(Add a new user)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data.get("name"),
        "email": data.get("email")
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT - (Update an existing user)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            user["email"] = data.get("email", user["email"])
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# DELETE - (Delete a user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
