---
title: Matriz de Risco
sidebar_position: 1
description : Apresentação da análise de risco do projeto
---

# Matriz de Risco

## Introdução

A matriz de riscos é uma ferramenta de análise de negócios e projetos, onde organizamos os riscos e oportunidades em uma tabela, onde as linhas são os riscos, e as colunas são os impactos e probabilidades. A partir disso, é possível identificar os riscos mais críticos e que requerem maior atenção e alocação de recursos para serem gerenciados. A matriz de risco que desenvolvemos considera o protótipo e o produto final do projeto.

<p align="center"><b> Figura 1 - Matriz de Risco</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/MatrizRiscoGrupo03.png').default} alt="Matriz de risco"/>
  <p><b>Fonte:</b> Elaborado por Grupo 3</p>
</div>

## Ameaças

### 1. Acurácia do modelo final inferior a 95%
- **Detalhamento:** Caso o modelo não atinja a acurácia mínima desejada, os resultados das previsões podem ser comprometidos, levando a inspeções ineficazes ou incorretas, o que pode impactar negativamente a eficiência do processo.

### 2. Falhas na inserção de novos dados no modelo, impactando negativamente nos resultados
- **Detalhamento:** Se novos dados não forem incorporados corretamente ou se o modelo não estiver preparao para isso, o modelo pode se desatualizar e não refletir as mudanças na produção, reduzindo a eficácia do processo de predição.

### 3. Falta de features (colunas) nos dados usados no treinamento do modelo
- **Detalhamento:** Se os dados que foram fornecidos para a gente não tiverem informações suficientes pode limitar o treinamento do modelo assim reduzindo a capacidade de realizar predições precisas, resultando em uma classificação inadequada dos veículos.

### 4. Mudanças nos parâmetros atuais em produção, afetando o modelo
- **Detalhamento:** Alterações nos parâmetros de produção podem exigir ajustes no treinamento modelo preditivo para que ele continue fornecendo resultados precisos e relevantes.

### 5. Modelo gerar muitos falsos positivos, ocasionando em possíveis decisões erradas
- **Detalhamento:** Falsos positivos podem levar a ações desnecessárias ou incorretas, como a realização de inspeções em veículos que não necessitam, desperdiçando tempo e recursos.

### 6. Modelo não se adaptar a novos dados quando for implementado
- **Detalhamento:** A incapacidade do modelo de se ajustar a novos dados pode reduzir sua utilidade ao longo do tempo, necessitando de re-treinamento frequente ou ajustes constantes.

### 7. Falta de engajamento do parceiro no desenvolvimento do projeto
- **Detalhamento:** A falta de envolvimento do parceiro pode dificultar o progresso do projeto, afetando a comunicação, alinhamento de expectativas e entrega dos resultados.

### 8. Limitações de recursos computacionais em relação a hardware
- **Detalhamento:** Restrições de hardware podem limitar a capacidade de processamento do modelo, impactando o tempo de treinamento e a eficiência geral do sistema. Atualmente, temos acesso a supercomputadores no laboratório que podem ser utilizados para mitigar esse risco.

### 9. Vazamentos dos dados fornecidos pela VW
- **Detalhamento:** A exposição de dados sensíveis pode acarretar em problemas legais e de reputação, além de comprometer a segurança das informações do projeto.

## Oportunidades

### 1. Diminuir o custo e tempo no processo de inspeção e testagem
- **Detalhamento:** Implementar o modelo preditivo pode reduzir significativamente o tempo e os custos associados à inspeção, aumentando a eficiência do processo de fabricação.

### 2. Gerar insights de melhoria em alguma etapa da fabricação dos carros
- **Detalhamento:** A análise dos dados pode revelar oportunidades de otimização em várias etapas da produção, melhorando a qualidade do produto final.

### 3. Automatização na geração de relatórios e insights a partir do modelo
- **Detalhamento:** A integração do modelo com sistemas de BI pode automatizar a geração de relatórios, facilitando a tomada de decisões e aumentando a agilidade da equipe.

### 4. Implementar e testar a solução para ter um maior TRL-3
- **Detalhamento:** Avançar a maturidade tecnológica da solução pode abrir novas possibilidades para sua aplicação em larga escala, tanto na VW quanto em outras indústrias.

### 5. Melhoria na qualidade dos veículos a partir do modelo desenvolvido
- **Detalhamento:** Ao identificar e corrigir possíveis falhas de produção antes que os veículos saiam da fábrica, a qualidade final pode ser significativamente aprimorada.

## Plano de Ação para Riscos

### 1. Desempenho do modelo inferior ao esperado
- **Ação:** Realizar validações contínuas e ajustes no modelo utilizando diferentes técnicas de machine learning, como ajuste de hiperparâmetros, validação cruzada e teste com diferentes algoritmos.

### 2. Baixa qualidade dos dados
- **Ação:** Implementar um processo forte de limpeza e pré-processamento dos dados. Considerar a utilização de técnicas de imputação de valores ausentes e normalização dos dados.

### 3. Modelo gerar falsos positivos
- **Ação:** Balancear as classes no conjunto de dados de treinamento, ajustar o threshold de classificação e realizar tuning dos parâmetros do modelo.

### 4. Modelo não se adaptar a novos dados
- **Ação:** Estabelecer um processo de re-treinamento mensal do modelo com dados novos e atualizados para garantir a adaptação às mudanças na produção.

### 5. Falhas na inserção de novos dados no modelo
- **Ação:** Automatizar o pipeline de ingestão de dados e implementar verificações de qualidade para garantir que os novos dados sejam inseridos corretamente.

### 6. Mudanças nos parâmetros de atuais em produção, afetando o modelo
- **Ação:** Criar um mecanismo de feedback para capturar mudanças nos parâmetros de produção e ajustar o modelo em tempo real ou durante o re-treinamento.

### 7. Falta de engajamento do parceiro
- **Ação:** Manter uma comunicação constante e transparente com o parceiro e tirar o máximo das reuniões de alinhamento de cada sprint.

### 8. Limitações de recursos computacionais
- **Ação:** Utilizar os supercomputadores do laboratório.

### 9. Vazamentos dos dados
- **Ação:** Manter os dados em ambientes seguros e não subir dados sensíveis para repositórios públicos.

## Conclusão

A matriz de riscos é uma ferramenta essencial para o gerenciamento de riscos em projetos, e durante as próximas sprints, será utilizada para monitorar e controlar os riscos identificados. O plano de ação proposto visa mitigar os riscos e aproveitar as oportunidades identificadas, garantindo um projeto eficiente e que gere valor para o cliente.
