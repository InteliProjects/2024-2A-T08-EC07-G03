# Banco de Dados

## Introdução

&emsp;&emsp;Para armazenar os dados presentes no sistema, é fundamental a criação de um banco de dados para essa função. Por isso, ele é considerado uma das partes mais importantes do Backend de um sistema.

&emsp;&emsp;Seguindo todo o contexto do projeto, o banco de dados foi criado utilizando a ferramenta PostgreSQL.

## PostgreSQL

&emsp;&emsp;O PostgreSQL é um gerenciador de banco de dados que permite a criação tanto de um banco de dados quanto de aspectos que envolvem todo esse sistema, como a criação do SQL, diagramas como o entidade-relacionamento, entre outros.

&emsp;&emsp;Por conta dessas características, esta ferramenta foi utilizada para a criação do banco de dados do projeto para esta Sprint 2.

## SQL

&emsp;&emsp;A partir da ferramenta supracitada, o grupo Käfer criou o primeiro banco de dados do projeto. Foram criadas tanto tabelas quanto colunas, que foram pensadas para armazenar informações seguindo todo o contexto do projeto. Toda essa estrutura pode ser vista nos códigos a seguir, que contemplam toda a criação das tabelas do banco de dados:

### Tabelas existentes:

#### Tabela `data_entries`:

```sql
CREATE TABLE IF NOT EXISTS public.data_entries(
    id serial NOT NULL,
    feature_1 double precision NOT NULL,
    feature_2 double precision NOT NULL,
    feature_3 double precision NOT NULL,
    date timestamp without time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT data_entries_pkey PRIMARY KEY (id)
);
```

&emsp;&emsp;Esta tabela armazena todas as entradas de dados feitas pelo usuário. Esta tabela é importante para armazenar alguns inputs presentes nos dados, como KNR, data e outros.

#### Tabela `model_training`:

```sql
CREATE TABLE IF NOT EXISTS public.model_training(
    id serial NOT NULL,
    model_name text COLLATE pg_catalog."default" NOT NULL,
    training_accuracy double precision NOT NULL,
    date timestamp without time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT model_training_pkey PRIMARY KEY (id)
);
```

&emsp;&emsp;Já esta tabela guarda as informações sobre as sessões de treinamento de modelos. Como pode ser visto na documentação dos wireframes da solução, há uma tela de treinamento de modelo, em que os dados são treinados para depois serem usados para exibir resultados. Assim, é importante ter uma tabela para armazenar essas informações de treino.

#### Tabela `analysis_results`:

```sql
CREATE TABLE IF NOT EXISTS public.analysis_results(
    id serial NOT NULL,
    data_entry_id integer NOT NULL,
    result_value double precision NOT NULL,
    date timestamp without time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT analysis_results_pkey PRIMARY KEY (id)
);
```

&emsp;&emsp;A terceira tabela armazena os resultados das predições do modelo, em que cada resultado é vinculado a uma entrada específica.

## Diagrama Entidade-Relacionamento (ER)

&emsp;&emsp;Um modelo entidade-relacionamento é um modelo de dados para descrever os dados ou aspectos de informação de um domínio de negócio ou seus requisitos de processo.

&emsp;&emsp;Com isso, um diagrama foi criado para exibir o banco de dados do sistema deste projeto. Ele pode ser visto na seguinte imagem:

<p align="center"><b> Figura 1 - Diagrama Entidade-Relacionamento</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/erd.png').default} alt="Diagrama ER"/>
  <p><b>Fonte:</b> Elaborado pelo Grupo 3</p>
</div>


&emsp;&emsp;A partir deste diagrama, feito com a ferramenta ERD Database do PostgreSQL, é possível visualizar as tabelas e as colunas presentes no banco de dados. Para ver o arquivo deste diagrama, ele esta localizado na pasta backend deste repositório.

&emsp;&emsp;Vale ressaltar que, nesta etapa do projeto, ainda não foi considerada a implementação de uma tela de login, o que deverá ser feito em alguma Sprint posterior. Então, é provável que o banco de dados seja atualizado para as próximas sprints.

&emsp;&emsp;Outro fator que reflete na situação do banco de dados para as próximas sprints, principalmente para a Sprint 3, é o desenvolvimento do datalake e da dockerização do sistema, pois, nesta sprint, essas tecnologias serão abordadas, o que poderá resultar em mudanças no banco de dados.