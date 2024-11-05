---
title: Tratamento de dados e Feature Engineering
sidebar_position: 1
description : Tratamento de dados e Feature Engineering desenvolvidos na sprint 3
---

# Introdução

&emsp;&emsp;Durante a sprint 03, o grupo trabalhou na exploração de novas features para o modelo preditivo com base no protótipo desenvolvido na sprint 02. Assim como nas fases anteriores, a metodologia CRISP-DM foi fundamental para o desenvolvimento. 

<p align="center"><b> Figura 1 - Crisp-DM</b></p>
<div align="center" class="zoom-image">
  <img src={require('./../../../static/img/crispEtapas.png').default} alt="Crisp-DM"/>
  <p><b>Fonte:</b> EBAC Online</p>
</div>

## Metodologia

&emsp;&emsp;Na sprint 3, o foco do desenvolvimento foi no entendimento dos dados e na preparação dos dados. As outras fases do CRISP-DM foram mantidas de acordo com o que foi desenvolvido na sprint 2.

### Entendimento dos Dados:

&emsp;&emsp;A fase de Entendimento dos Dados envolve uma etapa essencial de exploração dos dados. Por meio dessa imersão nos dados, a equipe busca garantir que eles sejam confiáveis, de alta qualidade e diretamente relevantes para o objetivo do projeto em questão.

&emsp;&emsp;Nesta sprint, identificou-se que a planilha "STATUS" fornecida pelo parceiro continha informações relevantes que ainda não haviam sido exploradas para melhorar o modelo, como as estações de montagem e o tempo gasto em cada uma delas, especialmente porque muitos desses dados são anteriores ao processo de rodagem dos carros. No entanto, essas informações poderiam ser melhor aproveitadas após um tratamento, selecionando apenas as estações pelas quais os KNRs passaram antes do teste de rodagem, e combinando-as para gerar uma nova coluna de dados no dataset.

&emsp;&emsp;Também foi observado que os dados de carros com falhas relatadas estavam extremamente desbalanceados, o que pode prejudicar a performance do modelo e causar impressões erradas. Isso ocorre porque o modelo pode acertar muitas vezes que um carro não terá falha apenas por generalizar que todos os carros não vão falhar, colocando em risco a segurança dos testes dos carros.

&emsp;&emsp;Além do desbalanceamento nos dados de rodagem, foi observado que a identificação correta de falhas nos carros só seria possível ao relacionar o KNR nas tabelas "STATUS" e "FALHAS". Se o KNR aparecesse em ambas as tabelas, isso indicava que o carro sofreu alguma falha durante o processo. Caso o KNR estivesse presente apenas na tabela "STATUS", isso significava que o carro completou o processo de fabricação sem falhas.

&emsp;&emsp;É muito importante compreender os dados de forma sólida, não apenas para simplificar o processo de modelagem, mas também para desempenhar um papel crucial na avaliação da adequação dos dados para atender às demandas específicas do projeto.

### Preparação dos Dados:
&emsp;&emsp;Esta etapa é fundamental para determinar o conjunto de dados que será utilizado no projeto. Portanto, os dados devem passar por uma fase de tratamento, crucial para garantir que nenhum dado de entrada problemático resulte em saídas imprecisas. Assim como nas outras etapas, a preparação dos dados já foi realizada na primeira sprint. No entanto, durante a sprint três, essa preparação foi aprimorada por meio das seguintes alterações:

&emsp;&emsp;A primeira hipótese testada nesta sprint foi que o modelo estava com baixo desempenho devido ao desbalanceamento dos dados. Para investigar isso, foi realizado um balanceamento dos dados utilizando o dataset desenvolvido na sprint dois, através do método de undersampling. Após esse balanceamento inicial, que reduziu o dataset para 5.000 linhas, decidiu-se que a melhor estratégia seria revisar os dados novamente e trabalhar na seleção de features antes de aplicar o balanceamento.

&emsp;&emsp;Os dados de cada aba da planilha STATUS foram extraidos e agrupados em um unico dataset que facilitasse a leitura dos dados. 

&emsp;&emsp;Em seguida, foram selecionadas apenas as estações de status relacionadas aos HALLEs até o ZP7, ou seja, antes do início dos dados de rodagem dos carros. Esse foi um passo importante, pois os dados só são úteis se forem obtidos antes do processo de rodagem.

```
status_necessarios = ['R750', 'L540', 'G700', 'M600', 'M700']

df_filtrado = df_tst[df_tst['STATUS'].isin(status_necessarios)]

df_filtrado['Presença'] = 1

df_pivot = df_filtrado.pivot_table(index='KNR', columns='STATUS', values='Presença', aggfunc='max', fill_value=0)

df_pivot = df_pivot.reindex(columns=status_necessarios, fill_value=0)

df_pivot.reset_index(inplace=True)

print(df_pivot)
```

&emsp;&emsp;Decidiu-se criar novas features a partir dos dados da coluna "DATA" para avaliar o tempo que cada KNR levou em cada estação. Para isso, o colaborador da empresa parceira forneceu a ordem cronológica que cada carro deve seguir no processo de fabricação. Com base nessa informação, foi calculado o tempo gasto em cada estação.

```
status_necessarios = ['R750', 'L540', 'G700', 'M600', 'M700']

for status in status_necessarios:
    df_tst[f'Tempo{status}'] = pd.Timedelta(seconds=0)

```

A informação sobre o tempo que cada KNR levou em cada estação foi incorporada ao dataset por meio da criação de novas features, seguindo o padrão de nomeação: Tempo\{estação\}. Dessa forma, foram adicionadas cinco novas features.

&emsp;&emsp;Também foram criadas colunas nomeadas após cada estação, indicando se o KNR passou ou não por essas estações. Essa implementação foi feita porque vários KNRs tinham dados referentes a todas as estações.

```
status_necessarios = ['R750', 'L540', 'G700', 'M600', 'M700']

df_filtrado = df_tst[df_tst['STATUS'].isin(status_necessarios)]

df_filtrado['Presença'] = 1

df_status_columns = df_filtrado.pivot_table(index='KNR', columns='STATUS', values='Presença', aggfunc='max', fill_value=0)

df_status_columns = df_status_columns.reindex(columns=status_necessarios, fill_value=0)
```

&emsp;&emsp;Por fim, os dados de falhas foram obtidos de uma maneira diferente. Nessa sprint, decidiu-se que era mais adequado para o projeto obter informações sobre falhas a partir da relação entre as tabelas de falhas e status para validar quais KNRs apresentaram falhas. Se o KNR estivesse presente em ambas as planilhas, seria considerado que houve falhas; caso estivesse apenas na planilha "STATUS", seria considerado que não houve falhas.

### Avaliação:
&emsp;&emsp;Ao analisar o conjunto de dados após a construção do dataset, foi constatado que os dados disponíveis não eram suficientes para construir um modelo eficiente com volume relevante de informações. Isso foi evidenciado durante o treinamento do modelo, que não gerou métricas significativas para a construção. É possível que o tratamento dos dados tenha apresentado erros ou que algumas features possam ser melhor exploradas. Essas questões serão investigadas e os resultados serão reavaliados na próxima sprint.

### Conclusão

&emsp;&emsp;Embora os resultados de desempenho do modelo não tenham melhorado, é crucial que os desenvolvedores continuem o processo de tratamento e engenharia de features, pois os dados ainda estão desbalanceados e a capacidade do modelo de identificar carros com possíveis falhas permanece insatisfatória. Na próxima sprint, os dados serão submetidos novamente ao processo de tratamento e novos modelos serão testados com o objetivo de alcançar uma melhor performance.
