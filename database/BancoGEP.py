import psycopg2

conexao = psycopg2.connect(
    database = "Gerenciador_Escolar_de_Patrimonio",
    host = "aws-0-us-east-1.pooler.supabase.com",
    user = "postgres.rzejcodwpgvohhskmyqm",
    password = "gerenciador123",
    port = "6543"
)
#Nao está funcionando ainda
print(conexao.info)