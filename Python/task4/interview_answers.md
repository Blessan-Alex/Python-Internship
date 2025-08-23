## Interview Questions: Answers

1. **What is Flask?**
   - Flask is a lightweight Python web framework for building web applications and APIs. It provides routing, request/response handling, and extensibility via extensions, while letting you choose components like databases and ORMs.

2. **What is REST?**
   - REST (Representational State Transfer) is an architectural style for building networked applications using stateless client-server communication over HTTP. It models resources with URLs and manipulates them using standard HTTP methods (GET, POST, PUT, DELETE, etc.). Responses are typically JSON.

3. **Difference between GET and POST?**
   - GET retrieves data and should not change server state. Parameters often go in the query string, and responses can be cached. POST sends data to create or process a resource, changes server state, and carries a JSON (or form) body; it is not cacheable by default.

4. **How does a Flask route work?**
   - You define a route with a decorator (e.g., `@app.get('/users')`). When a request matches the path and method, Flask calls the decorated function, which returns a response (string/tuple/`jsonify`). Path variables (like `<int:id>`) are parsed and passed as function arguments.

5. **What is `request.json`?**
   - In Flask, `request.json` (or `request.get_json()`) parses the request body as JSON when the `Content-Type` is `application/json`. It returns a Python dict (or `None` if parsing fails). Always validate and handle the case where it is missing/invalid.

6. **What are status codes like 200, 404?**
   - 200 OK: request succeeded
   - 201 Created: resource created
   - 204 No Content: request succeeded, no body returned
   - 400 Bad Request: invalid input
   - 404 Not Found: resource/route not found
   - 500 Internal Server Error: server-side error

7. **How do you run a Flask app?**
   - Simplest: `python app.py`. Alternatively: set `FLASK_APP=app:app` (module:app) and run `flask run`. Optionally set `FLASK_ENV=development` or `FLASK_DEBUG=1` during development.

8. **What is JSON?**
   - JSON (JavaScript Object Notation) is a lightweight, text-based data format for structured data. It represents objects (key-value pairs) and arrays, and maps naturally to Python dicts/lists.

9. **How to test an API?**
   - Manually: Postman or cURL.
   - Automated: write unit/integration tests (e.g., `pytest`) using Flask’s test client; assert status codes and response bodies.
   - Additional: schema validation (OpenAPI), contract tests, and negative tests for error cases.

10. **Can we use a database instead of memory?**
    - Yes. Replace the in-memory dict with a database such as SQLite/PostgreSQL. Use an ORM (e.g., SQLAlchemy) or direct SQL. Persist users in a `users` table and implement CRUD by querying/updating the DB inside each route. Add migrations (Alembic) for schema changes.

