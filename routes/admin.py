from flask import render_template, request, Blueprint
from database.database import CADEIRA, MESA, moveis

admin_route = Blueprint('admin', __name__)

#////////////////funções do adiministrador////////////////#

@admin_route.route('/<item>')
def listar_itens(item):

    for i in moveis:
        if item == moveis[i]:
            item = moveis[i]

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