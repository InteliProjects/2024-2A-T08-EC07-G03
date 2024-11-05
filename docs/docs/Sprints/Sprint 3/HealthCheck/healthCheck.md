---
title: Sistema de monitoramento da saúde das instâncias (Health Check)
sidebar_position: 1
description : Health Check desenvolvido na sprint 3
---

# Introdução

&emsp;&emsp;O sistema de monitoramento da saúde das instâncias é uma ferramenta que permite a verificação do estado de cada instância do sistema, no nosso caso backend e frontend. Fizemos isso através da função `healthCheck` do docker-compose, que verifica se as instâncias estão saudáveis e prontas para uso. Isso é feito através de uma requisição HTTP em uma rota específica, tanto para o backend quanto para o frontend.

# Docker compose

&emsp;&emsp;O docker-compose é uma ferramenta que permite a definição e execução de aplicativos Docker multi-container. Com ele, é possível definir os serviços, redes e volumes necessários para a execução de uma aplicação Docker. No nosso caso, utilizamos o docker-compose para definir os serviços do backend e do frontend, bem como a configuração do healthCheck.

Mais informações sobre o docker-compose podem ser encontradas [aqui](../Dockers/Docker.md).

# Health Check do Backend

No backend, o healthCheck é feito através da rota `/api/healthcheck/health`, que retorna um JSON com a mensagem "Ok". Para isso, foi adicionado o seguinte trecho de código no arquivo `routes/health.py`:

```python

@router.get("/health")
async def health_check():
    return {"status": "ok"}

```

No docker-compose, foi adicionado o seguinte trecho de código para configurar o healthCheck:

```yaml
healthcheck:
    test: ["CMD", "curl", "-f", "htt
  Compiled successfully in 152.43msp://localhost/api/healthcheck/health"]
    interval: 30s # Tempo entre os testes
    timeout: 10s # Tempo para o teste falhar
    retries: 3  # Numero de tentativas
    start_period: 60s # Tempo pra começar testar o status

```

# Health Check do Frontend

No frontend, configuramos um servidor nginx para servir a aplicação. O healthCheck é feito através da rota `/health`, que retorna um JSON com a mensagem "Ok". Para isso, foi adicionado o seguinte trecho de código no arquivo `nginx.conf`:

```nginx

server {
    listen 80;
    server_name localhost;

    location / {
        root /usr/share/nginx/html;
        try_files $uri $uri/ /index.html;
    }

    # Serve arquivos estáticos da pasta assets
    location /assets/ {
        root /usr/share/nginx/html;
        expires 3d;  # Configura cache para os ativos estáticos
    }

    # Health check
    location /health {
        return 200 'OK';
        add_header Content-Type text/plain;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}

```

No docker-compose, foi adicionado o seguinte trecho de código para configurar o healthCheck:

```yaml
healthcheck:
    test: ["CMD", "curl", "-f", "http://localhost/health"]
    interval: 30s # Tempo entre os testes
    timeout: 10s # Tempo para o teste falhar
    retries: 3  # Numero de tentativas
    start_period: 60s # Tempo pra começar testar o status
```

# Conclusão

O healthCheck é uma ferramenta importante para garantir a disponibilidade e a confiabilidade de um sistema. Com ele, é possível verificar se as instâncias do sistema estão saudáveis e prontas para uso. No nosso caso, configuramos o healthCheck tanto no backend quanto no frontend, garantindo que as instâncias estejam sempre disponíveis e funcionando corretamente.

Para verificar o status do container, basta executar o comando `docker ps` e verificar a coluna `STATUS`. Se o status for `healthy`, significa que o healthCheck foi bem-sucedido e a instância está saudável. Caso contrário, é necessário verificar o log do container para identificar o problema e corrigi-lo. Exemplo:

```bash

CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                    PORTS                                               NAMES
bcae98fe746f   src-backend    "uvicorn app:app --h…"   18 minutes ago   Up 18 minutes (healthy)   8000/tcp, 0.0.0.0:8000->80/tcp, [::]:8000->80/tcp   src-backend-1
defeca693ca8   src-frontend   "/docker-entrypoint.…"   18 minutes ago   Up 18 minutes (healthy)   88/tcp, 0.0.0.0:7000->80/tcp, [::]:7000->80/tcp     src-frontend-1

```

Na proxima sprint vamos adicionar uma aplicação de monitorament idependente para verificar o status de cada instância e enviar alertas em caso de falha.







