from flask import render_template, request, Blueprint, redirect, url_for
from database.database import CADEIRA, MESA, moveis
from database.usuarios import USUARIOS

admin_route = Blueprint('admin', __name__)

#////////////////funções do adiministrador////////////////#

@admin_route.route('/<item>')
def listar_itens(item):

    tabela = [CADEIRA,MESA]
    for i in tabela:
        palavra = str(tabela)
        print(palavra[tabela])

    for objeto in palavra:
        if item == palavra[objeto]:
            item = tabela[objeto]

    return render_template('lista_item.html', item = item  )



@admin_route.route('/item/<id>')
def detalhe_item():



    pass            


@admin_route.route('/adicionar', methods = ['POST'] )
def form_adicionar_item():



    pass



@admin_route.route('/<id>/deletar', methods = ['DELETE'])
def deletar_item(id):

    pass



@admin_route.route('/<id>/editar', methods = ['PUT'])
def editar_item(id):

    pass
#rota para cadastrar Usuário
@admin_route.route('/cadastrar', methods = ['GET','POST'])
def registrar_admin():

    #se a requisição for GET apenas manda a página
    if request.method == "GET":

        return render_template('registrar.html')
    
    #se ele mandar algo no formulário ele envia para o DB USUÁRIOS
    elif request.method == "POST":
        login = request.form['login']
        senha = request.form['senha']
        USUARIOS.append({'login': login, 'senha': senha})
        
        #redireciona para a página inicial
        return redirect(url_for('index'))