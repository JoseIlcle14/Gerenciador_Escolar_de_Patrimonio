from flask import Flask, render_template
from routes.admin import admin_route
from routes.comum import comum_route
from models import Usuarios, Objetos,Moveis,Eletronicos
from flask_sqlalchemy import SQLAlchemy
from database.db import db
from flask_login import LoginManager

app = Flask(__name__)

#chave de segurança do projeto
app.secret_key = '12345678'
lm = LoginManager(app)
lm.login_view = 'login'

#cirando conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db.init_app(app)   

@lm.user_loader
def user_loader(id):
    usuario = db.session.query(Usuarios).filter_by(id=id).first()
    
    return usuario

app.register_blueprint(admin_route, url_prefix = '/lista')

app.register_blueprint(comum_route, url_prefix = '/comum')

@app.route('/')
def index():
    #apagar uma tabela
    #Moveis.__table__.drop(db.engine)
    #print("Tabela Objetos deletada com sucesso!")
    
    j = int('050201')
    sala = int('02')
    obj = int('05')
    for i in range(3):
        nc = Eletronicos(id = j, id_sala= sala, id_objeto= obj, potencia = '0.113', consumo = '3.4')
        j += 1
        db.session.add(nc)
        

    db.session.commit()
   
    
    """
    #apagar uma linha
    id = 20346
    apagar = Moveis.query.get(id)

    if apagar:
        db.session.delete(apagar)
        db.session.commit()
        print('linha apagada')
    else:
        print('n deu crt')
    """





    
    
    return render_template('index.html')

   
    
#criando o banco de dados
with app.app_context():
    db.create_all()
app.run(debug=True)