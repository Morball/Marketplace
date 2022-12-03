from flask import render_template
from app import app


@app.errorhandler(404)
def not_found(self):
    return render_template("errors/404.html")

@app.errorhandler(500)
def internal_error(self):
    return render_template("errors/500.html")

