from app import app
from flask import render_template

@app.route("/admin/auth")
def admin_auth():
    return render_template("auth.html")