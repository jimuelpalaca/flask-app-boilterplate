from App import app
from flask import render_template


@app.route('/auth/login')
def login():
    return render_template('auth/login.html')