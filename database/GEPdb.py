import mysql.connector
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='ilcle',
    database = 'gepdb',
)

cursor = conexao.cursor()
comando = f'insert into usuarios (login,senha,tipo) values("joseilcle@gmail.com","jujustsu","Comum")'
cursor.execute(comando)
conexao.commit()





cursor.close()
conexao.close()