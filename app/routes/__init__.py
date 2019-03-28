from app import app
from flask import jsonify


@app.route('/')
def index():
    return 'hello'


@app.route('/data')
def data():
    results = {
        "name": "name",
        "email": "email@email.com",
    }
    return jsonify(results)
