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

## Interview Questions & Answers

### Flask & REST API Concepts

**1. What is Flask?**
Flask is a lightweight, micro web framework for Python that allows you to build web applications quickly. It's minimal and flexible, providing the essentials for web development without unnecessary complexity.

**2. What is REST?**
REST (Representational State Transfer) is an architectural style for designing networked applications. It uses HTTP methods (GET, POST, PUT, DELETE) to perform CRUD operations on resources, making APIs stateless and scalable.

**3. Difference between GET and POST?**
- **GET**: Used to retrieve data, parameters sent in URL, idempotent, cacheable
- **POST**: Used to create/submit data, parameters sent in request body, not idempotent, not cacheable

**4. How does a Flask route work?**
Flask routes use decorators to map URL patterns to Python functions. When a request matches the route pattern, Flask calls the associated function and returns the response.

**5. What is request.json?**
`request.json` is a Flask property that contains the parsed JSON data from the request body. It's used to access JSON data sent in POST/PUT requests.

**6. What are status codes like 200, 404?**
HTTP status codes indicate the result of a request:
- **200**: OK (success)
- **201**: Created (resource created successfully)
- **400**: Bad Request (client error)
- **404**: Not Found (resource not found)
- **500**: Internal Server Error (server error)

**7. How do you run a Flask app?**
```python
if __name__ == '__main__':
    app.run(debug=True)
```
Or from command line: `python app.py`

**8. What is JSON?**
JSON (JavaScript Object Notation) is a lightweight data interchange format. It's easy for humans to read/write and for machines to parse/generate. Used for API data exchange.

**9. How to test an API?**
- **Postman**: GUI tool for API testing
- **curl**: Command-line tool for HTTP requests
- **Browser**: For GET requests
- **Unit tests**: Automated testing with frameworks like pytest

**10. Can we use a database instead of memory?**
Yes! Flask can integrate with databases like:
- **SQLite**: Lightweight, file-based database
- **PostgreSQL**: Robust, feature-rich database
- **MySQL**: Popular relational database
- **MongoDB**: NoSQL document database
- **SQLAlchemy**: ORM for database operations