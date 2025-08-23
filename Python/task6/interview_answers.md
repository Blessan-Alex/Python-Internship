## Interview Questions: Answers (Flask Templates, Jinja2, Web Forms)

1. **What is a template in Flask?**
   - A template is an HTML (or text) file with placeholders and control structures, rendered by Flask using a templating engine (Jinja2) to produce dynamic responses.

2. **What’s Jinja2?**
   - Jinja2 is Flask’s default templating engine. It supports variable interpolation (`{{ }}`), control flow (`{% %}`), filters, macros, inheritance, and autoescaping for safe HTML.

3. **How do you pass data to a template?**
   - Use `render_template('index.html', key=value, ...)`. The keyword args become template variables.

4. **How are forms handled in Flask?**
   - Create a route that accepts `GET` (to render the form) and `POST` (to handle submission). Access form fields via `request.form['field']` or `request.form.get('field')`. Validate inputs, then process (store, email, etc.).

5. **What is `render_template()`?**
   - A Flask helper that loads a template from the `templates/` directory, renders it with provided context variables, and returns an HTTP response.

6. **How to style your app?**
   - Use static CSS files placed in the `static/` directory. Reference with `{{ url_for('static', filename='styles.css') }}`. You can also include external CSS frameworks.

7. **What’s POST vs GET method in forms?**
   - GET: parameters in URL, used for retrieval; should not modify server state.
   - POST: parameters in body, used to submit data; changes server state.

8. **What are static files?**
   - Files served as-is (CSS, JavaScript, images) from the `static/` directory. Flask serves them at `/static/...`.

9. **How is routing done in Flask?**
   - Define route decorators on view functions (e.g., `@app.get('/')`, `@app.route('/contact', methods=['GET', 'POST'])`). Flask matches URL paths and HTTP methods to these functions.

10. **Can Flask serve HTML/CSS/JS?**
    - Yes. Flask renders HTML via templates and serves CSS/JS as static files from the `static/` directory.


