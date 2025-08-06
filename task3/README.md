# Task 3: Flask REST API

## How to Run

1. Install Flask if you haven't already:
   ```bash
   pip install flask
   ```
2. Start the server:
   ```bash
   python app.py
   ```

## API Endpoints

- **GET /users**: List all users
- **GET /users/<id>**: Get a user by ID
- **POST /users**: Create a new user (JSON: id, name, email)
- **PUT /users/<id>**: Update user name/email
- **DELETE /users/<id>**: Delete a user

## Example curl Commands

- **Create a user:**
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"id":1,"name":"Alice","email":"alice@example.com"}' http://127.0.0.1:5000/users
  ```
- **Get all users:**
  ```bash
  curl http://127.0.0.1:5000/users
  ```
- **Get a user by ID:**
  ```bash
  curl http://127.0.0.1:5000/users/1
  ```
- **Update a user:**
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"name":"Alice Smith"}' http://127.0.0.1:5000/users/1
  ```
- **Delete a user:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/users/1
  ```

## Notes
- Data is stored in memory and will reset when the server restarts.
- You can also use Postman to test the API.