## Executar
- docker-compose up --build

## Dependencias
- Instalar as bibliotecas que está no requirements.txt
Obs: As dependencias são instalar quando rodamos o docker-compose up

## Shut Down
- docker-compose down

## Arquivo de configuração
- Para flexibilizar a utilização do serviço, foi criado um arquivo de configuração que possui as caracteristicas do arquivo a ser processado.

```
{
    "file_name": "base_teste", // Nome do arquivo a ser processado.
    "file_path": "app/data",   // Caminho do arquivo a ser processado.
    "file_extension": "txt",   // Extensão do arquivo a ser processado.
    "file_headers": ["cpf", "private", "incompleto", "data_ultima_compra", "ticket_medio", "ticket_ultima_compra",
      "loja_mais_frequente", "loja_ultima_compra"] // Cabeçalhos a serem utilizados no arquivo a ser processado
}
``` 

## Testar o docker sem o docker compose
- docker images -a
- docker build -t neoway-test-app .
- docker run -it neoway-test-app ls
- docker run -it neoway-test-app python app/main.py

## Remover imagens e containers
- docker kill <container_id>
- docker rm <container_id>
- docker rmi Image neoway-test-app
- docker ps -a | awk '{ print $1,$2 }' | grep neoway-test-app | awk '{print $1 }' | xargs -I {} docker rm {}

## Para acessar o database atraves do psql
- psql -h localhost -p 5434 -U postgres -d neoway_teste

## Links úteis docker-compose e dockerfile
- https://www.youtube.com/watch?v=HxPz3eLnXZk
- https://www.youtube.com/watch?v=SR95WmOSm0c
- https://www.youtube.com/watch?v=Rv_2uvSRuwk
- https://www.youtube.com/watch?v=gHaFqYRJ_aw