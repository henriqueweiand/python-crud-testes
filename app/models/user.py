from app import db
from app import manager


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(32), unique=True)


db.create_all()
manager.create_api(User, methods=['POST', 'GET', 'PUT', 'DELETE'])
