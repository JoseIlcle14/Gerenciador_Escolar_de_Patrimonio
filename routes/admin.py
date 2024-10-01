from flask import render_template, request, Blueprint, redirect, url_for
from database.database import CADEIRA, MESA, AR, VENTILADOR, PROJETOR, LOUSA
from models import Usuarios
from database.db import db

admin_route = Blueprint('admin', __name__)

#////////////////funções do adiministrador////////////////#

@admin_route.route('/<itens>')
def listar_itens(itens):

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

    
    return render_template('lista_item.html', tabela = itens)




@admin_route.route('/<itens>/<int:item_id>')
def detalhe_item(itens, item_id):

    objeto = list(filter(lambda c: c['id'] == item_id, itens))[0]

    return render_template('detalhe_item.html', item = objeto)



@admin_route.route('/<itens>/adicionar', methods = ['POST'] )
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
def deletar_item( itens,item_id):

    global CLIENTES
    itens = [ c for c in itens if c['id'] != item_id  ]

    return {'deleted': 'ok'}



@admin_route.route('/<itens>/<int:item_id>/editar', methods = ['PUT'])
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

        return redirect('index')        