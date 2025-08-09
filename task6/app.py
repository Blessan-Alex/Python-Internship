from __future__ import annotations

from typing import Any, Dict, Optional

from flask import Flask, render_template, request, redirect, url_for, flash


def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.secret_key = "dev-secret-key"  # Needed for flash messages

    # Simple in-memory store for contact submissions
    submissions: list[Dict[str, str]] = []

    @app.get("/")
    def index() -> Any:
        # Example dynamic data passed to template
        projects = [
            {"title": "Flask API", "description": "REST API with CRUD"},
            {"title": "Data Analysis", "description": "Pandas + charts"},
            {"title": "Portfolio", "description": "This site"},
        ]
        return render_template("index.html", name="Your Name", role="Software Developer", projects=projects)

    @app.route("/contact", methods=["GET", "POST"])
    def contact() -> Any:
        if request.method == "GET":
            return render_template("contact.html")

        # POST
        name: Optional[str] = request.form.get("name")
        email: Optional[str] = request.form.get("email")
        message: Optional[str] = request.form.get("message")

        errors: Dict[str, str] = {}
        if not name or not name.strip():
            errors["name"] = "Name is required"
        if not email or not email.strip():
            errors["email"] = "Email is required"
        if not message or not message.strip():
            errors["message"] = "Message is required"

        if errors:
            for msg in errors.values():
                flash(msg, "error")
            # Re-render the form with previously entered values
            return render_template("contact.html", form={"name": name or "", "email": email or "", "message": message or ""}), 400

        submissions.append({"name": name.strip(), "email": email.strip(), "message": message.strip()})
        return render_template("thankyou.html", name=name.strip())

    @app.get("/health")
    def health() -> Any:
        return {"ok": True}, 200

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)


