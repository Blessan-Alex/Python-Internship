## Task 6: Portfolio Website with Flask

A minimal personal portfolio built with Flask, templates (Jinja2), and basic styling.

### Features
- Home page with name, role, and sample projects
- Contact page with a form and basic validation
- Simple `/health` endpoint

### Setup (Windows PowerShell)
```powershell
cd task6
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5001`.

### Structure
- `app.py` – Flask app and routes
- `templates/` – `index.html`, `contact.html`, `thankyou.html`
- `static/` – `styles.css`

### Notes
- Submissions are stored in memory; restart clears them. For real apps, persist to a DB or send email.


