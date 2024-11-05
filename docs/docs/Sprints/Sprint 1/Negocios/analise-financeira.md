---
title: Análise Financeira
sidebar_position: 1
description : Apresentação da análise financeira do projeto
---

# Análise Financeira

## Introdução

Esta seção aborda a análise financeira do protótipo e do projeto implantado. Será detalhado os custos relacionados à produção, desde os custos com desenvolvedores até os impostos aplicados sobre o projeto. A principal finalidade desse documento é apresentar, de forma clara, os recursos financeiros necessários para avaliar a viabilidade do projeto antes de avançar para a fase de implementação em grande escala.

## Levantamento de custos

Para auxiliar na identificação e estimativa dos custos envolvidos no projeto, a análise foi dividida em duas seções distintas: Protótipo e Projeto Implementado. Cada seção aborda os custos específicos relacionados às diferentes fases do projeto, garantindo uma compreensão clara e detalhada dos investimentos necessários.

## Protótipo

Para realizar essa análise, o período de tempo de dois meses será considerado o período de tempo necessário para desenvolver o protótipo. Sendo assim, os custos serão divididos entre desenvolvedores e o custo da infraestrutura necessária para manter a solução na nuvem (Cloud) durante dois meses.

### Desenvolvimento de Software: custo médio de mão de obra

| *Função* | *Quantidade* | *Meses* | *Salário Mensal (média)* | *Valor Final* |
| ----------| ------- | ------- | ----- | ------ |
| Engenheiro de Software | 2 | 2 | R$ 13.885,61 | R$ 55.542,44 |
| Cientista de Dados | 2 | 2 | R$ 9.009,92 | R$ 36.039,68 |
| Engenheiro de DevOps | 2 | 2 | R$ 8.371 | R$ 16.742 |
| Gestor de Projeto | 1 | 2 | R$ 6.303 | R$ 12.606 |
| Total | | | | **R$ 120.930,12** |

### Custo da nuvem (Cloud)

A fim de estimar os custos da infraestrutura em nuvem para o protótipo inicial, uma pesquisa foi feita e foi considerado os seguintes aspectos, tendo como referência um escopo de 2 meses:

| *Serviço* | *Quantidade* | *Valor/Mês* | *Valor Final |
| ----------| ------- | ------- | ----- |
| Computação| 2 instâncias de máquinas virtuais com 4 vCPUs e 16 GB de RAM | R$ 0,55 por hora x 2 instâncias x 160 horas = R$ 1.760,00 | R$ 3.520,00 |
| Armazenamento | 400 GB de armazenamento em SSD | R$ 0,30 por GB x 400 GB = R$ 120,00 | RR$ 240,00 |
| Rede | 1 TB de transferência de dados | R$ 0,10 por GB x 1.024 GB = R$ 102,40 | R$ 245,76 |
| Monitoramento e Logs | Cloud Monitor | R$ 150,00 | R$ 300,00 |
| Banco de Dados | Backup automático dos dados | R$ 120,00 | R$ 240,00 |
| Segurança | Configuração de VPC e firewall | R$ 60,00 | R$ 120,00 |
| Total | | R$ 3.052,88 | R$ 6.105,76 |

Detalhes dos serviços:
- Computação: refere-se a máquinas virtuais para execução de algoritmos preditivos e processos críticos.
- Armazenamento: SSD para dados críticos e backups de modelos
- Rede: transferência de dados para comunicação entre sistemas e usuários
- Monitoramento e Logs: uso de um serviço de monitoramento contínuo do desempenho e análise de logs, como Cloud Monitor
- Banco de Dados: banco de dados relacional para armazenar resultados e histórico das operações
- Balanceamento de Carga: ferramenta para distribuir o tráfego entre as instâncias, essencial para garantir eficiência e prevenir sobrecarga
- Backup: solução de backup automatizado para garantir a integridade dos dados.
- Segurança: serviço de firewall e rede privada virtual (VPC) para proteger os recursos, incluindo configurações de segurança para proteger os dados sensíveis

### Custo total do prótipo

Soma dos custos finais do protótipo:

| *Descrição* | Valor |
| ----------- | ----- |
| Custos relacionados com a mão de obra | R$ 120.930,12 |
| Custos relacionados a infraestrutura | R$ 6.105,76 |
| Custo total para implementação | **R$ 127.035,88**|

### Valor final: Margem de Lucro + Importo da Nota Fiscal

Para calcular a margem de lucro, considera-se que pode variar, frequentemente ficando entre 10% e 20%. Considerando que um protótipo de um sistema de manutenção preditiva utilizando IA e com arquitetura em nuvem, o custo tende a ser caro, portanto é recomendado evitar a cobrança de um valor muito alto, então, calcula-se a margem de lucro tendo 10% como taxa mínima.

Ademais, é importante considerar os impostos de emissão da Nota Fiscal (NF) - no Brasil representa 18% do valor total do produto ou serviço. Sendo um imposto obrigatório, ele deve ser incluído para calcular o valor final, garantindo conformidade fiscal.

Para calcular o imposto, foi aplicado o método conhecido como "Por Dentro". Esse método incorpora o valor do imposto diretamente no preço do produto ou serviço, resultando em um aumento tanto na alíquota efetiva quanto no preço final.

| *Descrição* | *+ Lucro (10%) | Impostos de emissão da NF (18%) |
| ------- | ------ | ----- |
| Custos de implementação do protótipo | R$ 12.703,58 | R$ 139.739,46 | R$ 25.153,10 | **R$ 164.892,57** |

> Para mais informações sobre o método "Por dentro", [clique aqui](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://emiteai.com.br/calculo-imposto-por-dentro/&ved=2ahUKEwiDibLt7PeHAxV7ppUCHUGmNtgQFnoECBsQAw&usg=AOvVaw10cIUVzT_62bzr5Fspk2a-).

## Projeto implementado

Para efetuar os cálculos e a estimativa do projeto implementado após a validação do protótipo, considera-se os mesmos serviços e valores médios. Foi estimado um tempo de seis meses para desenvolvimento e implementação do projeto final, dividindo os custos, novamente, entre desenvolvedores e infraestrutura, além de custos adicionais para esta etapa do projeto. Vale ressaltar que os primeiros dois meses do projeto são destinados a criação e avaliação do protótipo.

### Desenvolvimento de Software: Custo médio da mão de obra

| *Função* | *Quantidade* | *Meses* | *Salário Mensal (média)* | *Valor Final* |
| ----------| ------- | ------- | ----- | ------ |
| Engenheiro de Software | 2 | 4 | R$ 13.885,61 | R$ 111.084,88 |
| Cientista de Dados | 2 | 4 | R$ 9.009,92 | R$ 72.079,36 |
| Engenheiro de DevOps | 2 | 4 | R$ 8.371 | R$ 33.484 |
| Gestor de Projeto | 1 | 4 | R$ 6.303 | R$ 25.212 |
| Total | | | | **R$ 241.860,24** |

### Custos da infraestrutura em Cloud

| *Serviço* | *Quantidade* | *Valor/Mês* | *Valor Final |
| ----------| ------- | ------- | ----- |
| Computação| 2 instâncias de máquinas virtuais com 4 vCPUs e 16 GB de RAM | R$ 0,55 por hora x 2 instâncias x 160 horas = R$ 1.760,00 | R$ 7.040,00 |
| Armazenamento | 400 GB de armazenamento em SSD | R$ 0,30 por GB x 400 GB = R$ 120,00 | R$ 480,00 |
| Rede | 1 TB de transferência de dados | R$ 0,10 por GB x 1.024 GB = R$ 102,40 | R$ 491,52 |
| Monitoramento e Logs | Cloud Monitor | R$ 150,00 | R$ 600,00 |
| Banco de Dados | Backup automático dos dados | R$ 120,00 | R$ 2.400,00 |
| Balanceamento de Dados | Load Balancer para distribuir o tráfego | R$ 120,00 | R$ 480,00 |
| Backup | Backup automático dos dados | R$ 120,00 | R$ 480,00 |
| Segurança | Configuração de VPC e firewall | R$ 60,00 | R$ 240,00 |
| Total | | **R$ 6.105,76** | **R$ 12.211,52** |

### Custos adicionais

Após a fase inicial de implementação do protótipo, durante a finalização, terá custos adicionais. A seguir, alguns dos custos foram estimados seguindo a expectativa para a segunda fase de implementação, vale ressaltar que os custos adicionais não são fixos, sendo vulneráveis a alterações, tanto dos itens da descrição quanto a estimativa de custo.

| *Descrição* | *Estimativa de Custo |
| --------- | -------- |
| Testes em larga escala | ~ R$ 34.500,00 |
| Manutenção Contínua | ~ R$ 13.000,00 |
| Suporte Pós-Implementação | ~ R$ 68.000,00 |
| **Total** | **~ R$ 111.500,00** |

> Os custos foram estimados com base na ferramenta de calculadora da AWS. Fontes presentes na última seção.

### Custo total do restante da implementação do projeto

Abaixo está o valor total incluindo o custo da mão de obra, infraestrutura e custos adicionais, considerando os quatro meses restantes do desenvolvimento.

| *Descrição* | *Estimativa de Custo |
| --------- | -------- |
| Custos relacionados a mão de obra| R$ 241.860,24 |
| Custos relacionados a infraestrutura | R$ 12.211,52 |
| Custos adicionais | ~ R$ 111.500,00 |
| **Total** | **R$ ~369.571,76** |

### Valor final: Margem de Lucro + Imposto da Nota Fiscal

Ao calcular o valor final do projeto implementado considera-se três âmbitos:

1. Calcular o lucro

2. Calcular o lucro adicionando os impostos sobre a implementação durante a segunda fase do projeto - duração de 04 meses.

3. Por último, fase do protótipo + fase final da implementação.

Facilitando, assim, a visualização das fases e custos da implementação da solução toda.

Para calcular a margem de lucro, foi considerado a média entre 10% e 20% - 15% - considerando que o parceiro optou por seguir com o restante do projeto após a fase do protótipo, a margem de lucro foi ampliada para garantir um retorno adequado. Ademais, se torna necessário considerar os impostos de emissão da nota fiscal - que, no Brasil, representa cerca de 18% do valor final.

| *Descrição* | *+ Lucro* | *Custos + Lucro* | *Emissão da NF (18%)* | *Valor Final* |
| -------- | ------- | ------- | ------- | ------ |
| Custos de implementação do protótipo | R$ 12.703,58 (10%) | R$ 12.703,58 (10%) | R$ 25.153,10 | R$ 164.892,57 |
| Custo de implementação da 2° fase | R$ 55.435,76 (15%) | R$ 425.007,52 | R$ 76.501,35 | $ 556.944,63 |
| Custos de implementação total da solução | R$ 68.139,34 | R$ 564.746,99 | R$ 101.654,45 | R$ **734.540,78** | 

## Fontes de Receita

Dado o projeto, algumas possíveis fontes de receita podem incluir:

### Licenciamento de Software

Refere-se a cobrar uma taxa de licenciamento pelo uso do sistema de inspeção preditivo desenvolvido. A Volkswagen pagaria uma taxa mensal ou anual para usar o software, garantindo atualizações e suporte técnico, sendo assim, a receita é baseada em assinaturas.

### Consultoria e Customização

Trata-se de cobrar pela personalização e adaptação do sistema às necessidades específicas da Volkswagen. Então a receita seria baseada em projetos, com cobrança por horas de consultoria ou taxa fixa para personalizações específicas.

### Atualizações e Retreinamento do Modelo:

A receita seria baseada em contratos de atualização regulares, manutenção e retreino do modelo preditivo com novos dados fornecidos, garantindo a alta acurácia ao longo do tempo.

## Proposta de Valor

A proposta de valor da solução, que utiliza um modelo preditivo para classificar veículos quanto a possíveis falhas de fabricação, está diretamente ligada à análise financeira do projeto. A identificação antecipada de defeitos reduz o desperdício de recursos e tempo na produção, o que se traduz em uma significativa redução de custos operacionais. Essas economias, decorrentes da menor necessidade de retrabalho, sucata e tempo de inatividade, melhoram diretamente as margens de lucro.

Além disso, a eficiência do processo de inspeção proporcionada pelo modelo preditivo aumenta a produtividade e reduz o tempo de ciclo, permitindo maior capacidade de produção e, consequentemente, um impacto positivo na receita. Também, a possibilidade de adaptar a solução para outros setores, como a indústria pesada e de eletrodomésticos, expande o mercado potencial, gerando novas oportunidades de receita e crescimento.

Finalmente, ao melhorar a qualidade do produto final por meio da identificação precoce de defeitos, a solução contribui para a redução de devoluções, menor necessidade de garantias e maior satisfação dos clientes, fatores que podem resultar em um aumento nas vendas e na fidelização dos clientes. Dessa forma, a proposta de valor não apenas agrega benefícios operacionais, mas também se traduz em resultados financeiros sólidos, justificando o investimento e demonstrando o potencial de retorno financeiro do projeto.

## Análise de Viabilidade Financeira 

A viabilidade financeira do projeto pode ser avaliada com base nos custos de implementação, projeções de receitas e os benefícios econômicos esperados. O custo mensal total para a infraestrutura em cloud é de R$5.054,80, cobrindo aspectos como computação, armazenamento, rede, monitoramento, logs e banco de dados. Além disso, deve-se considerar despesas adicionais, como manutenção, suporte técnico e eventuais atualizações do sistema, que podem impactar o custo final do projeto.

O principal retorno financeiro do projeto advém da economia gerada pela maior eficiência na linha de produção, estimada em até 10% dos custos operacionais. A solução não apenas reduz custos com retrabalho e desperdício, mas também aumenta a produtividade, permitindo que mais veículos sejam inspecionados em menos tempo. Também, a adaptabilidade da solução para setores como a indústria pesada e de eletrodomésticos amplia o mercado-alvo, criando novas oportunidades de receita.

Com base nessas estimativas, o retorno sobre o investimento (ROI) do projeto é altamente positivo. Se a economia operacional for de, por exemplo, R$ 50.000,00 por mês, o investimento inicial seria recuperado rapidamente, gerando lucro em pouco tempo. No longo prazo, a capacidade de retreinar o modelo com novos dados e expandir para outros setores garante a sustentabilidade econômica do projeto, tornando-o financeiramente viável e potencialmente lucrativo.

## Conclusão

O projeto proposto demonstra um potencial significativo para transformar o processo de inspeção de veículos na indústria automobilística através da implementação de um modelo preditivo avançado. A proposta de valor, que visa identificar antecipadamente possíveis falhas de fabricação e reduzir desperdícios e tempo de produção, está alinhada com as necessidades identificadas e promete trazer benefícios substanciais tanto em termos de eficiência operacional quanto de redução de custos.

Os requisitos técnicos e funcionais detalhados - presentes em outra seção da documentação - asseguram que a solução será robusta e capaz de atender às exigências da Volkswagen e de outros setores potenciais. A integração de tecnologias modernas, como a infraestrutura em cloud e a capacidade de adaptação a diferentes setores, fortalece a viabilidade e escalabilidade do sistema. A análise financeira revela que o projeto é economicamente viável, com um retorno sobre o investimento favorável baseado nas economias esperadas e na expansão de mercado.

Em resumo, a implementação do modelo preditivo não só atende às expectativas de eficiência e precisão na identificação de defeitos, mas também apresenta uma sólida base financeira que garante a recuperação do investimento e a geração de lucro. A combinação de um modelo bem projetado, a adaptação para novos mercados e uma estrutura de custos bem definida posiciona o projeto como uma solução promissora e valiosa para a indústria, com potencial para expandir seu impacto e trazer melhorias significativas ao processo de produção.

### Fontes:

- https://www.salario.com.br/tabela-salarial/

- https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.glassdoor.com.br/Sal%25C3%25A1rios/engenheiro-devops-sal%25C3%25A1rio-SRCH_KO0,17.htm&ved=2ahUKEwiXhpfro_OHAxWOpJUCHfrVN1UQFnoECBUQAQ&usg=AOvVaw1taVxj_R4Uk3n5cFCTBVWv 

- https://www.glassdoor.com.br/Sal%C3%A1rios/gestor-de-projetos-sal%C3%A1rio-SRCH_KO0,18.htm 

- https://calculator.aws/#/addService 

- https://www.capterra.com/resources/roi-accounting-software/ 

- "Principles of Corporate Finance" por Richard A. Brealey, Stewart C. Myers, e Franklin Allen 

- "Cloud Economics: How to Evaluate the Financial Benefits of Cloud Computing" por Amazon Web Services (AWS) 
