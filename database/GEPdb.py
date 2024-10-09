import mysql.connector
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='ilcle',
    database = 'gepdb',
)

cursor = conexao.cursor()


def inserir_objetos():
    objeto = input("Informe o objeto de inserção: ")
    local = int(input("diga o numero da sala: "))
    id = 33101
    if objeto == 'cadeira' or objeto == 'mesa' and local == 1 :
        for i in range (46):
            comando = f'insert into {objeto}(id,cor,material,idsala) values({id},"azul","ferro e plástico",{local})'
            id += 1

inserir_objetos()
#resultado = cursor.fetchall() #lê o banco de dados
cursor.close()
conexao.close()