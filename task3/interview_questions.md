# Interview Questions: Task 3

1. **What is Flask?**
   - Flask is a lightweight Python web framework used to build web applications and APIs. It is known for its simplicity and flexibility.

2. **What is REST?**
   - REST (Representational State Transfer) is an architectural style for designing networked applications. It uses HTTP methods to perform CRUD operations on resources, typically represented in JSON or XML.

3. **Difference between GET and POST?**
   - GET is used to retrieve data from a server, while POST is used to send data to the server to create or update resources. GET requests are idempotent and do not change server state; POST requests can change server state.

4. **How does a Flask route work?**
   - A Flask route maps a URL path to a Python function (view). When a request matches the route, Flask calls the associated function to handle the request and return a response.

5. **What is request.json?**
   - `request.json` is a Flask property that parses and returns the JSON data sent in the body of a request, typically used with POST and PUT methods.

6. **What are status codes like 200, 404?**
   - Status codes are part of HTTP responses. 200 means success, 404 means resource not found, 201 means created, 400 means bad request, etc.

7. **How do you run a Flask app?**
   - Save your Flask app in a Python file (e.g., app.py) and run `python app.py`. The app will start a local server, usually at http://127.0.0.1:5000/.

8. **What is JSON?**
   - JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.

9. **How to test an API?**
   - You can test an API using tools like Postman or curl to send HTTP requests and inspect responses. Automated tests can also be written in code.

10. **Can we use a database instead of memory?**
    - Yes, you can use a database (like SQLite, PostgreSQL, or MongoDB) to persist data instead of storing it in memory. This allows data to persist across server restarts and supports larger datasets.

**Key Concepts:** REST, HTTP Methods, Flask