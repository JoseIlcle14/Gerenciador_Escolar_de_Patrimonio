from flask import Flask, render_template, session   
from routes.funcoes import funcoes_route
from models import Usuarios
from database.db import db
from flask_login import LoginManager

app = Flask(__name__)

#chave de segurança do projeto
app.secret_key = '12345678'
lm = LoginManager(app)
lm.login_view = 'funcoes.login'

#cirando conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db.init_app(app)   

usuario = None

@lm.user_loader
def user_loader(id):
    global usuario
    
    usuario = db.session.query(Usuarios).filter_by(id=id).first()
    
    return usuario

app.register_blueprint(funcoes_route)

@app.route('/')
def index():
    usu = session.get('usu')

    return render_template('index.html', usu = usu)

   
    
#criando o banco de dados
with app.app_context():
    db.create_all()
app.run(host='0.0.0.0',debug=True)