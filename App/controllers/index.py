from App import app
from flask import redirect, url_for


@app.route('/')
def index():
    return redirect(url_for('login'))
