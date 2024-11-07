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

    global tabela_moveis
    global tabela_eletronicos

    tabela_moveis = db.session.query(Moveis).filter_by(id_objeto = itens).all()

    if tabela_moveis:

        return render_template('lista_item.html', tabela = tabela_moveis)

    else:
        
        tabela_eletronicos = db.session.query(Eletronicos).filter_by(id_objeto = itens).all()  

        return render_template('lista_item.html', tabela = tabela_eletronicos)


# visualizar os detalhes de determinado item de determinada tabela
@funcoes_route.route('/<itens>/<int:item_id>')
def detalhe_item(itens, item_id):

   pass


#////////////////funções adicionais dos administradores////////////////#

# adicionar determinado item em determinada tabela
@funcoes_route.route('/adicionar', methods = ['POST', 'GET'] )
@login_required
def adicionar_item():
    
    item_turma = request.form['turma']

    print(item_turma)
    # if tabela_moveis:

    #     item_cor = request.get['cor']
    #     item_material = request.get['material']
    #     item_novo = tabela_moveis(id = item_id, id_sala = item_turma )    

    # else: 

    #     item_potencia = request.get['potencia']
    #     item_consumo = request.get['consumo']

    

    return redirect(url_for('index'))


# remover determinado item de determinada tabela
@funcoes_route.route('/<itens>/<int:item_id>/deletar', methods = ['DELETE'])
@login_required
def deletar_item( itens,item_id):

    pass


# editar determinado item de determinada tabela
@funcoes_route.route('/<itens>/<int:item_id>/editar', methods = ['PUT'])
@login_required
def editar_item(itens, item_id):

    item_editado = None
    data = request.json

    for c in itens:
        if c['id'] == item_id:
            c['cor'] = data['cor']
            c['local'] = data['local']
            c['material'] = data['material']

            item_editado = c

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