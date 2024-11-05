FROM python:3.12

# Diretório de trabalho do container
WORKDIR /code2

# Copiar os requirements para dentro do container
COPY ./requirements.txt /code2/requirements.txt

# Instalar as dependências
RUN pip install --no-cache-dir --upgrade -r /code2/requirements.txt

# Copiar todo o conteúdo para dentro de /code2
COPY . /code2

EXPOSE 8009

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8009"]
