import psycopg2

# Par  metros de conex  o com o PostgreSQL
db_host = 'meu-postgres'  # Ou use o endere  o IP se preferir
db_port = '5432'
db_name = 'postgres'
db_user = 'postgres'
db_password = 'postgres'  # Substitua pela sua senha

try:
    # Conectando ao PostgreSQL
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )

    # Criando um cursor
    cursor = connection.cursor()

    # Executando uma consulta de exemplo
    cursor.execute("SELECT version();")

    # Obtendo os resultados
    version = cursor.fetchone()[0]
    print(f"Vers  o do PostgreSQL: {version}")

except Exception as e:
    print(f"Erro ao conectar ao PostgreSQL: {e}")

finally:
    # Fechando a conex  o e o cursor
    if connection:
        cursor.close()
        connection.close()
        print("Conex  o fechada com o PostgreSQL")

