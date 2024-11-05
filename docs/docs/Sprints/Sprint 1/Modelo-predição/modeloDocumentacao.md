---
title: Primeiro modelo de predição
sidebar_position: 2
description : Primeiro modelo de predição
---

# Introdução

&emsp;Para o primeiro sistema preditivo desta primeira sprint, o modelo foi estruturado com base na metodologia CRISP-DM, uma das abordagens mais consolidadas e eficazes dentro do universo de Data Science, caracterizada por um ciclo iterativo, onde cada etapa do processo é revisitada conforme necessário, desde o Entendimento do Negócio. Essas fases são fundamentais para garantir que o modelo preditivo desenvolvido esteja alinhado com os objetivos do negócio e seja capaz de gerar resultados. A partir desda metodologia, foi desenvolvido um modelo preditivo com métricas de classificação para a exibição dos resultados.

# Metodologia

&emsp;O projeto foi estruturado com base na metodologia CRISP-DM (Cross Industry Standard Process for Data Mining). Essa é uma abordagem presente na metodologia ágil, amplamente empregada em iniciativas que exploram o universo do Data Science e Machine Learning, especialmente em contextos caracterizados por volumes expressivos de dados.

&emsp;O CRISP-DM opera como um ciclo iterativo, uma vez que, dada a complexidade à manipulação e interpretação de vastos volumes de dados, é crucial proceder com avanços de etapa a etapa para alcançar um progresso gradual no ciclo do projeto. Essa metodologia apresenta seis estágios distintos, porém para esta primeira sprint de projeto a implementação do modelo será da etapa 1 até a etapa 5: Entendimento do Negócio, Entendimento dos Dados, Preparação dos Dados, Modelagem e Avaliação

<p align="center"><b> Figura 1 - Crisp-DM</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/crispEtapas.png').default} alt="Crisp-DM"/>
  <p><b>Fonte:</b> Elaborado por Grupo 3</p>
</div>

Fonte: EBAC Online

&emsp;Entendimento do Negócio: A fase inicial do processo CRISP-DM, conhecida como Entendimento do Negócio, desempenha um papel crucial ao aprofundar-se na compreensão do panorama e do contexto em que o projeto está envolvido. Nesse estágio, busca-se adquirir conhecimento dos objetivos e exigências do projeto, além de mapear como esses objetivos se traduzem em desafios de análise de dados. Essa exploração inicial é fundamental, uma vez que estabelece fundamentos essenciais para a tomada de decisões estratégicas, desde o começo até os momentos futuros do projeto. Nessa sprint, o entendimento do negócio foi feito a partir da criação de diversas ferramentas de negócios, como o Business Model Canvas, a Análise Financeira e a Matriz de Riscos.

&emsp;Entendimento dos Dados: A próxima fase é o Entendimento dos Dados. Ela envolve uma etapa essencial de coleta e exploração dos dados. Por meio dessa imersão nos dados, a equipe busca garantir que eles sejam confiáveis, de alta qualidade e diretamente relevantes para o escopo do projeto em questão. Uma compreensão sólida dos dados não apenas simplifica o processo de modelagem, mas também desempenha um papel importante na avaliação da adequação dos dados para atender às demandas específicas do projeto. Além disso, verificações rigorosas quanto à precisão, coesão e coerência dos dados são realizadas, assim como a criação de relatórios descritivos que fornecem insights sobre a natureza dos dados. Todo esse entendimento foi feito a partir de diversos estudos sobre os dados, que podem ser exemplados nas seguintes imagens:

<p align="center"><b> Figura 2 - Top 10 falhas mais comuns</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/10_falhas.png').default} alt="10 falhas"/>
  <p><b>Fonte:</b> Elaborado por Grupo 3</p>
</div>

<p align="center"><b> Figura 3 - Distribuição das Falhas ao Longo do Tempo</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/distri_falhas.png').default} alt="distri falhas"/>
  <p><b>Fonte:</b> Elaborado por Grupo 3</p>
</div>

Fonte: Elaborado pelo grupo Käfer

&emsp;Preparação dos dados: A etapa de Preparação dos Dados, também reconhecida como "pré-processamento", é fundamental na determinação do conjunto de dados que será utilizado no projeto. Os dados devem passar por uma fase de tratamento, que é crucial para garantir que nenhum dado de entrada problemático resulte em saídas imprecisas. Isso foi feito nesta sprint a partir de ajustes nas planilhas dos dados enviados, e também em mudanças nos dataframes, para que os modelos sejam capazes de funcionarem a partir dos dados enviados, como a transformação dos dados categóricos em númericos, que pode ser visto no notebook da documentação desta sprint.

&emsp;Modelagem: Nessa etapa retomamos tudo aquilo que foi feito nas etapas anteriores ao analisar os dados, preparar esses dados e compreender o objetivo do projeto, para que a escolha do modelo seja a melhor possível, podendo se repetir diversas vezes essa etapa até achar um modelo adequado ao projeto. Para esta sprint 1, decidimos seguir com o modelo Random Forest Classifier, dada as características de predição existentes neste projeto para realizar, que consiste nas determinações de falhas na produção dos carros na fábrica da Volkswagen. 

&emsp;Avaliação: Nesta etapa são analisadas as respostas obtidas no item anterior e é verificado se está de acordo com os objetivos do negócio e os resultados esperados pelo parceiro do projeto, seguindo a metodologia crisp, se o modelo não está de acordo é possível voltar às etapas, realizando novamente um teste de modelo preditivo, além de poder retornar para realizar uma nova preparação dos dados. Nessa fase é testado o modelo e a partir dos resultados sabemos se o modelo tem uma boa eficácia, além de finalizar a parte mais voltada para a programação e seguir para a última etapa da metodologia crisp. Dado este princípio, vale adiantar nesta documentação que ocorreu o fenômeno de overfitting neste primeiro modelo preditivo do projeto, então é possível prever que haverá novas modelagens de dados e testes em outros modelos preditivos com a finalidade de melhorar os resultados da predição.

# Modelo

&emsp;O escolhido para a introdução desse projeto foi o Random Forest. “Em resumo, o Random Forest irá criar muitas árvores de decisão, de maneira aleatória”[1] e, em seguida, combina os resultados dessas árvores para formar um único resultado consolidado. Esse algoritmo encontra-se na biblioteca scikit-learn e baseia-se no conceito de ensemble learning, que envolve o uso de vários modelos para obter uma previsão, muito parecido com a abordagem de uma árvore de decisão tradicional. No entanto, o Random Forest utiliza diversas árvores de decisões para gerar a previsão esperada. É um modelo versátil e pode ser usado tanto para regressão ou classificação, que teve a classificação como forma escolhida nesse projeto para prever falhas na produção de automóveis na fábrica da Volkswagen. Devido a sua capacidade de lidar com o uso de diversas features e ao mecanismo de ensemble, esse modelo se torna muito eficiente em resultados com diversos tipos de problemas.

<p align="center"><b> Figura 4 - Random Forest</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/randomForest.png').default} alt="Random Forest"/>
  <p><b>Fonte:</b> Deniz Gunay</p>
</div>

# Métricas

&emsp;Na criação de um modelo preditivo, é essencial serem utilizados critérios para avaliar o desempenho deste. Desse modo, esses critérios são chamados de métricas e elas podem ser divididas em dois grupos: de regressão e de classificação. Assim, foram utilizadas métricas de classificação para avaliar o modelo preditivo desenvolvido pela equipe Käfer, uma vez que o modelo testado foi o Random Forest Classifier. As métricas escolhidas são: Acurácia, Precisão, Sensibilidade (Recall) e F1-Score. Além disso, é importante ressaltar que o grupo utilizou a biblioteca sklearn.metrics para realizar o cálculo das métricas, o que é apresentado no trecho de código abaixo:

<p align="center"><b> Figura 5 - Métricas</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/metricasSprint1Kafer.png').default} alt="Metricas"/>
  <p><b>Fonte:</b> Elaborado por Grupo 3</p>
</div>

&emsp;Nesse sentido, a seguir serão apresentadas os significados das métricas de classificação utilizadas para avaliar o modelo preditivo:

1- Acurácia: A acurácia mede a proporção total de predições corretas em relação ao número total de exemplos.

2- Precisão: A precisão mede a proporção de predições positivas corretas em relação ao total de predições positivas feitas pelo modelo.

3- Sensibilidade (Recall): A sensibilidade (ou recall) mede a proporção de verdadeiros positivos que foram corretamente identificados pelo modelo em relação ao total de exemplos positivos reais.

4- F1-Score: O F1-Score é a média harmônica entre precisão e recall.

A imagem abaixo apresenta todos os resultados obtidos nas métricas apresentadas acima de maneira resumida:

<p align="center"><b> Figura 6 - Resultados</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/resultadosSprint1Kafer.png').default} alt="Resultados"/>
  <p><b>Fonte:</b> Elaborado por Grupo 3</p>
</div>

<p align="center"><b> Figura 7 - Matriz de Confusão</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/output.png').default} alt="Matriz de Confusão"/>
  <p><b>Fonte:</b> Elaborado por Grupo 3</p>
</div>

&emsp;Dados os resultados das quatro métricas escolhidas acima, é possível analisar que ocorreu o fenômeno de overfitting nesta predição, por conta da proximidade dos valores ao número 1, valor máximo destas métricas. O modelo se ajustou muito bem ao conjunto de dados anteriomente verificados, mas será ineficaz para prever novos resultados. Uma das causas para a ocorrência deste fenômeno pode ter sido o desbalanceamento dos dados. Após o recebimento dos dados do cliente, várias ajustes foram feitos nas planilhas, para os dados estarem preparados corretamente para serem utilizados. Além disso, mais ajustes foram feitos no dataframe, que podem ser vistos no notebook da solução, como a transformação dos dados categóricos para numéricos. Apesar do caso de overfitting, o modelo preditivo desta sprint foi concluído dessa forma. 

&emsp;Portanto, com base nos resultados que o algoritmo preditivo proporcionou e ao analisar as métricas obtidas, é possível concluir que o modelo demonstrou a predição da fabricação de um carro na fábrica da Volkswagen, prevendo se ela falhou ou não. A partir destas métricas de avaliação, é possível fazer previsões e fornecer informações para tomar decisões estratégicas com base nas previsões do modelo, o que significa que o algoritmo está cumprindo com seu propósito de executar previsões confiáveis. Apesar da ocorrência do overfitting, foi possível fazer um modelo já na primeira Sprint de projeto, o que foi um passo inicial importante para o desenvolvimento da solução.

# Referências

[1] DIDATICA TECH. O que é e como funciona o algoritmo RandomForest. Disponível em: https://didatica.tech/o-que-e-e-como-funciona-o-algoritmo-randomforest/ Acesso em: 15 ago. 2024.