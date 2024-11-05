---
title: Documentação Final da POC.
sidebar_position: 1
description: Documentação final e atualizada da solução.
---

# Introdução

&emsp;&emsp;Uma **PoC (Proof of Concept)**, ou Prova de Conceito, é uma demonstração prática utilizada para verificar a viabilidade de uma ideia ou solução em um cenário real. No campo da tecnologia, isso geralmente envolve o desenvolvimento de um protótipo simples para mostrar que o conceito proposto pode funcionar.

&emsp;&emsp;A PoC tem um escopo limitado, focando apenas nos aspectos essenciais da ideia, sem a necessidade de construir uma solução completa, tendo como principal objetivo, validar se a ideia pode ser tecnicamente implementada antes de avançar com o desenvolvimento completo.

&emsp;&emsp;Além disso, a PoC também ajuda a identificar desafios ou limitações que podem surgir ao longo do processo, permitindo ajustes necessários antes da implementação final. Em resumo, ela serve para provar que o conceito é viável e funciona, antes de dedicar mais recursos ao projeto.

# Problema

&emsp;&emsp;A Volkswagen percebeu a oportunidade de melhorar significativamente a precisão das inspeções realizadas nos veículos antes de eles avançarem para a fase de rodagem na linha de montagem. Atualmente, o processo de inspeção é abrangente, mas poderia ser otimizado por meio de uma estratégia que permitisse priorizar de maneira mais eficaz os veículos com maior probabilidade de apresentar defeitos. Ao identificar antecipadamente quais veículos têm maior chance de apresentar problemas, a empresa poderia utilizar melhor o tempo e os recursos disponíveis durante os testes, concentrando esforços nos casos mais críticos.

&emsp;&emsp;Essa abordagem mais direcionada e inteligente na fase de inspeção teria um impacto positivo direto na eficiência geral do processo produtivo. Com a capacidade de detectar e resolver problemas de forma mais rápida, seria possível reduzir o retrabalho e as paralisações nas etapas posteriores da fabricação. Além disso, essa otimização contribuiria para um aumento na qualidade final dos veículos, uma vez que os defeitos seriam identificados e corrigidos de maneira mais ágil e eficaz, antes que comprometessem etapas mais avançadas da produção. Em sumo, ao priorizar veículos mais propensos a falhas, a Volkswagen não apenas elevaria o nível de eficiência, mas também garantiria um produto final de maior qualidade.

# Solução

&emsp;&emsp;A solução proposta consiste em um modelo preditivo de classificação com uma acurácia mínima de 95%, projetado para identificar de forma antecipada possíveis defeitos nos veículos durante o processo de montagem. O modelo funciona classificando os veículos em duas categorias, denominadas classe 1 (apresenta falha) e classe 2 (não apresenta falha), o que permite que os analistas da fábrica ajustem o processo de inspeção de maneira mais eficiente, concentrando seus esforços nos veículos que apresentam maior probabilidade de apresentar problemas; essa classificação não só otimiza o uso dos recursos nas inspeções, mas também aumenta a agilidade no processo produtivo, uma vez que os veículos de maior risco podem ser priorizados, reduzindo o tempo gasto em inspeções generalizadas.

&emsp;&emsp;Além disso, o modelo é desenhado para ser escalável, com a capacidade de ser recalibrado mensalmente à medida que novos dados de produção são coletados, permitindo que o sistema se ajuste continuamente às condições reais da fábrica, aprimorando a assertividade das inspeções de forma progressiva. Ademais, esse modelo preditivo traz melhorias contínuas ao processo de inspeção, contribuindo para um aumento na eficiência e na confiabilidade do produto final.

## Entendimento do Negócio

&emsp;&emsp;Primeiramente, antes de dar início ao projeto, o grupo Käfer realizou uma análise de negócios cuidadosa, contendo uma Matriz de Risco com planod e ação, Business Model Canvas e uma Análise Financeira considerando o protótipo e o projeto implementado.

### Matriz de Risco

&emsp;&emsp;A matriz de risco desenvolvida para o projeto da Volkswagen destaca claramente as principais ameaças e oportunidades associadas ao uso de um modelo preditivo para a inspeção de veículos durante o processo de montagem. Por meio dessa análise, foi possível identificar os riscos mais críticos, como a possibilidade de o modelo apresentar acurácia inferior a 95%, a inserção incorreta de novos dados, falhas de adaptação do modelo a mudanças na produção e a limitação de recursos computacionais. Esses fatores podem comprometer a eficácia do processo de predição e a qualidade final dos veículos, exigindo medidas preventivas e planos de ação bem definidos.

&emsp;&emsp;No entanto, a matriz também revela importantes oportunidades, como a redução de custos e tempo nas inspeções, a possibilidade de automatização de relatórios, a geração de insights para a melhoria contínua do processo de fabricação e o aumento da maturidade tecnológica da solução. Com a implementação adequada das estratégias de mitigação dos riscos e aproveitamento das oportunidades, espera-se que o projeto não apenas atenda aos requisitos da Volkswagen, mas também traga avanços significativos na eficiência e qualidade do processo produtivo.

### Business Model Canvas (BMC)

&emsp;&emsp;A elaboração do Business Model Canvas (BMC) para este projeto, embora contextualizada em um cenário acadêmico, foi estruturada como se uma startup estivesse oferecendo essa solução ao mercado. Isso permitiu uma análise estratégica mais ampla, destacando não apenas a proposta de valor, mas também os recursos necessários, as atividades-chave e as fontes de receita. Com base nos nove blocos do BMC, é possível compreender como o projeto pode gerar valor para seus clientes e se posicionar de maneira sustentável no mercado.

&emsp;&emsp;Os **segmentos de clientes** bem identificados — grandes montadoras como Volkswagen, GM e Fiat, e indústrias de eletrodomésticos e pesadas — são atendidos por meio de **canais digitais** eficientes e da participação ativa em eventos do setor, proporcionando ampla visibilidade e networking estratégico. Além disso, o **relacionamento com o cliente** é reforçado por programas de fidelidade e relatórios de desempenho mensais que mostram o valor concreto gerado pela solução.

&emsp;&emsp;Para dar suporte a essa operação, a solução se baseia em uma **infraestrutura tecnológica de alto desempenho**, com recursos de computação em nuvem e machine learning, além de **parcerias principais** com empresas de tecnologia, como a AWS, que garantem a integração contínua com os sistemas de gestão e automação das fábricas. 

&emsp;&emsp;As **atividades chave** do projeto incluem a constante pesquisa e desenvolvimento de novos algoritmos para adaptar o modelo a diferentes linhas de produção e indústrias. Essa inovação contínua é fundamental para manter a competitividade da solução e expandir seu impacto. 

&emsp;&emsp;Em termos financeiros, a solução é sustentada por uma clara **estrutura de custos** focada em despesas operacionais com infraestrutura de TI, pesquisa e marketing, além de investimentos constantes em desenvolvimento. As **fontes de receita**, por sua vez, incluem a venda do modelo preditivo e serviços de pesquisa, desenvolvimento e otimização, garantindo uma entrada de recursos constante e escalável.

**Conclusão Final**:
O BMC desenvolvido para esta solução demonstra sua viabilidade estratégica e operacional. Cada bloco se integra para criar um sistema robusto que, além de entregar um valor claro aos clientes, tem capacidade de sustentar e expandir suas operações. O modelo preditivo para identificação de falhas, inicialmente voltado para o setor automobilístico, oferece uma proposta de valor que pode ser replicada em diversos outros setores industriais, ampliando o impacto da solução. 

&emsp;&emsp;Este projeto, inicialmente focado no setor automobilístico brasileiro, possui uma proposta de valor sólida e bem definida: utilizar um modelo preditivo para identificar falhas na fabricação de veículos. Isso resulta em uma redução significativa de perdas financeiras e de tempo, além de otimizar os processos produtivos. O impacto potencial da solução, ao ser aplicada a outras indústrias como a de bens intermediários e a indústria pesada, abre portas para uma expansão futura, ampliando seu escopo de atuação.

&emsp;&emsp;Com parcerias estratégicas, uma infraestrutura tecnológica sólida e fontes de receita diversificadas, o projeto está bem posicionado para crescer e agregar valor ao mercado, atendendo à demanda por maior eficiência produtiva e redução de perdas. Dessa forma, o BMC não só valida a viabilidade da ideia, mas também aponta para um caminho claro de expansão, inovação contínua e sucesso sustentável.

### Análise Financeira

&emsp;&emsp;A análise financeira do projeto é dividida em duas fases principais: o desenvolvimento do **protótipo** e a implementação do **projeto completo**. A fase do protótipo envolve o levantamento de custos com desenvolvimento de software e infraestrutura em nuvem ao longo de dois meses. Para essa fase, os custos de mão de obra totalizam **R$ 120.930,12**, enquanto os custos de infraestrutura somam **R$ 6.105,76**, levando a um total de **R$ 127.035,88**. Com a adição de margem de lucro (10%) e impostos (18%), o custo final do protótipo chega a **R$ 164.892,57**.

&emsp;&emsp;A fase de **implementação do projeto completo** é estimada para ocorrer em quatro meses, com custos de mão de obra de **R$ 241.860,24**, infraestrutura de **R$ 12.211,52**, e custos adicionais de **R$ 111.500,00**, totalizando **R$ 369.571,76**. Considerando uma margem de lucro de 15% e os impostos, o valor final da implementação é estimado em **R$ 556.944,63**. Ao somar os custos do protótipo e do projeto final, o custo total da solução chega a **R$ 734.540,78**.

&emsp;&emsp;A análise financeira destaca a necessidade de um investimento significativo para o desenvolvimento e implementação do projeto. O protótipo é relativamente acessível, mas a implementação completa envolve custos elevados, principalmente devido à mão de obra e infraestrutura. Ao incorporar uma margem de lucro justa e os impostos, o valor final reflete o retorno financeiro necessário para garantir a viabilidade do projeto. Assim, a análise demonstra a importância de avaliar a viabilidade econômica antes de prosseguir com a implementação em grande escala.

A seção de Requisitos Técnicos é fundamental para o sucesso de qualquer projeto, pois define as especificações necessárias para que o desenvolvimento ocorra de maneira eficiente e alinhada aos objetivos. O propósito desta documentação é detalhar os requisitos técnicos levantados, abordando aspectos cruciais como software, desempenho e outras necessidades técnicas. Com esses requisitos bem definidos, garantimos que todos os envolvidos no projeto tenham uma compreensão clara das expectativas e das metas a serem alcançadas.

### Proposta Geral do Sistema

&emsp;&emsp;Durante a apresentação dos representantes da Volkswagen, parceiros deste projeto, foi levantada a necessidade de inspeções mais assertivas antes do processo de rodagem dos veículos na fábrica. Em resposta a essa demanda, propôs-se o desenvolvimento de um modelo preditivo para classificar os carros com possíveis defeitos nas seguintes categorias: classe 1 e classe 2. O principal objetivo é tornar o processo de inspeção mais eficiente, focando nos problemas mais prováveis, permitindo economizar tempo e reduzir a ocorrência de problemas durante a fase de testes de rodagem.

&emsp;&emsp;A solução, sendo um modelo preditivo com uma acurácia desejada acima de 95%, visa melhorar a eficiência dos testes de rodagem por meio da classificação e identificação prévia de possíveis defeitos durante a montagem. Além disso, o sistema precisa ser escalável, sendo calibrado mensalmente com novos dados de produção para garantir maior assertividade nas inspeções dos veículos.

&emsp;&emsp;O sistema será utilizado por analistas da fábrica para ajustar o processo de inspeção e fornecer uma visualização clara dos resultados do algoritmo. Dessa forma, o motorista inspetor saberá exatamente qual tipo de inspeção é necessária para cada veículo, garantindo uma abordagem mais eficaz na fase de rodagem.

#### Requisitos Funcionais

&emsp;&emsp;Requisitos funcionais são as funcionalidades específicas que o sistema deve proporcionar para atender às operações desejadas. Para este projeto, os seguintes requisitos funcionais foram elaborados:

- **RF1 - Interface Gráfica Simples**: A interface gráfica deve apresentar de maneira clara e objetiva os resultados da classificação do modelo preditivo, facilitando a identificação do tipo de inspeção a ser realizada. Deve incluir um dashboard interativo para a visualização dos resultados e métricas associadas.
  
- **RF2 - Importação de Dados**: O sistema deve suportar a importação de dados a partir de diferentes fontes, como arquivos CSV, XLSX, bancos de dados SQL e APIs, permitindo o re-treinamento do modelo para melhorar a precisão com base em dados atualizados.
  
- **RF3 - Utilização em Cloud**: A aplicação deve ser migrada para a nuvem, utilizando a infraestrutura da AWS, para armazenar o modelo preditivo treinado e realizar o deploy da API do projeto.

- **RF4 - Integração de Tecnologias**: Deve ser estabelecida uma integração entre o modelo de predição, o banco de dados e o sistema de coleta de dados, permitindo um fluxo contínuo de informações entre esses elementos.

- **RF5 - Documentação**: A documentação deve explicar detalhadamente o funcionamento do sistema, as técnicas empregadas no modelo preditivo, os processos de integração e o uso da interface de usuário.

#### Requisitos Não Funcionais

&emsp;&emsp;Os requisitos não funcionais definem as características de qualidade que o sistema deve apresentar. Para este projeto, foram identificados os seguintes requisitos não funcionais:

- **RNF1 - Acurácia do Modelo**: O modelo preditivo deve categorizar corretamente os veículos nas classes 1 e 2, com uma acurácia superior a 95%. O modelo será amplamente testado e ajustado com base nos resultados.

- **RNF2 - Usabilidade da Interface Gráfica**: A interface gráfica deve ser fácil de usar e compreender, permitindo que os operadores identifiquem rapidamente o defeito classificado e o tipo de inspeção necessária. A interface será avaliada pelo número de cliques necessários para realizar uma tarefa (máximo de 3 cliques), e 90% das funcionalidades devem estar disponíveis na tela inicial.

### Estudo de Viabilidade Técnica

&emsp;&emsp;O estudo de viabilidade técnica é uma etapa crucial, especialmente em projetos que envolvem inovação e novas tecnologias. No caso deste projeto, que visa implementar um modelo preditivo para auxiliar na manutenção de veículos da Volkswagen com base nos dados do processo de montagem, o estudo de viabilidade técnica garante que as decisões sejam baseadas em análises cuidadosas.

#### Tecnologia e Ferramentas Disponíveis

- **Modelos de Aprendizado de Máquina**: Estas tecnologias são amplamente usadas na indústria para analisar grandes volumes de dados, identificar padrões complexos e melhorar previsões com novos dados.

- **Serviço de Cloud**: A adoção de uma infraestrutura de cloud, como a AWS, oferece escalabilidade, alta disponibilidade e segurança, além de integrar facilmente outras ferramentas, como APIs e bancos de dados.

- **Interface com FastAPI e React**: A combinação de FastAPI para a criação de APIs robustas e React para interfaces dinâmicas resulta em uma aplicação ágil e escalável.

#### Análise de Dados

&emsp;&emsp;Os dados fornecidos pela Volkswagen foram analisados, e observou-se que muitos carros apresentam algum tipo de defeito durante a montagem. Essa informação orientou o desenvolvimento de um modelo preditivo robusto, que utiliza principalmente dados relacionados ao torque durante a montagem dos carros.

&emsp;&emsp;Foi necessário reunir dados de várias tabelas e organizá-los em um único arquivo para viabilizar a análise. A partir das informações obtidas, foi possível prever a ocorrência de falhas com maior precisão, utilizando as colunas relacionadas ao processo de montagem.

#### Diagrama de Blocos

&emsp;&emsp;A arquitetura da solução é estruturada em três fases: ETL (Extração, Transformação e Carga), Storage e Aprendizado de Máquina. Todo o sistema é hospedado na nuvem, utilizando serviços da AWS. O processo inicia-se na fase de ETL, onde os dados são tratados e separados em conjuntos de treino e teste. Na fase de storage, os dados são armazenados e o modelo é retreinado com novos dados. Na fase de aprendizado de máquina, os dados são utilizados para atualizar o modelo preditivo, que alimenta o backend e fornece informações claras na interface de usuário.

## Modelo Preditivo

&emsp;&emsp;Durante as sprints do projeto, a equipe implementou um modelo preditivo utilizando a metodologia CRISP-DM, que permitiu um ciclo iterativo de desenvolvimento, revisão e aprimoramento contínuo. Na primeira sprint, foi desenvolvido um modelo preditivo com o algoritmo Random Forest, que demonstrou a capacidade de prever falhas na produção de automóveis na fábrica da Volkswagen. Embora o modelo apresentasse um desempenho elevado nas métricas de avaliação, como acurácia e F1-Score, também foi identificado um fenômeno de overfitting, o que indicou a necessidade de ajustes no tratamento de dados e balanceamento.

&emsp;&emsp;Na segunda sprint, a equipe focou na melhoria do modelo, explorando dados adicionais, como estações de montagem e tempos gastos em cada uma delas. Foram removidas duplicatas do dataset e criadas novas colunas que permitiram um entendimento mais aprofundado das informações, como frequência de ocorrências e tempo gasto, além da definição de uma nova coluna para falhas de rodagem. Apesar das melhorias, a equipe percebeu que os dados ainda estavam desbalanceados, indicando a necessidade de mais refinamentos.

&emsp;&emsp;Na terceira sprint, o projeto passou pela fase de dockerização e a configuração de um datalake, que facilitou o armazenamento e a gestão de dados. Essa estrutura foi essencial para a coleta e processamento de informações, garantindo que os dados estivessem organizados e prontos para o treinamento do modelo. A quarta sprint concentrou-se no processo de ETL, onde os dados foram extraídos de arquivos XLSX fornecidos pela empresa parceira, formatados e processados adequadamente para o treinamento do modelo. O fluxo de retrain do modelo foi desenhado com foco nas personas principais, como operadores e engenheiros de dados, utilizando diagramas de blocos para visualizar o processo e facilitar a compreensão.

&emsp;&emsp;Com a conclusão dessas etapas, o projeto avançou significativamente na construção de um sistema preditivo robusto, visando melhorar a precisão das previsões e a segurança dos testes dos automóveis, sendo assim, o modelo está finalizado.

## Backend

&emsp;&emsp;Durante o desenvolvimento do backend, o grupo iniciou a estruturação das rotas essenciais para a comunicação entre o modelo preditivo e a interface do usuário. Optou-se pelo FastAPI devido à sua alta performance, capacidade de utilizar recursos modernos do Python, como tipagem e async/await, e sua documentação intuitiva, que facilita a integração e o uso do serviço por desenvolvedores. O backend foi projetado para receber o KNR como input, permitindo a recuperação de dados associados de um bucket, simulada localmente através de um arquivo Excel.

&emsp;&emsp;A primeira função implementada, buscar_dados_por_knr, busca os dados do KNR fornecido e os formata para entrada no modelo preditivo. Em seguida, a função predict utiliza esses dados para gerar previsões e retornar os resultados ao usuário, tratando exceções com mensagens apropriadas.

&emsp;&emsp;Para organizar o código, adotou-se uma estrutura de controllers e routers no FastAPI, facilitando a manutenção e a escalabilidade do projeto. Além disso, foi criado um banco de dados utilizando PostgreSQL, com a criação de tabelas para armazenar entradas de dados, informações sobre o treinamento do modelo e resultados de análises. O modelo entidade-relacionamento (ER) foi elaborado para visualizar as relações entre as tabelas e suas colunas.

&emsp;&emsp;Na continuação do projeto, novas rotas foram adicionadas ao backend, que agora interage com um banco de dados Supabase. Foram implementadas rotas para inserir registros de treinamento do modelo e para recuperar o histórico de treinamento. O grupo também criou novas rotas para buscar entradas de dados e resultados de análises, permitindo o acesso eficiente às informações armazenadas no Supabase. Essas adições foram fundamentais para melhorar a funcionalidade do sistema e garantir que as informações fossem corretamente geridas e acessadas.

## Frontend

&emsp;&emsp;O desenvolvimento do frontend da aplicação Käfer foi um processo metódico e bem estruturado, com foco na criação de uma interface de usuário intuitiva e eficiente. A partir da elaboração inicial dos wireframes, que proporcionaram uma visão clara da estrutura e do fluxo da aplicação, o grupo avançou para a implementação prática, utilizando tecnologias como TypeScript, Vite e Tailwind CSS. Cada etapa do desenvolvimento foi cuidadosamente planejada e executada, assegurando que o resultado final atendesse aos requisitos funcionais e de usabilidade.

1. **Criação do Wireframe:** O wireframe desempenhou um papel crucial na definição da interface. Ele permitiu identificar e resolver problemas de usabilidade antes do início do desenvolvimento. Com a representação visual das telas, o grupo pôde alinhar expectativas e entender melhor como os usuários interagiriam com a aplicação. As telas desenhadas incluíram a Tela Inicial, que apresenta opções claras de "Executar" e "Treinar", assim como as telas de execução e resultados, proporcionando um fluxo de navegação lógico e eficiente.

2. **Tecnologias Utilizadas:** A escolha de TypeScript trouxe robustez ao desenvolvimento, permitindo a detecção de erros em tempo de compilação e aumentando a confiabilidade do código. Vite, por sua vez, proporcionou um ambiente de desenvolvimento rápido e eficiente, essencial para a construção de aplicações reativas, enquanto Tailwind CSS facilitou a criação de layouts responsivos, permitindo que o grupo se concentrasse mais na experiência do usuário do que na escrita de CSS.

3. **Estrutura do Código:** A estrutura do código foi organizada em componentes React, com um foco especial na interatividade e na gestão de estado. O componente Home, por exemplo, gerencia a navegação entre as páginas de execução e treinamento por meio do useNavigate, enquanto o uso de popups modais enriqueceu a experiência do usuário, permitindo interações mais dinâmicas e informativas.

4. **Fluxo da Aplicação:** O fluxo definido nos wireframes foi seguido rigorosamente, assegurando que os usuários pudessem navegar de forma fluida entre as diferentes funcionalidades da aplicação. Desde a Tela Inicial até os resultados do modelo executado, cada etapa foi projetada para ser clara e intuitiva, facilitando a interação e garantindo que os usuários alcançassem seus objetivos de maneira eficiente.

&emsp;&emsp;Em suma, o desenvolvimento do frontend da aplicação Käfer foi marcado por um forte alinhamento entre design e implementação, resultando em uma interface que não só atende às necessidades dos usuários, mas também reflete as melhores práticas de usabilidade e acessibilidade. O processo integrado de criação e iteração garantiu que a solução final fosse não apenas funcional, mas também agradável de usar, posicionando a aplicação para um sucesso significativo no seu uso prático.

## Deploy da Aplicação na AWS

&emsp;&emsp;Esta documentação tem como objetivo explicar o processo de deploy de um projeto hospedado no GitHub em uma instância EC2 da AWS. Utilizando a infraestrutura da Amazon Web Services (AWS), é possível implementar e gerenciar aplicações na nuvem de maneira escalável e eficiente. A instância EC2 (Elastic Compute Cloud) oferece uma plataforma flexível para a execução de diferentes tipos de aplicações, como Node.js, Python, Docker, entre outras. O processo descrito aqui abrange desde a criação da instância, configuração de servidores web, clonagem do repositório até a execução do projeto utilizando (docker-compose).

&emsp;&emsp;Para realizar o deploy deste projeto, foi necessário ativar uma conta de estudante na AWS e criar uma instância EC2 chamada "projeto-kafer". Nessa instância, foram instalados o `git` e o `docker`. Em seguida, o repositório do projeto foi clonado por meio de uma chave SSH configurada previamente. Após esses passos, o projeto ficou pronto para ser executado com o comando `docker-compose up --build`.

&emsp;&emsp;Dado que, nas últimas sprints, nosso datalake estava hospedado em um supercomputador da faculdade Inteli, não era possível utilizar o `docker-compose` anterior, pois a rede é diferente quando o projeto está sendo executado em uma instância AWS. Por esse motivo, foi necessário criar uma nova imagem, que permitisse a criação do datalake na mesma instância que executa o projeto. As alterações foram feitas para que todo o projeto pudesse ser executado apenas por meio do `docker-compose`.

&emsp;&emsp;As instâncias EC2 da AWS são configuradas com um endereço IP público dinâmico, o que significa que o IP pode mudar sempre que a instância for reiniciada. Para garantir que o IP da instância permaneça o mesmo, evitando a necessidade de atualizar configurações após cada reinicialização, é necessário associar um Endereço IP Elástico. Esse recurso oferece um IP estático que pode ser vinculado à instância EC2 em execução, garantindo que o IP público seja constante e facilitando o acesso contínuo ao projeto implantado, mesmo após reinicializações ou alterações na instância. No caso deste projeto, o IP público fixo é 44.208.228.224, e o frontend pode ser acessado através da porta 7000, o health check pela porta 8009, e o backend pela porta 8000.

&emsp;&emsp;O processo de deploy de uma aplicação hospedada no GitHub para uma instância EC2 da AWS oferece uma solução poderosa e flexível para a execução de projetos na nuvem. Com a configuração adequada, foi possível garantir que a aplicação esteja sempre disponível, com um IP estático e acesso simplificado. A integração do `docker-compose` facilita a execução e manutenção do projeto, enquanto a infraestrutura da AWS oferece escalabilidade e confiabilidade.

## Proposta de Implementação de Testes

&emsp;&emsp;O projeto possui um **frontend** que permite o upload de arquivos de dados. Esses arquivos são processados por um fluxo **ETL** (Extrair, Transformar, Carregar) e enviados para um **backend** que utiliza um modelo de **machine learning** para realizar previsões ou avaliações com base nos dados.

### Tecnologias utilizadas no projeto:
- Frontend: Desenvolvido em Vite.
- Backend: Desenvolvido em FastAPI.
- Modelo: Atualmente, o modelo utilisado é o LSTM.
- Processo ETL: Responsável por transformar e preparar os dados antes de enviá-los ao backend.
- Docker: imagens individuais para o frontend, backend, datalake e health check.

## Testes propostos
### 1. Testes de Upload de Arquivo
#### Teste 1.1: Upload de Arquivo Válido
- **Cenário**: O usuário faz upload de um arquivo com dados formatados corretamente.
- **Passos**:
  1. O usuário faz upload de um arquivo no formato XLSX.
  2. O frontend envia o arquivo para o backend via uma requisição.
  3. O backend aceita o arquivo e inicia o processamento.

- **Resultado Esperado**: O backend retorna um status de sucesso (`200 OK`) e confirma o início do processamento dos dados.

#### Teste 1.2: Upload de Arquivo Inválido
- **Cenário**: O usuário tenta enviar um arquivo inválido (formato não suportado ou arquivo corrompido).

- **Passos**:
  1. O usuário faz upload de um arquivo inválido.
  2. O frontend envia o arquivo para o backend.
  3. O backend rejeita o arquivo.

- **Resultado Esperado**: O backend retorna um status de erro (`400`) com uma mensagem explicando o motivo da rejeição.

### 2. Testes de Processamento de Dados (ETL)

#### Teste 2.1: Dados Válidos e Formatados
- **Cenário**: O arquivo contém dados corretamente formatados, prontos para processamento.
- **Passos**:
  1. O processo ETL extrai, transforma e carrega os dados conforme esperado.
  2. Verificar que os dados estejam prontos para serem enviados ao backend.
- **Resultado Esperado**: O ETL processa e formata os dados corretamente, garantindo que o formato de saída seja adequado para o backend.
#### Teste 2.2: Dados com Problemas
- **Cenário**: O arquivo contém dados inconsistentes ou incompletos.
- **Passos**:
  1. O ETL processa os dados e lida com valores inconsistentes ou faltantes.
  2. Avaliar o tratamento de erros durante o processo de transformação.
- **Resultado Esperado**: O processo ETL detecta e trata as inconsistências (valores nulos, dados fora de intervalo) ou retorna um erro adequado.
### 3. Testes de Previsão/Processamento de Dados (Modelo de Machine Learning)
#### Teste 3.1: Resultado Positivo
- **Cenário**: Os dados indicam um resultado positivo para a previsão ou avaliação.
- **Passos**:
  1. O backend processa os dados enviados pelo ETL e passa para o modelo de machine learning.
  2. O modelo faz uma previsão ou avaliação correta.
- **Resultado Esperado**: O backend retorna um resultado (previsão de falha ou detecção de anomalia).
#### Teste 3.2: Resultado Negativo
- **Cenário**: Os dados indicam um resultado negativo.
- **Passos**:
  1. O backend processa os dados enviados pelo ETL e passa para o modelo de machine learning.
  2. O modelo faz uma previsão ou avaliação negativa.
- **Resultado Esperado**: O backend retorna um resultado negativo (ausência de falha ou comportamento normal).
### 4. Testes de API
#### Teste 4.1: Validação de Resposta do backend
- **Cenário**: O frontend envia uma requisição para o backend com os dados processados.
- **Passos**:
  1. O frontend faz uma requisição `POST` ou `GET` para o backend.
  2. O backend responde com sucesso ou erro, dependendo da entrada.
- **Resultado Esperado**: A API retorna respostas apropriadas (`200 OK` para sucesso ou `400` para erros).
#### Teste 4.2: Tempo de Resposta da API
- **Cenário**: Avaliar o tempo de resposta da API para garantir que o desempenho esteja dentro dos limites aceitáveis.
- **Passos**:
  1. Enviar requisições repetidas para a API e medir o tempo de resposta.
- **Resultado Esperado**: O tempo de resposta deve ser inferior a um limite aceitável (2 segundos para operações simples).
### 5. Testes de Frontend
#### Teste 5.1: Exibição Correta dos Resultados
- **Cenário**: O frontend deve exibir o resultado do processamento dos dados corretamente para o usuário.
- **Passos**:
  1. O usuário faz upload de um arquivo de dados.
  2. O backend processa os dados e retorna o resultado para o frontend.
  3. O frontend exibe o resultado da avaliação para o usuário.
- **Resultado Esperado**: O frontend exibe corretamente os resultados da previsão ou avaliação (mensagem de falha detectada ou operação normal).

# Conclusão

&emsp;&emsp;O modelo de machine learning desenvolvido para a identificação de defeitos em veículos da Volkswagen representa um avanço significativo na indústria automotiva. Com uma precisão de 0.77 e um recall de 1.00, o modelo demonstrou sua capacidade de detectar de forma eficaz problemas que poderiam comprometer a qualidade dos produtos finais. Isso significa que, quando o modelo identifica um defeito, ele está certo 77% das vezes e que ele identifica todos os defeitos presentes nos dados. A solução, que combina um pipeline de dados robusto, um modelo de machine learning sofisticado e uma infraestrutura escalável, oferece um grande potencial para a otimização dos processos de produção e a melhoria da experiência do cliente.

&emsp;&emsp;Além dos benefícios diretos para a Volkswagen, essa solução abre caminho para diversas outras aplicações em diferentes setores. A capacidade de identificar padrões e anomalias em grandes conjuntos de dados pode ser utilizada para otimizar processos, prever falhas em equipamentos, personalizar produtos e desenvolver novas soluções inovadoras. A implementação bem-sucedida deste projeto demonstra o poder da inteligência artificial em transformar a indústria e impulsionar a competitividade das empresas..

&emsp;&emsp;Para o futuro, vislumbra-se a expansão dessa solução para outras áreas da fábrica, a integração com sistemas de gestão mais amplos e a exploração de técnicas de aprendizado de máquina mais avançadas. A coleta contínua de dados e o monitoramento do desempenho do modelo são essenciais para garantir sua longevidade e adaptabilidade a um ambiente em constante evolução.





