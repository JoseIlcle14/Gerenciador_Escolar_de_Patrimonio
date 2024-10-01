from flask import render_template, request, Blueprint

comum_route = Blueprint('comum',__name__)

#funções do usuário comum

@comum_route.route('/sobre')
def sobre():
    return render_template('sobre.html')


@comum_route.route('/itens')
def lista_itens():

    pass



@comum_route.route('/itens/<id>')
def detalhe_item():

    pass