from __future__ import annotations

from typing import Dict, Any, Optional

from flask import Flask, jsonify, request


def create_app() -> Flask:
    """Create and configure the Flask application.

    The application exposes a simple in-memory REST API to manage users
    with the following routes:
      - GET    /users                → list users
      - GET    /users/<id>           → get one user
      - POST   /users                → create user
      - PUT    /users/<id>           → update user
      - DELETE /users/<id>           → delete user
    """

    app = Flask(__name__)

    # In-memory store. In production this would be a database.
    users: Dict[int, Dict[str, Any]] = {}
    next_user_id: Dict[str, int] = {"value": 1}  # wrapping in dict to mutate inside closures

    def generate_user_id() -> int:
        new_id = next_user_id["value"]
        next_user_id["value"] += 1
        return new_id

    def parse_json_body() -> Optional[Dict[str, Any]]:
        if not request.is_json:
            return None
        return request.get_json(silent=True) or None

    @app.get("/")
    def root() -> Any:
        return jsonify(
            {
                "message": "User API is running",
                "routes": [
                    {"method": "GET", "path": "/users"},
                    {"method": "GET", "path": "/users/<id>"},
                    {"method": "POST", "path": "/users"},
                    {"method": "PUT", "path": "/users/<id>"},
                    {"method": "DELETE", "path": "/users/<id>"},
                ],
            }
        )

    @app.get("/users")
    def list_users() -> Any:
        return jsonify(list(users.values())), 200

    @app.get("/users/<int:user_id>")
    def get_user(user_id: int) -> Any:
        user = users.get(user_id)
        if user is None:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user), 200

    @app.post("/users")
    def create_user() -> Any:
        body = parse_json_body()
        if body is None:
            return jsonify({"error": "Expected JSON body"}), 400

        name = body.get("name")
        email = body.get("email")

        if not isinstance(name, str) or not name.strip():
            return jsonify({"error": "'name' is required and must be a non-empty string"}), 400
        if not isinstance(email, str) or not email.strip():
            return jsonify({"error": "'email' is required and must be a non-empty string"}), 400

        user_id = generate_user_id()
        user = {"id": user_id, "name": name.strip(), "email": email.strip()}
        users[user_id] = user
        return jsonify(user), 201

    @app.put("/users/<int:user_id>")
    def update_user(user_id: int) -> Any:
        if user_id not in users:
            return jsonify({"error": "User not found"}), 404

        body = parse_json_body()
        if body is None:
            return jsonify({"error": "Expected JSON body"}), 400

        provided_fields = {key: value for key, value in body.items() if key in {"name", "email"}}
        if not provided_fields:
            return jsonify({"error": "Provide at least one of: name, email"}), 400

        if "name" in provided_fields:
            name_value = provided_fields["name"]
            if not isinstance(name_value, str) or not name_value.strip():
                return jsonify({"error": "'name' must be a non-empty string"}), 400
            users[user_id]["name"] = name_value.strip()

        if "email" in provided_fields:
            email_value = provided_fields["email"]
            if not isinstance(email_value, str) or not email_value.strip():
                return jsonify({"error": "'email' must be a non-empty string"}), 400
            users[user_id]["email"] = email_value.strip()

        return jsonify(users[user_id]), 200

    @app.delete("/users/<int:user_id>")
    def delete_user(user_id: int) -> Any:
        if user_id not in users:
            return jsonify({"error": "User not found"}), 404
        del users[user_id]
        return "", 204

    # Optional: make 404s return JSON instead of HTML
    @app.errorhandler(404)
    def handle_404(error):  # type: ignore[no-redef]
        return jsonify({"error": "Not found"}), 404

    # Optional: make 400s return JSON
    @app.errorhandler(400)
    def handle_400(error):  # type: ignore[no-redef]
        return jsonify({"error": "Bad request"}), 400

    return app


app = create_app()


if __name__ == "__main__":
    # For local development convenience
    app.run(host="0.0.0.0", port=5000, debug=True)

