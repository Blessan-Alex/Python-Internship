## Task 4: Build a REST API with Flask

This directory contains a minimal REST API for managing users, implemented with Flask and an in-memory data store.

### Features
- **GET /users**: list all users
- **GET /users/<id>**: get one user by id
- **POST /users**: create a new user (JSON body)
- **PUT /users/<id>**: update an existing user (JSON body)
- **DELETE /users/<id>**: delete a user by id

### Requirements
- Python 3.10+

### Setup (Windows PowerShell)
```powershell
cd task4
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Run the API
```powershell
python app.py
```
The server listens on `http://127.0.0.1:5000`.

### Example Requests (cURL)

- Create a user
```bash
curl -s -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com"}'
```

- List users
```bash
curl -s http://127.0.0.1:5000/users
```

- Get one user
```bash
curl -s http://127.0.0.1:5000/users/1
```

- Update a user
```bash
curl -s -X PUT http://127.0.0.1:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"email": "alice+new@example.com"}'
```

- Delete a user
```bash
curl -i -X DELETE http://127.0.0.1:5000/users/1
```

### Postman Tips
- Set the request body to **raw** and **JSON** for POST/PUT.
- Include `Content-Type: application/json` header.

### Notes
- Data is not persisted. Restarting the server resets the in-memory store.
- For persistence, replace the in-memory dict with a database (e.g., SQLite, PostgreSQL). See `interview_answers.md` for a brief discussion.

