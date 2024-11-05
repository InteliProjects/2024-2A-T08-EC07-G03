---
title: Requisitos de Visualização
sidebar_position: 1
description: Levantamento de requisitos de visualização para o projeto
---

# Introdução

A seguir será descrito como será a visualização dos dados do projeto no frontend/dashboard que será desenvolvido para entender melhor a relação dos dados e dos resultados gerados atráves do nosso modelo. 

## Necessidades do Projeto

Segue abaixo as necessidades levantadas que a interface do projeto deve atender:

- **Clareza e Intuitividade na Apresentação dos Dados e Resultados:** A visualização deve ser clara e intuitiva, permitindo que os analistas de sistemas e outros stakeholders identifiquem rapidamente os pontos críticos na linha de produção a partir do resultado do modelo preditivo.

- **Interatividade:** A visualização deve ser interativa, permitindo que os usuários explorem diferentes cenários e dados, como o impacto de variações nas matérias-primas ou nas práticas de logística. A interação pode incluir zoom, filtragem de dados e a seleção de diferentes camadas de informação para uma análise mais detalhada.

- **Integração de Dados Dinâmicos:** O sistema deve conseguir integrar novos dados periodicamente e consegui refletir os novos dados gerados. Isso inclui a capacidade de visualizar dados de novos lotes de produção, impactos atualizados e o desempenho do modelo preditivo ao longo do tempo.

- **Segurança de Dados:** É crucial garantir que o sistema de visualização tenha medidas de segurança robustas, como autenticação de usuários e criptografia de dados, para proteger informações sensíveis.

- **Escalabilidade:** A solução deve ser escalável para acomodar um aumento no volume de dados ou novos requisitos de visualização no futuro.
  
- **Feedback ao Usuário:** Fornecer feedback visual, como animações sutis, para indicar quando novos dados são carregados ou quando uma interação (como a aplicação de um filtro) foi bem-sucedida.
  
- **Consistência Visual:** Utilizar uma paleta de cores consistente e um layout uniforme em todo o dashboard para facilitar a navegação e interpretação dos dados.

## Possibilidades de Acesso e Visualização

Caso seja necessário, o dashboard poderá ser acessado por diferentes tipos de usuários, cada um com diferentes permissões de acesso e necessidades de visualização. Abaixo estão descritos os tipos de usuários e as permissões de acesso que cada um terá:

### Tipos de Usuários e Permissões de Acesso

- **Gerentes de Produção:** Acesso a uma visão geral do ciclo produtivo com dashboards que apresentam KPIs, áreas de risco, e o desempenho geral do processo produtivo. Eles terão permissão para visualizar dados históricos e realizar comparações de desempenho entre diferentes períodos.

- **Analistas de Sistemas:** Acesso a dados detalhados, incluindo a visualização de métricas de desempenho do modelo preditivo, taxas de defeitos por classe, e a análise de tendências. Eles terão a capacidade de exportar dados e realizar análises mais profundas.

### Frontend do Dashboard

Para atender às necessidades dos usuários e garantir uma experiência de visualização que gere valor, a interface do dashboard deve incluir os seguintes elementos:

#### Gráficos e Dados

1. **Visão Geral do Ciclo Produtivo:**
   - **Gráfico de Barras Empilhadas ou Gráfico de Linhas:** Mostra a distribuição dos defeitos identificados por classe ao longo do tempo. Permite que os usuários vejam a evolução das taxas de defeitos e identifiquem possíveis padrões.

2. **Análise de Risco e Fragilidade:**
   - **Heatmap:** Destaca as áreas do processo produtivo (Setores) com maior incidência de problemas e sendo possível identificar quais foram os problemas nessas áreas.

3. **Desempenho do Modelo Preditivo:**
   - **Gráfico de Confusão:** Mostra a precisão do modelo preditivo, exibindo a distribuição de previsões corretas e incorretas para cada classe..
   - **Gráfico de Evolução da Acurácia:** Linha do tempo mostrando como a acurácia do modelo tem melhorado ao longo do tempo com a introdução de novos dados e ajustes de parâmetros.

Essa é uma visão geral de como será a visualização dos dados do projeto no frontend/dashboard que será desenvolvido para entender melhor a relação dos dados e dos resultados gerados atráves do nosso modelo.



