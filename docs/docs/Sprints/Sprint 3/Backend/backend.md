---
title: Backend
sidebar_position: 2
description : Backend que desenvolvido na sprint 3
---

# Introdução

A partir do que foi desenvolvido na Sprint 2, o grupo Käfer continuou o desenvolvimento do backend da solução, com o objetivo de adicionar mais rotas e fazer com que as informações fossem guardadas no banco de dados. Essa etapa é essencial essencial para garantir a comunicação eficaz entre os resultados do modelo preditivo e a interface do usuário.

## Visão Geral do Projeto

O backend foi contruído com FastAPI para fornecer endpoints que interagem com um modelo preditivo e um banco de dados Supabase. O backend é responsável por:

- Receber e processar dados de entrada.
- Fazer previsões com um modelo treinado. 
- Armazenar e recuperar dados de treinamento e previsões

### Tecnologias Utilizadas:

- FastAPI
- Uvicorn
- Pydantic
- Supabase
- Joblib
- Pandas
- Python 3.12

## Rotas e Endpoints

### POST /api/insert_model_training

Insere um novo registro de treinamento do modelo.

* **Parâmetros  de Requisição:**
    - **Body:**
        - 'model_name' (str): Nome do modelo.
        - 'training_accuracy' (float): Precisão do treinamento.
        - 'date' (str): Data do treinamento no formato YYYY-MM-DD

* **Resposta:**
    - **200 OK:**

    ```json
    {
      "message": "Model created successfully",
      "comparison_with_previous": "Melhoria"
    }
    ```
    - **400 Bad Request:**
    
    ```json
    ----
        {
        "message:" "Data inválida. O formato correto é YYYY-MM-DD"
        }

    ```

* **Exemplo de Requisição com cURL:**
  ```bash

  curl -X POST "http://127.0.0.1:8000/api/insert_model_training" -H "Content-Type: application/json" -d 
    
        {
        "model_name": "Model A",
        "training_accuracy": 0.85,
        "date": "2024-09-10"
        }

  ```

### GET /api/model_training_history

Recupera o histórico de treinamento do modelos.

* **Resposta:**
  - **200 OK:**

    ```json
    {
      "training_history": [
        {
          "model_name": "Model A",
          "training_accuracy": 0.85,
          "date": "2024-09-10 00:00:00"
        }
      ]
    }

  ```

* **404 Not Found:**


    ```json
        {
        "message": "No training history found"
        }     
    ```

## Funções e Métodos

### `make_prediction(knr: str)`

Faz um apredição com base no KNR fornecido.

* **Parâmetros:**
  - `knr` (str): Código KNR para busca e predição.

* **Retorno:**
  - Dicionário com o resultado da predição.

* **Exemplo de Uso:**

    ```python
        result = make_prediction("12345")
        print(result)
    ```
