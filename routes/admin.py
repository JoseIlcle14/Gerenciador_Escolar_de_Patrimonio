from flask import render_template, request, Blueprint
from database.database import cadeira, mesa

admin_route = Blueprint('admin', __name__)

#////////////////funções do adiministrador////////////////#

@admin_route.route('/<item>')
def listar_itens(item):


    return render_template('lista_item.html', item = cadeira  )



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