---
title: Dockerização do sistema
sidebar_position: 1
description : Introdução ao Docker
---

# Introdução

Docker é uma plataforma de código aberto que permite automatizar a implantação, o dimensionamento e a gestão de aplicações em contêiner. Os contêineres são unidades padronizadas de software que empacotam código e todas as suas dependências, de modo que a aplicação possa ser executada de forma rápida e confiável em qualquer ambiente.

No nosso caso, utilizamos o Docker para facilitar a execução do sistema em diferentes ambientes, garantindo que todas as dependências estejam corretamente instaladas e configuradas. Dividimos o sistema em dois contêineres: um para o backend e outro para o frontend. Cada contêiner possui sua própria imagem, que contém todas as dependências necessárias para a execução da aplicação.

## Docker Backend

O Dockerfile do backend é responsável por criar a imagem do contêiner do backend. Neste arquivo, são definidas as instruções para a criação da imagem, como a instalação das dependências, a cópia dos arquivos necessários e a definição do comando de inicialização do backend.

```dockerfile
FROM python:3.12

# Diretorio de trabalho do containeir
WORKDIR /code

# Copiar os requirements pra dentro do container
COPY ./requirements.txt /code/requirements.txt

# Instalar as dependências
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copiar todo conteudo para dentro do code
COPY . /code

# Porta que vai rodar a aplicação
EXPOSE 8000

# Rodar aplicação
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

```

Sumarizando um pouco o que foi feito no Dockerfile:

- Utilizamos a imagem oficial do Python 3.12 como base.
- Definimos o diretório de trabalho como `/code`.
- Copiamos o arquivo `requirements.txt` para o diretório `/code` e instalamos as dependências.
- Copiamos todos os arquivos do diretório atual para o diretório `/code` dentro do contêiner.
- Expondo a porta 8000, que é a porta em que o FastAPI irá rodar.
- Rodamos o comando `uvicorn app:app --host

Para rodar o cotainer do backend, deve-se rodar o seguinte comando:

```bash

docker build -t backend-kafer .

docker run -d -p 8000:80 backend-kafer

```

Assim pode ser acesso as rotas do backend em `http://localhost:8000/docs`.

## Docker Frontend

O Dockerfile do frontend é responsável por criar a imagem do contêiner do frontend. Para facilitar o deploy da aplicação no futuro e segurança utilizando o Nginx como servidor web.

```dockerfile
FROM node:16-alpine AS build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# Nginx para servir os arquivos estáticos
FROM nginx:alpine

# Copiar os arquivos de configuração customizado do Nginx
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# Copia os arquivos do build para o diretório do Nginx
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 88
CMD ["nginx", "-g", "daemon off;"]

```

Sumarizando um pouco o que foi feito no Dockerfile:

- Utilizamos a imagem oficial do Node 16-alpine como base para o build.
- Definimos o diretório de trabalho como `/app`.
- Copiamos os arquivos `package.json` e `package-lock.json` para o diretório `/app` e instalamos as dependências.
- Copiamos todos os arquivos do diretório atual para o diretório `/app` dentro do contêiner.
- Rodamos o comando `npm run build` para gerar os arquivos estáticos da aplicação.
- Utilizamos a imagem oficial do Nginx como base para o contêiner final.
- Copiamos o arquivo de configuração customizado do Nginx para o diretório `/etc/nginx/conf.d/default.conf`.
- Copiamos os arquivos do build para o diretório `/usr/share/nginx/html` dentro do contêiner.
- Expondo a porta 88, que é a porta em que o Nginx irá rodar.
- Rodamos o comando `nginx -g daemon off;` para iniciar o servidor Nginx.

Para rodar o cotainer do frontend, deve-se rodar o seguinte comando:

```bash

docker build -t frontend-kafer .

docker run -d -p 3000:80 frontend-kafer
```

Assim pode ser acesso a aplicação em `http://localhost:3000`.

## Docker Compose

Para conseguir rodar os dois containers juntos, utilizamos o Docker Compose. O arquivo `docker-compose.yml` é responsável por definir a configuração dos contêineres e a rede que será utilizada para a comunicação entre eles. Além disso, atraves dele estavamos fazendo o heatlh check dos containers que está detalhado no [Health Check](../HealthCheck/healthCheck.md).

```yaml
version: "3.8"

services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "8000:80"
    volumes:
      - ./backend:/code
    depends_on:
      - frontend
    networks:
      - app-network
    # Healthcheck para verificar a saude do container -> fica tentando enquanto o container estiver rodando
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/api/healthcheck/health"]
      interval: 30s # Tempo entre os testes
      timeout: 10s # Tempo para o teste falhar
      retries: 3  # Numero de tentativas
      start_period: 60s # Tempo pra começar testar o status
  frontend:
    build:
      context: ./app-typescript
      dockerfile: Dockerfile
    ports:
      - "3000:80"
    volumes:
      - ./app-typescript:/app
    networks:
      - app-network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]  # rota de health check do frontend
      interval: 30s 
      timeout: 10s
      retries: 3   

networks:
  app-network:
    driver: bridge

```

Sumarizando um pouco o que foi feito no docker-compose.yml:

- Definimos a versão do Docker Compose como `3.8`.
- Definimos dois serviços: `backend` e `frontend`.
- Para cada serviço, definimos o build context e o Dockerfile a ser utilizado.
- Mapeamos as portas dos contêineres para as portas do host.
- Mapeamos os volumes dos contêineres para os diretórios locais.
- Definimos a rede a ser utilizada para a comunicação entre os contêineres.
- Configuramos o healthcheck para verificar a saúde dos contêineres.
- Definimos a rede `app-network` como bridge para a comunicação entre os contêineres.

Para rodar os contêineres juntos, basta rodar o seguinte comando:

```bash

docker-compose up --build

``
