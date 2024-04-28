
# docker rm -f $(docker ps -aq)
# docker rmi -f $(docker images -q)
# https://hub.docker.com/_/microsoft-mssql-server


# docker pull mcr.microsoft.com/mssql/server:2022-preview-ubuntu-22.04
# docker pull mcr.microsoft.com/mssql/server:2022-latest

# docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=yourStrong(!)Password" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2022-latest
# docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=yourStrong(!)Password" -e "MSSQL_PID=Evaluation" -p 1433:1433  --name sqlpreview --hostname sqlpreview -d mcr.microsoft.com/mssql/server:2022-preview-ubuntu-22.04

# precisa ter uma rede configurada para rodar o servidor
# docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=#pigmeu1234" -p 1433:1433 -d --network rede-docker mcr.microsoft.com/mssql/server:2022-latest
# docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=#pigmeu1234"-e "MSSQL_PID=Evaluation" -p 1433:1433  --name sqlpreview --hostname sqlpreview -d mcr.microsoft.com/mssql/server:2022-preview-ubuntu-22.04
# para acessar a imagem pelo terminal do outro docker
# sqlcmd -S determined_banach -U sa -P "#pigmeu1234"


