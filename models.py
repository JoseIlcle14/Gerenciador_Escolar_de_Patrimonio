from database.db import db
from flask_login import UserMixin

class Usuarios(UserMixin, db.Model):
    __tablename__ = "USUARIOS"

    id = db.Column(db.Integer, primary_key = True, not_null = True)

    login = db.Column(db.String(20), unique = True)

    senha = db.Column(db.String(10)) 

