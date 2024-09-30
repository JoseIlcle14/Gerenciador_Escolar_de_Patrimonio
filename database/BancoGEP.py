import psycopg2

conexao = psycopg2.connect(
    database = "gepdb",
    host = "aws-0-us-east-1.pooler.supabase.com",
    user = "postgres.rzejcodwpgvohhskmyqm",
    password = "gerenciador123",
    port = "6543"
)
