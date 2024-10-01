from flask import Flask, render_template
from routes.admin import admin_route
from routes.comum import comum_route
from models import Usuarios
from flask_sqlalchemy import SQLAlchemy
from database.db import db

app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db.init_app(app)   

app.register_blueprint(admin_route, url_prefix = '/lista')

app.register_blueprint(comum_route, url_prefix = '/comum')

@app.route('/')
def index():

    return render_template('index.html')

with app.app_context():
    db.create_all()
app.run(debug=True)