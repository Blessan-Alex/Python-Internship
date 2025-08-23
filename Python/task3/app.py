from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage: {id: {"name": ..., "email": ...}}
users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or 'id' not in data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing user data"}), 400
    if data['id'] in users:
        return jsonify({"error": "User already exists"}), 400
    users[data['id']] = {"id": data['id'], "name": data['name'], "email": data['email']}
    return jsonify(users[data['id']]), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    users[user_id].update({k: v for k, v in data.items() if k in ['name', 'email']})
    return jsonify(users[user_id]), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)