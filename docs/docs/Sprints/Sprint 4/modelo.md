---
title: Tratamento de dados e Feature Engineering
sidebar_position: 1
description: Tratamento de dados e Feature Engineering desenvolvidos na sprint 3
---

# Introdução

&emsp;&emsp;Durante a sprint 04, o grupo trabalhou na exploração de novas features para o modelo preditivo com base no protótipo desenvolvido na sprint 03. Assim como nas fases anteriores, a metodologia CRISP-DM foi fundamental para o desenvolvimento.

## Metodologia

&emsp;&emsp;Durante a sprint 4, o grupo trabalhou na exploração de novas features para o modelo preditivo com base no protótipo desenvolvido na sprint 3. Assim como nas fases anteriores, a metodologia CRISP-DM foi fundamental para o desenvolvimento.

&emsp;&emsp;Nesta sprint, identificou-se que a planilha "STATUS" fornecida pelo parceiro continha informações relevantes sobre o tempo gasto nas estações, juntamente com as informações de identificação de resultados do sistema em relação aos KNRs, por meio da tabela de resultados na coluna NAME.

**Agrupando por KNR e somar o tempo gasto em cada ZP/CAB**

```
# Aplicar a função de grupo ao dataframe
df_filtered['Group'] = df_filtered['STATUS'].apply(get_group)

# Calcular a diferença de tempo entre os status consecutivos para o mesmo KNR
df_filtered['Tempo'] = df_filtered.groupby('KNR')['DATA'].diff().dt.total_seconds() / 60  # Diferença em minutos

# Preencher NaN com 0, já que a primeira ocorrência não tem tempo anterior
df_filtered['Tempo'] = df_filtered['Tempo'].fillna(0)

# Criar colunas para armazenar o tempo gasto em cada ZP/CAB
for group in station_to_group.keys():
    df_filtered[f'Tempo_{group}'] = df_filtered.apply(lambda row: row['Tempo'] if row['Group'] == group else 0, axis=1)

# Agrupar por KNR e somar o tempo gasto em cada ZP/CAB
df_result = df_filtered.groupby('KNR').agg({f'Tempo_{group}': 'sum' for group in station_to_group.keys()}).reset_index()
```
**Criando colunas com os dados da coluna NAME**

```
# Criar uma tabela pivô onde cada NAME se torna uma coluna
df_merged = df_merged.pivot_table(index='KNR', columns='NAME', aggfunc='size', fill_value=0)

# Alterar os valores diferentes de zero para 1 (para indicar que aquele KNR tem dados para aquele NAME)
df_merged = (df_merged > 0).astype(int)

# Resetar o índice para trazer KNR de volta como coluna
df_merged = df_merged.reset_index()

# Exibir o DataFrame resultante
print(df_merged)

```

&emsp;&emsp;Para melhor aproveitamento dos dados, foi realizado um tratamento em cada uma das tabelas para garantir que não haveria dados nulos, repetidos ou dados de estações pelas quais os KNRs passam depois do teste de rodagem, que não serão utilizados no treinamento do modelo. Isso porque, no momento de uso real desse projeto, esses dados ainda não terão sido obtidos, dado que o objetivo do projeto é desenvolver uma solução que será utilizada antes do processo de rodagem dos carros da VW.

&emsp;&emsp;Além disso, os dados da coluna NAME da tabela RESULTS foram utilizados, já que essa coluna fornece informações sobre os resultados do sistema após as fases de parafusamento, pintura e outras fases que envolvem muitos detalhes. Para isso, cada NAME único foi transformado em uma coluna com o nome respectivo. Caso o KNR tenha recebido a característica do NAME, ele recebeu o número 1, indicando que teve aquele resultado; caso contrário, recebeu o valor 0, indicando que não teve aquele resultado.

&emsp;&emsp;Ao final do tratamento dos dados, as novas features de STATUS e RESULTS foram agrupadas em um único dataset. Esse novo dataset foi salvo como `results_merged.csv` e utilizado para o treinamento do modelo LSTM. Um ponto importante a se considerar é que, após todo o tratamento dos dados, a base de dados ficou com cerca de 300 linhas, o que é uma quantidade muito pequena para o treinamento do modelo. Por isso, é importante que na próxima sprint seja feita uma análise no último tratamento dos dados para garantir que nenhum dado foi perdido nesse processo.

&emsp;&emsp;Como mencionado anteriormente, o algoritmo escolhido para realizar o treinamento do modelo foi o LSTM. O modelo foi treinado com 100 épocas e chegou aos seguintes resultados:
- Acurácia de teste: 98%
- Precisão: 77%
- Recall: 100%
- F1-Score: 87%

&emsp;&emsp;O próximo passo é testar a performance do modelo com os novos dados fornecidos pela VW, para analisar com mais dados o que deve ser melhorado no modelo.
