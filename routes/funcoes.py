from flask import render_template, request, Blueprint, redirect, url_for
from models import Usuarios, Objetos, Moveis, Eletronicos
from database.db import db
from flask_login import login_user, login_required

funcoes_route = Blueprint('funcoes', __name__)

#////////////////funções dos usuários////////////////#

# carregar a página sobre nós
@funcoes_route.route('/sobre')
def sobre():
    
    return render_template('sobre.html')


# visualizar os objetos de determinada tabela
@funcoes_route.route('/<int:itens>')
def listar_itens(itens):
    global id_obj
    id_obj = itens
    global tabela_moveis
    global tabela_eletronicos

    tabela_moveis = db.session.query(Moveis).filter_by(id_objeto = itens).all()

    if tabela_moveis:

        return render_template('lista_item.html', tabela = tabela_moveis)

    else:
        
        tabela_eletronicos = db.session.query(Eletronicos).filter_by(id_objeto = itens).all()  

        return render_template('lista_item.html', tabela = tabela_eletronicos)


# visualizar os detalhes de determinado item de determinada tabela
@funcoes_route.route('/<int:item_id>/detalhe')
def detalhe_item(item_id):

   pass


#////////////////funções adicionais dos administradores////////////////#

# adicionar determinado item em determinada tabela
@login_required
@funcoes_route.route('/adicionar', methods = ['POST'] )
def adicionar_item():
    item_tipo = id_obj
    item_turma = request.form['turma']

    if tabela_moveis:

        item_cor = request.form['cor']
        item_material = request.form['material']
        
        ultimo_id = db.session.query(Moveis).with_entities(Moveis.id).filter_by(id_sala = item_turma, id_objeto = item_tipo).order_by(Moveis.id.desc()).first()

        id_novo = (ultimo_id[0] + 1)

        item_novo = Moveis(id = id_novo, id_sala = item_turma, material = item_material, cor = item_cor, id_objeto = item_tipo )    
        
        db.session.add(item_novo)
        db.session.commit()
        
        return redirect(f'{item_tipo}')

    else: 

        item_potencia = request.form['potencia']
        item_consumo = request.form['consumo']

        ultimo_id = db.session.query(Eletronicos).with_entities(Eletronicos.id).filter_by(id_sala = item_turma, id_objeto = item_tipo).order_by(Eletronicos.id.desc()).first()

        id_novo = (ultimo_id[0] + 1)

        item_novo = Eletronicos(id = id_novo, id_sala = item_turma, potencia = item_potencia, consumo = item_consumo, id_objeto = item_tipo )

        db.session.add(item_novo)
        db.session.commit()

        return redirect(f'{item_tipo}')


# remover determinado item de determinada tabela
@login_required
@funcoes_route.route('/<int:item_id>/Deletar')
def deletar_item(item_id):
    if tabela_moveis:

        objeto_del = db.session.query(Moveis).filter_by(id = item_id).first()

        db.session.delete(objeto_del)
        db.session.commit()
        
        return redirect(f'/{id_obj}')

    else:
        objeto_del = db.session.query(Eletronicos).filter_by(id = item_id).first()
        db.session.delete(objeto_del)
        db.session.commit()

        return redirect(f'/{id_obj}')


# editar determinado item de determinada tabela
@login_required
@funcoes_route.route('/<int:item_id>/editar', methods = ['PUT'])
def editar_item(item_id):
    pass    
    
#////////////////login////////////////#

@funcoes_route.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':

        return render_template('registrar.html')
    
    elif request.method == 'POST':

        login = request.form('login')
        senha = request.form('senha')

        user = db.session.query(Usuarios).filter_by(login = login, senha = senha).first()

        if not user:
            return 'Você não tem um login'
        
        login_user(user)
        return redirect(url_for('index'))     