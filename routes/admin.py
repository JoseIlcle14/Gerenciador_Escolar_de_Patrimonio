from flask import render_template, request, Blueprint, redirect, url_for
from database.database import CADEIRA, MESA, AR, VENTILADOR, PROJETOR, LOUSA
from models import Usuarios
from database.db import db
from flask_login import login_user, login_required

admin_route = Blueprint('admin', __name__)

#////////////////funções do adiministrador////////////////#

def encontrar_tabela(itens):

    match itens:

        case 'CADEIRA':
            itens = CADEIRA
            

        case 'MESA':
            itens = MESA
            

        case 'AR':
            itens = AR
            

        case 'VENTILADOR':
            itens = VENTILADOR
            

        case 'PROJETOR':
            itens = PROJETOR 
            

        case 'LOUSA':
            itens = LOUSA

    return itens

@admin_route.route('/<itens>')
def listar_itens(itens):

    tabela = encontrar_tabela(itens)

    return render_template('lista_item.html', tabela = tabela)




@admin_route.route('/itens/')
def detalhe_item():

    

    return render_template('detalhe_item.html')



@admin_route.route('/<itens>/adicionar', methods = ['POST'] )
@login_required
def adicionar_item(itens):

    data = request.json

    novo_item = {
        "id": len(itens) + 1,
        "cor": data['cor'],
        "local": data['local'],
        "material": data['material']
    }

    itens.append(novo_item)

    return render_template('item_unidade.html', novo_item = novo_item)



@admin_route.route('/<itens>/<int:item_id>/deletar', methods = ['DELETE'])
@login_required
def deletar_item( itens,item_id):

    global CLIENTES
    itens = [ c for c in itens if c['id'] != item_id  ]

    return {'deleted': 'ok'}



@admin_route.route('/<itens>/<int:item_id>/editar', methods = ['PUT'])
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

    return render_template('item_unidade.html', item_editado = item_editado)
    

@admin_route.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':

        return url_for('index')
    
    elif request.method == 'POST':

        login = request.form('login')
        senha = request.form('senha')

        user = db.session.query(Usuarios).filter_by(login = login, senha = senha).first()

        if not user:
            return 'Você não tem um login'
        
        login_user(user)
        return redirect(url_for('index'))

#rota para cadastrar Usuário
@admin_route.route('/cadastrar', methods = ['GET','POST'])
def registrar_admin():

    #se a requisição for GET apenas manda a página
    if request.method == "GET":

        return render_template('registrar.html')
    elif request.method == 'POST':

        login = request.form['login']
        senha = request.form['senha']

        novo_usuário = Usuarios(login=login, senha=senha)
        db.session.add(novo_usuário)
        db.session.commit()

        login_user(novo_usuário)

        return redirect(url_for('index'))      
  