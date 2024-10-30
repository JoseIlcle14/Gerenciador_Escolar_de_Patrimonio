from flask import render_template, request, Blueprint, redirect, url_for
from models import Usuarios, Objetos, Moveis, Eletronicos
from database.db import db
from flask_login import login_user, login_required

funcoes_route = Blueprint('funcoes', __name__)

#////////////////funções do adiministrador////////////////#

@funcoes_route.route('/sobre')
def sobre():
    
    return render_template('sobre.html')



@funcoes_route.route('/<int:lista>/<int:itens>')
def listar_itens(lista, itens):

    tabela = db.session.query(Moveis).filter_by(id_objeto = itens).all()

    if not tabela:

        tabela = db.session.query(Eletronicos).filter_by(id_objeto = itens).all()    
    
    lista = lista

    return render_template('lista_item.html', itens = tabela, lista = lista)



@funcoes_route.route('/<itens>/<int:item_id>')
def detalhe_item(itens, item_id):

   pass



@funcoes_route.route('/<itens>/adicionar', methods = ['POST'] )
@login_required
def adicionar_item(itens):

    pass



@funcoes_route.route('/<itens>/<int:item_id>/deletar', methods = ['DELETE'])
@login_required
def deletar_item( itens,item_id):

    pass



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
    

@funcoes_route.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':

        return render_template("registrar.html")
    
    elif request.method == 'POST':

        login = request.form('login')
        senha = request.form('senha')

        user = db.session.query(Usuarios).filter_by(login = login, senha = senha).first()

        if not user:
            return 'Você não tem um login'
        
        login_user(user)
        return redirect(url_for('index'))

       