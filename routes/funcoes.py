from flask import render_template, request, Blueprint, redirect, url_for,session
from models import Usuarios,Moveis, Eletronicos
from database.db import db
from flask_login import login_user, login_required
import jsonpickle

funcoes_route = Blueprint('funcoes', __name__)

#////////////////funções dos usuários////////////////#

# carregar a página sobre nós
@funcoes_route.route('/sobre')
def sobre():
    
    return render_template('sobre.html')

tabela_moveis = []
# visualizar os objetos de determinada tabela
@funcoes_route.route('/<int:itens>')
def listar_itens(itens):
    session['id_obj'] = itens
    
    global tabela_moveis
    tabela_moveis = db.session.query(Moveis).filter_by(id_objeto = itens).all()
    
    if tabela_moveis:
        
        mov = True
        session['tabela'] = jsonpickle.encode(tabela_moveis)

        return render_template('lista_item.html', tabela = tabela_moveis, movel = mov)

    else:
        
        mov = False
        tabela_eletronicos = db.session.query(Eletronicos).filter_by(id_objeto = itens).all() 

        return render_template('lista_item.html', tabela = tabela_eletronicos, movel = mov)


# visualizar os detalhes de determinado item de determinada tabela
@funcoes_route.route('/<int:item_id>/detalhe')
def detalhe_item(item_id):

    pass


#////////////////funções adicionais dos administradores////////////////#

# adicionar determinado item em determinada tabela
@login_required
@funcoes_route.route('/adicionar', methods = ['POST'] )
def adicionar_item():
    item_tipo = session.get('id_obj')    
    item_turma = request.form['turma']
    
    if tabela_moveis:

        item_cor = request.form['cor']
        item_material = request.form['material']
        id_novo = request.form['id']        

        item_novo = Moveis(id = id_novo, id_sala = item_turma, material = item_material, cor = item_cor, id_objeto = item_tipo )    
        
        db.session.add(item_novo)
        db.session.commit()
        
        return redirect(f'{item_tipo}')

    else: 

        item_potencia = request.form['potencia']
        item_consumo = request.form['consumo']
        id_novo = request.form['id']

        item_novo = Eletronicos(id = id_novo, id_sala = item_turma, potencia = item_potencia, consumo = item_consumo, id_objeto = item_tipo )

        db.session.add(item_novo)
        db.session.commit()

        return redirect(f'{item_tipo}')


# remover determinado item de determinada tabela
@funcoes_route.route('/<int:item_id>/Deletar')
def deletar_item(item_id):
    id_obj = session.get('id_obj')
        
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
@funcoes_route.route('/<int:item_id>/editar>', methods = ['POST'])
def editar_item(item_id):
    id_obj = session.get('id_obj')
    print(item_id)

    if tabela_moveis:
        
        item =  db.session.query(Moveis).filter_by(id=item_id).first()
        item.id_sala = request.form['turma']    
        item.material = request.form['material']
        item.cor = request.form['cor']
        
        return redirect(f'{id_obj}')
    else:

        item = db.session.query(Eletronicos).filter_by(id=item_id).first()

        # item.id_sala = request.form['turma']    
        # item.potencia = request.form['potencia']
        # item.consumo = request.form['consumo']

        # db.session.commit()
        
    return redirect(f'/{id_obj}')

#////////////////login////////////////#

@funcoes_route.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':

        return render_template('entrar.html')
    
    elif request.method == 'POST':

        login = request.form['login']
        senha = request.form['senha']

        user = db.session.query(Usuarios).filter_by(login = login, senha = senha).first()

        if not user:
            menssagem = True
            return render_template('entrar.html', menssagem = menssagem)
        
        login_user(user)
        return redirect(url_for('index'))     