---
title: Desenvolvimento do Backend
sidebar_position: 2
description : Backend desenvolvido na sprint 2
---

# Introdução
&emsp;&emsp;Durante a sprint 02, o grupo deu início ao desenvolvimento do backend da solução, com o objetivo de estruturar as rotas que serão utilizadas na aplicação. Esse trabalho é essencial para garantir a comunicação eficaz entre os resultados do modelo preditivo e a interface utilizada pelo usuário.

## Por que FastAPI?

&emsp;&emsp;Escolheu-se o FastAPI para este projeto devido à sua alta performance, que aproveita recursos modernos do Python como tipagem e async/await, facilitando a construção de APIs rápidas e eficientes. A documentação automática e intuitiva proporcionada pelo FastAPI simplifica a integração e o uso do serviço por desenvolvedores e clientes. Além disso, sua escalabilidade permite que o projeto cresça sem comprometer o desempenho. A facilidade de integração com bibliotecas como `pandas` e `sklearn` torna-o especialmente adequado para projetos que envolvem processamento de dados e machine learning.

# Como foi projetado

&emsp;&emsp;Optou-se por receber o KNR como input, com a ideia de que os dados associados a esse KNR possam ser recuperados de um bucket de dados, como o S3. Para replicar esse comportamento em um ambiente local, criamos um arquivo Excel contendo os dados de um KNR específico e implementamos uma função que busca esses dados com base no KNR fornecido na rota.

```
def buscar_dados_por_knr(knr):
    df = pd.read_excel("dados.xlsx")
    dados = df[df["KNR"] == knr]

    if dados.empty:
        raise ValueError(f"KNR {knr} não encontrado.")

    dados["KNR"] = 0

    features = dados[
        [
            "KNR",
            "MODELO",
            "COR",
            "MOTOR",
            "ESTACAO",
            "USUARIO",
            "HALLE",
            "FALHA",
            "DATA_x",
            "NAME",
            "ID",
            "STATUS",
            "UNIT",
            "VALUE_ID",
            "VALUE",
            "DATA_y",
        ]
    ].values

    features = features.reshape(1, -1)

    return features
```

&emsp;&emsp;Na função buscar_dados_por_knr, recebemos o KNR enviado pelo usuário, coletamos os dados armazenados no banco de dados para o KNR requisitado, e formatamos esses dados para a entrada do modelo.

```
def predict(knr: str):
    try:
        data = buscar_dados_por_knr(knr)
        print(data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    prediction = model.predict(data)
    print(type(prediction))

    return {"knr": knr, "prediction": int(prediction[0])}
```

&emsp;&emsp;Na função predict, os dados são enviados como inputs para o modelo, e o resultado da previsão é retornado junto com o KNR. Caso o KNR não seja encontrado, uma exceção HTTP 404 é gerada.

# Estrutura

&emsp;&emsp;Optou-se por utilizar a estrutura de controllers e routers no FastAPI para promover uma organização clara e modular do código. Essa abordagem facilita a manutenção e a escalabilidade do projeto, permitindo que a lógica de negócios (controllers) e o mapeamento das rotas (routers) sejam separados de maneira lógica e organizada. Com essa estrutura, é mais fácil adicionar novas funcionalidades e endpoints sem sobrecarregar o código existente, além de melhorar a legibilidade e a testabilidade do sistema. A separação também permite que diferentes membros da equipe trabalhem em diferentes partes do projeto de forma independente e eficiente.
