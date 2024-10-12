import mysql.connector
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='ilcle',
    database = 'gepdb',
)

cursor = conexao.cursor()

inserir_objetos()

#cursor.execute(comando)
#conexao.commit()
    
#resultado = cursor.fetchall() #lê o banco de dados
cursor.close()
conexao.close()