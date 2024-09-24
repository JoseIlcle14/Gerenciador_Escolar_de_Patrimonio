import mysql.connector
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='ilcle',
    database = 'gepdb',
)

cursor = conexao.cursor()


def inserir_usuarios():
    login = "jorge.silva@gmail.com"
    senha = "40028922"
    tipo = "Administrador"
    comando = f'insert into usuarios (login,senha,tipo) values("{login}","{senha}","{tipo}")'
    cursor.execute(comando)
    conexao.commit()
def inserir_moveis():
    # id,nome,cor,material,sala
    nome = input("informe seu obejeto: ")
    cor = input("informe a cor: ")
    material = input("informe o material: ")
    sala = input("informe sua localização: ")
    comando = f'insert into moveis (nome,cor,material,sala) values("{nome}","{cor}","{material}","{sala}")'
    cursor.execute(comando)
    conexao.commit()
    

def inserir_eletronicos():
    nome = input("informe seu obejeto: ")
    consumoEnergia = int(input("Informe o consumo desse aparelho: "))
    comando = f'insert into eletronicos (nome,consumoEnergia) values("{nome}","{consumoEnergia}")'
    cursor.execute(comando)
    conexao.commit()

def inserir_objetos():
    comp = input("Você deseja inserir um movel(m) ou um eletrônico(e)?")
    if comp == 'm':
        inserir_moveis()
    if comp == 'e':
        inserir_eletronicos()


inserir_usuarios()
inserir_objetos()


#resultado = cursor.fetchall() #lê o banco de dados
cursor.close()
conexao.close()