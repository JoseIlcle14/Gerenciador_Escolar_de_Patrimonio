from sqlalchemy import ForeignKey
from database.db import db
from flask_login import UserMixin

class Usuarios(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key = True)

    login = db.Column(db.String(20), unique = True)

    senha = db.Column(db.String(10))

class Objetos(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))

class Sala(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(30))

class Moveis(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    material = db.Column(db.Integer, )
    id_sala = db.Column(db.Integer, ForeignKey('Sala.id'))