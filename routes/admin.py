from flask import render_template, request, Blueprint

#funções do usuário administrador

@admin_route.route('/itens')
def lista_itens():

    pass




@admin_route.route('/itens/<id>')
def detalhe_item():

    pass



@admin_route.route('/itens/adicionar', methods = ['POST'] )
def form_adicionar_item():

    pass



@admin_route.route('itens/<id>/deletar', methods = ['DELETE'])
def deletar_item(id):

    pass



@admin_route.route('/itens/<id>/editar', methods = ['PUT'])
def editar_item(id):

    pass



