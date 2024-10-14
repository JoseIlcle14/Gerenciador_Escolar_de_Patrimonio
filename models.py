from database.db import db
from flask_login import UserMixin

class Usuarios(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key = True)

    login = db.Column(db.String(20), unique = True)

    senha = db.Column(db.String(10))

class Cadeira(db.Model):

    id = db.Column(db.Integer, primary_key = True)

    cor = db.Column(db.String(50))

    material = db.Column(db.String(50))