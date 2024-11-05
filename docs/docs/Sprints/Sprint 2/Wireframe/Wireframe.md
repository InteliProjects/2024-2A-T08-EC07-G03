---
title: Wireframe
sidebar_position: 1
description : Esboço da Interface
---

### Introdução

Wireframes são essenciais no processo de design e desenvolvimento de qualquer aplicação de software. Eles servem como um esboço que delineia a estrutura, o conteúdo e a funcionalidade da interface antes do início do design ou desenvolvimento real. Wireframes ajudam a visualizar o layout e o fluxo da aplicação, facilitando a compreensão de como o produto final funcionará para desenvolvedores, designers e stakeholders. Ao criar um wireframe, podemos identificar possíveis problemas de usabilidade logo no início, garantindo que o design seja amigável ao usuário e atenda aos requisitos do projeto. Além disso, wireframes fornecem um guia claro para os desenvolvedores seguirem durante a fase de codificação, reduzindo a probabilidade de mal-entendidos e garantindo que o produto final esteja alinhado com o design pretendido.

### 1. Tela Inicial

<p align="center"><b> Figura 1 - Tela Inicial</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/tela_inicial1.png').default} alt="Tela Inicial"/>
  <p><b>Fonte:</b> Elaborado por Grupo 3</p>
</div>

A **Tela Inicial** é o ponto de entrada da aplicação Käfer. Ela apresenta um logotipo proeminente de um besouro (Käfer) no centro da tela, simbolizando o nome da aplicação. Abaixo do logotipo, há dois botões principais: **Executar** e **Treinar**.

- **Executar**: Este botão provavelmente leva o usuário à seção onde ele pode executar ou analisar um conjunto de dados.
- **Treinar**: Este botão provavelmente navega o usuário até a seção de treinamento de modelo, onde ele pode fazer upload de dados e treinar seus modelos.

O design é minimalista, com foco em guiar o usuário para essas duas ações principais.

### 2. Execução e Treino

<p align="center"><b> Figura 2 - Execução e Treino</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/carregamento.png').default} alt="Tabela"/>
  <p><b>Fonte:</b> Elaborado por Grupo 3</p>
</div>

Ao clicar em **Executar** na tela inicial, o usuário é levado à tela de **Upload**.

- Esta tela solicita que o usuário faça o upload de um arquivo CSV para análise.
- O usuário tem a opção de arrastar e soltar o arquivo na área designada ou clicar para fazer o upload.
- Uma barra de progresso na parte inferior indica o status do upload, ajudando o usuário a entender o progresso da entrada de dados.


Se o usuário selecionar **Treinar** na tela inicial, ele é direcionado para a tela de **Treino do Modelo**.

- Semelhante à etapa anterior, esta página solicita que o usuário faça o upload de um arquivo CSV para treinar o modelo.
- Uma barra de progresso indica o status do upload, fornecendo feedback em tempo real para o usuário.

### 3. Modelo Treinado

<p align="center"><b> Figura 3 - Modelo Treinado</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/resultados_treino.png').default} alt="Resultados Treino"/>
  <p><b>Fonte:</b> Elaborado por Grupo 3</p>
</div>

Após o processo de treinamento, o usuário é levado à tela de **Modelo Treinado**.

- Esta tela exibe os resultados atuais e anteriores do modelo treinado.
- O usuário pode visualizar **Gráficos e Métricas** relacionados ao desempenho do modelo.
- Esta tela permite que o usuário compare o desempenho do modelo atual com o anterior, auxiliando na avaliação da eficácia do treinamento.

### 4. Modelo Executado

<p align="center"><b> Figura 4 - Modelo Executado</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/resultados_exc.png').default} alt="Resultados Execução"/>
  <p><b>Fonte:</b> Elaborado por Grupo 3</p>
</div>

Após o processo de treinamneto do modelo, o usuário ao clicar no botão **Home** é redirecionado para a **Tela Inicial**, após todo processo de carregamento da **Execução** do Modelo, o usuário é levado pra tela de resultados do **Modelo Executado**.

- Esta tela exibe os resultados atuais e anteriores do modelo treinado.
- O usuário pode visualizar **Gráficos e Métricas** relacionados ao desempenho do modelo.
- Esta tela permite que o usuário compare o desempenho do modelo atual com o anterior, auxiliando na avaliação da eficácia do treinamento.

### 5. POPUP Ver Mais

<p align="center"><b> Figura 5 - POPUP Ver Mais</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/vermais.png').default} alt="Resultados Ver mais"/>
  <p><b>Fonte:</b> Elaborado por Grupo 3</p>
</div>

Clicar em **Ver Mais** na tela de Resultados abre uma janela detalhada de **POPUP**.

- Este popup fornece uma visão mais aprofundada dos resultados atuais, com foco em um gráfico de barras comparando o desempenho real do modelo com os resultados desejados.
- O usuário pode ver tanto o **Resultado Atual** quanto o **Resultado Desejado**, permitindo uma comparação clara e compreensão de como o modelo se saiu em relação às expectativas.

### Fluxo da Aplicação

A imagem abaixo ilustra o fluxo da aplicação Käfer conforme descrito nas seções acima:

<p align="center"><b> Figura 6 - Fluxo da Aplicação</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/fluxo.png').default} alt="fluxo"/>
  <p><b>Fonte:</b> Elaborado por Grupo 3</p>
</div>

O fluxo da aplicação começa na **Tela Inicial**, onde o usuário escolhe entre **Executar** uma análise de dados ou **Treinar** um modelo. Dependendo da escolha, o usuário será levado para a tela de **Tabela Para Análise** ou **Treino do Modelo**. Após a conclusão das respectivas ações, o usuário pode visualizar os resultados em **Modelo Treinado** ou **Resultados**, com a opção de explorar mais detalhes através do **POPUP Ver Mais**. Este fluxo garante uma navegação intuitiva e eficiente, guiando o usuário por todas as etapas do processo de análise e treinamento de forma clara e direta.

### Conclusão

O wireframe da aplicação Käfer foi criado com a intenção de garantir que os usuários tenham uma experiência simples e eficiente, desde o primeiro contato na tela inicial até a visualização dos resultados detalhados de um modelo treinado. Esse esboço ajuda a entender como cada parte da interface se conecta, tornando a navegação mais fácil e intuitiva, além de assegurar que as funções principais estejam sempre ao alcance.

A construção de um wireframe é essencial para identificar e corrigir problemas de usabilidade logo no início, antes que o desenvolvimento comece. Isso garante que o produto final atenda às expectativas e siga as boas práticas de design. Com o fluxo descrito, o usuário é conduzido por um processo lógico, que simplifica tarefas mais complexas, como a análise de dados e o treinamento de modelos.

Esta parte do documento serve como uma base sólida para o desenvolvimento da aplicação, oferecendo uma visão clara de como a interface deve ser construída e como os usuários irão interagir com ela. Esse alinhamento entre o design e o desenvolvimento é crucial para o sucesso do projeto, garantindo que o produto final seja funcional, eficiente e fácil de usar.
