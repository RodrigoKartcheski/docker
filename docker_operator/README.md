docker build . --tag docker-operator-etl:1.0

docker compose up --force-recreate -d

Cria um volume entre o container e o host
$ docker run -v /app:/home/jobs/teste_dags/pluto --name ctner hello-world

copia os arquivos do container para o host
$ docker cp ctner:/app /home/jobs/teste_dags/pluto

$ docker exec -it docker-operator-etl:1.0 sh



fonte:
https://www.restack.io/docs/airflow-knowledge-apache-docker-operator

https://forum.astronomer.io/t/cannot-connect-to-docker-daemon-when-using-dockeroperator-in-astronomer/2944

https://github.com/apache/airflow/issues/16803

solução não testada
https://github.com/jgsqware/clairctl/issues/60


Apliquei o sudo diretamente no host
sudo chmod 666 /var/run/docker.sock
https://github.com/apache/airflow/issues/16803
