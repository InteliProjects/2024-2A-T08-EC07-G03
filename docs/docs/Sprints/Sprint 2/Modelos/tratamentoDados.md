---
title: Tratamento de dados e Feature Engineering
sidebar_position: 2
description : Modelos desenvolvidos na sprint 2
---

# Introdução

&emsp;&emsp;Durante a sprint 02, o grupo aprimorou o modelo preditivo com base no protótipo desenvolvido na sprint 01. Assim como na primeira fase, a metodologia CRISP-DM foi fundamental para o desenvolvimento. Essa metodologia, amplamente reconhecida por sua eficácia, segue um ciclo iterativo, onde cada etapa do processo é revisitada conforme necessário para garantir melhorias contínuas. Utilizando a abordagem CRISP-DM, a equipe desenvolveu um modelo preditivo com métricas de classificação para avaliar e exibir os resultados, aprimorando a precisão e a confiabilidade das previsões.

<p align="center"><b> Figura 1 - Crisp-DM</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/crispEtapas.png').default} alt="Crisp-DM"/>
  <p><b>Fonte:</b> EBAC Online</p>
</div>

## Metodologia

&emsp;&emsp;A seguir, será recapitulando os conceitos do CRISP-DM apresentados na sprint 01 considerando as mudanças feitas.

### Entendimento do Negócio:
&emsp;&emsp;A fase inicial do processo CRISP-DM, conhecida como Entendimento do Negócio, desempenha um papel crucial ao aprofundar-se na compreensão do panorama e do contexto em que o projeto está envolvido. Essa exploração inicial é fundamental, uma vez que estabelece fundamentos essenciais para a tomada de decisões estratégicas, desde o começo até os momentos futuros do projeto. Durante a sprint 01, o entendimento do negócio foi feito a partir da criação de diversas ferramentas de negócios, como o Business Model Canvas, a Análise Financeira e a Matriz de Riscos.

### Entendimento dos Dados:

&emsp;&emsp;A fase seguinte é o Entendimento dos Dados, que envolve uma etapa essencial de coleta e exploração dos dados. Por meio dessa imersão nos dados, a equipe busca garantir que eles sejam confiáveis, de alta qualidade e diretamente relevantes para o objetivo do projeto em questão.

&emsp;&emsp;Nessa sprint, foi identificado que os dados forneciam informações relevantes que ainda não haviam sido exploradas para melhorar o modelo, como as estações de montagem e o tempo gasto em cada uma delas. No entanto, essas informações poderiam ser melhor aproveitadas se fossem combinadas para gerar uma nova coluna de informações no dataset. 

&emsp;&emsp;Também foi observado que os dados de carros com falhas relatadas estavam extremamente desbalanceados, o que pode prejudicar a performance do modelo e causar impressões erradas. Isso ocorre porque o modelo pode acertar muitas vezes que um carro não terá falha apenas por generalizar que todos os carros não vão falhar, colocando em risco a segurança dos testes dos carros.

&emsp;&emsp;É muito importante compreender os dados de forma sólida, não apenas para simplificar o processo de modelagem, mas também para desempenhar um papel crucial na avaliação da adequação dos dados para atender às demandas específicas do projeto.

### Preparação dos Dados:
&emsp;&emsp;Esta etapa é fundamental para determinar o conjunto de dados que será utilizado no projeto. Portanto, os dados devem passar por uma fase de tratamento, crucial para garantir que nenhum dado de entrada problemático resulte em saídas imprecisas. Assim como nas outras etapas, a preparação dos dados já foi realizada na primeira sprint. No entanto, durante a sprint dois, essa preparação foi aprimorada por meio das seguintes alterações:

&emsp;&emsp;Primeiramente, as linhas duplicadas foram removidas do dataset para garantir que nenhuma coluna com dados completamente idênticos se repita, evitando prejuízos aos testes do modelo. 

```
# tirando duplicatas 
df_falhas = df_falhas.drop_duplicates()
df_falhas.info()

```

&emsp;&emsp;Além disso, foram criadas novas colunas com base nas informações das colunas KNR, ID e DATA. Essas novas colunas contêm informações sobre a frequência com que cada ID se repetiu em cada KNR, sendo nomeadas como NVezes1, NVezes2 e NVezes718.

```# Contar o número de ocorrências de cada ID para cada KNR
nvezes_por_estacao = df_result_combined.groupby(['KNR', 'ID']).size().reset_index(name='Contagem')

# Criar um DataFrame pivotado para armazenar a contagem em colunas separadas para cada ID
nvezes_resultado = nvezes_por_estacao.pivot(index='KNR', columns='ID', values='Contagem').fillna(0)

# Renomear as colunas para o formato desejado
nvezes_resultado.columns = ['Nvezes1' if col == 1 else 
                            'Nvezes2' if col == 2 else 
                            'Nvezes718' if col == 718 else f'Nvezes_{col}' for col in nvezes_resultado.columns]

# Resetar o índice para transformar KNR em coluna
nvezes_resultado = nvezes_resultado.reset_index()
```

&emsp;&emsp;Também foram adicionadas colunas que indicam quanto tempo cada KNR gastou em cada ID, com a hipótese de que o tempo gasto em cada ID poderia ser um indicador de falha no carro. As colunas com os valores de tempo foram nomeadas SomaTempo1, SomaTempo2 e SomaTempo718 e os tempos foram medidos em segundos.

```
import pandas as pd

linhas_acima_de_um_dia = resultado[
    (resultado['SomaTempo1'] > pd.Timedelta(days=1)) |
    (resultado['SomaTempo2'] > pd.Timedelta(days=1)) |
    (resultado['SomaTempo718'] > pd.Timedelta(days=1))
]

num_linhas_acima_de_um_dia = len(linhas_acima_de_um_dia)

print(f"{num_linhas_acima_de_um_dia} acima a um dia.")

```

&emsp;&emsp;Por fim, foi criada uma coluna de referência para determinar se um carro apresentou ou não falha na fase de rodagem. Esta coluna foi baseada na coluna FALHAS, que contém dados de diversos tipos de falhas. Como o objetivo é prever apenas as falhas de rodagem, criamos uma nova coluna que captura exclusivamente essa informação, definindo 0 para indicar um carro sem falha de rodagem e 1 para indicar a ocorrência de falha de rodagem.

```
df_combined_final_monstro['TemFalhaRod'] = df_combined_final_monstro['KNR'].apply(lambda x: 1 if x in knr_set else 0)
```

**As seções a seguir foram detalhadas com as escolhas do projeto na seção Modelos, podendo ser encontrada [aqui](./modelos.mdx)!**

### Modelagem:
&emsp;&emsp;Durante essa etapa, o modelo começa a tomar forma, apresentando os primeiros resultados. O tipo de modelagem a ser utilizada normalmente é definida de acordo com a necessidade do negócio e com o tipo de variável a ser analisada. O modelo de uso decidido foi o KNR.

### Avaliação:
&emsp;&emsp;Nesta etapa são analisadas as respostas obtidas no item anterior e é verificado se está de acordo com os objetivos do negócio e os resultados esperados pelo parceiro do projeto, seguindo a metodologia crisp, se o modelo não está de acordo é possível voltar às etapas, realizando novamente um teste de modelo preditivo, além de poder retornar para realizar uma nova preparação dos dados. Nessa fase é testado o modelo e a partir dos resultados sabemos se o modelo tem uma boa eficácia, além de finalizar a parte mais voltada para a programação e seguir para a última etapa da metodologia crisp.

### Conclusão

&emsp;&emsp;Na Sprint 02, a equipe aprimorou o modelo preditivo utilizando a metodologia CRISP-DM, focando na melhoria da precisão e confiabilidade das previsões. O entendimento aprofundado dos dados e a preparação minuciosa, que incluiu a remoção de duplicatas e a criação de novas colunas, foram essenciais para refinar o modelo. A introdução de indicadores de tempo e uma coluna específica para falhas de rodagem alinharam o modelo com os objetivos do projeto. Apesar disso, os dados devem continuar no processo de tratamento e feature engineering dado que eles ainda estão desbalanceados e os acertos do modelo em relação aos carros que podem ter falhas ainda é baixo. Na próxima sprint os dados vão passar novamente pelo processo de tratamento e novos modelos devem ser testados até que os modelos tenham melhor performance.
