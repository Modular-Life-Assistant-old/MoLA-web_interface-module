from flask import Blueprint, redirect, url_for, render_template

app = Blueprint('home', __name__)

@app.route('/static/<path:filename>')
def send_foo(filename):
    return send_from_directory(
        os.path.dirname(os.path.abspath(__file__)) + '/../static/',
        filename
    )
