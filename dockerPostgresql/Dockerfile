#! Dockerfile
# docker build . -t postgresql:1.0

# Use a imagem base do Ubuntu
FROM ubuntu:latest

# Atualize o repositório de pacotes e instale o BASH, Python 3, iputils-ping, cliente PostgreSQL (psql) e Python3 pip
RUN apt-get update && \
    apt-get install -y bash python3 iputils-ping postgresql-client python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Crie e ative um ambiente virtual Python
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instale o módulo psycopg2 usando pip dentro do ambiente virtual
RUN pip install psycopg2-binary

# Copie um script SQL de teste para o contêiner (opcional)
COPY test_postgresql_connection.py /root/

# Comando padrão a ser executado quando o contêiner for iniciado
CMD ["/bin/bash"]

