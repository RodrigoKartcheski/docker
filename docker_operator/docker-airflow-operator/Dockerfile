#! Dockerfile

FROM python:3.9

USER root

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src src

# Definir usuário airflow
RUN useradd -ms /bin/bash airflow

# Alterar permissões do arquivo task.py
RUN chmod +x src #/task.py

# Alterar proprietário do arquivo task.py para o usuário airflow
RUN chown airflow:airflow src #/task.py

USER airflow
