from app import app
from flask import jsonify, request
import requests
import json
import jwt

@app.route('/')
def index():
    return 'hello'



@app.route("/getToken")
def generate():
    encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')

    return encoded


@app.route("/checkToken")
def check():
    encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')

    return encoded


@app.route('/sales', methods=['POST'])
def sales():
    data = request.form
    payload = {
        "id": 0,
        "datetime": "string",
        "storeId": "string",
        "posId": "string",
        "partnerReference": "string",
        # "customer": data['customer'],  # array
        # "items": data['items'],  # array
        "subtotal": 0,
        "discount": 0,
        "addition": 0,
        "total": 0,
        # "payments": data['payments'],  # array
    }
    # r = requests.post("https://ene66npcfay49.x.pipedream.net", data=payload)
    return json.dumps(data)
