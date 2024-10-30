from flask import Flask, render_template
from routes.funcoes import funcoes_route
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

app.register_blueprint(funcoes_route)

@app.route('/')
def index():
    #apagar uma tabela
    #Moveis.__table__.drop(db.engine)
    #print("Tabela Objetos deletada com sucesso!")
    
    j = int('060201')
    sala = int('02')
    obj = int('06')
    for i in range(1):
        nc = Eletronicos(id = j, id_sala= sala, id_objeto= obj, potencia = '0.26', consumo = '2.6')
        j += 1
        db.session.add(nc)
    db.session.commit()
   
    
    #apagar uma linha
    # id = 40301
    # apagar = Eletronicos.query.get(id)

    # if apagar:
    #     db.session.delete(apagar)
    #     db.session.commit()
    #     print('linha apagada')
    # else:
    #     print('n deu crt')
    
    #update na tabela
    # id = 40101
    # for i in range(2):
    #     objeto = Eletronicos.query.get(id)
    #     novo_idsala = 1
    #     if objeto:
    #         objeto.id_sala = novo_idsala
    #         db.session.commit()
    #         print('deu crt')
    #     else:
    #         print('n deu crt')
    #     id += 1

    
    
    return render_template('index.html')

   
    
#criando o banco de dados
with app.app_context():
    db.create_all()
app.run(debug=True)