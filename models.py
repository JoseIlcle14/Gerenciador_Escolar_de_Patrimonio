from database.db import db

class Usuarios(db.Model):
    __tablename__ = "USUARIOS"

    login = db.Column(db.String(20), unique = True, primary_key = True)

    senha = db.Column(db.String(10)) 

