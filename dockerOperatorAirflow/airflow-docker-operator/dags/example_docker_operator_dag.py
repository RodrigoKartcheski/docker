from datetime import datetime
import uuid

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

def generate_container_name():
    unique_id = uuid.uuid4().hex[:10]  # Usar os primeiros 10 caracteres do UUID para o nome
    return f"example-DURACELL-docker-operator-dag__print_message__{unique_id}"
    
# Criar o objeto Mount para montar o volume
volume_mount = Mount(type="bind", source="/home/jobs/docker-airflow-operator/src", target="/app/src")

    
with DAG(
    dag_id="example-docker-operator-dag",
    schedule_interval=None,
    start_date=datetime(2022, 7, 24),
) as dag:

    message_task = DockerOperator(
        task_id="print_message",
        api_version="auto",
        docker_url="unix://var/run/docker.sock",
        auto_remove=False,
        network_mode='bridge',
        image="docker-operator-etl:1.0",
        mounts=[volume_mount],  # Lista de volumes a serem montados no contêiner
        command="python src/task.py",
        #container_name="{{ task_instance_key_str }}",
        container_name=generate_container_name(),  # Usar o nome gerado dinamicamente
        user="airflow",
        mount_tmp_dir=False,
        force_pull=False,
    )


if __name__ == "__main__":
    dag.cli()
    
    
    
