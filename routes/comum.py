from flask import render_template, request, Blueprint

#funções do usuário comum

@comum_route.route('/itens')
def lista_itens():

    pass



@comum_route.route('/itens/<id>')
def detalhe_item():

    pass