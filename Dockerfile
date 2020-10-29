FROM python:3.8.0-buster

#Cria um diretorio para a aplicação
WORKDIR /app

#Define as variaves de ambiente do python.
ENV PATH=$PATH:/app
ENV PYTHONPATH "${PYTHONPATH}:/app"

#Instala as dependencias do projeto
COPY requirements.txt .
RUN pip install -r requirements.txt

#Copia da pasta raiz do host para a pasta raiz do container
# "host" : "container"
COPY . .