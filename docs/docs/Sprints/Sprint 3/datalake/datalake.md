### Data Lake para Armazenamento de Dados de Treinamento e Modelos com GridFS

#### **Contexto Geral**

O foco do data lake é fornecer uma solução eficiente para armazenar grandes volumes de **dados de treinamento** e **modelos treinados**, permitindo sua recuperação e reutilização conforme necessário dentro do escopo do projeto.

Além do armazenamento de dados, o projeto prevê **estratégias de backup** para garantir a segurança e a disponibilidade dos dados. O data lake não é um projeto isolado, mas sim uma peça crítica dentro de uma arquitetura mais ampla, que envolve outras ferramentas e serviços para manipulação e análise de dados de machine learning.

#### **Objetivo Específico do Data Lake**

O data lake foi criado para resolver os seguintes desafios dentro do projeto:

1. **Armazenamento de grandes volumes de dados**: Os modelos de machine learning dependem de conjuntos de dados robustos e volumosos, que precisam ser armazenados de maneira eficiente e escalável.
2. **Armazenamento dos modelos de aprendizado de máquina**: Depois que os modelos são treinados, eles são armazenados para serem reutilizados ou avaliados posteriormente.
3. **Planos de backup**: Garantir a segurança e a disponibilidade dos dados armazenados através de backups regulares, evitando perdas devido a falhas no sistema ou problemas de integridade dos dados.

#### **Descrição Técnica**

##### **1. MongoDB e GridFS**

Dentro do projeto, o **MongoDB** é utilizado para armazenar dados não estruturados e semiestruturados, aproveitando a flexibilidade desse banco de dados NoSQL. O **GridFS** é uma extensão do MongoDB que permite o armazenamento de arquivos que excedem o limite de 16 MB dos documentos BSON tradicionais.

- **GridFS** armazena os arquivos em duas coleções principais:
  - **fs.files**: Contém metadados, como o nome, tamanho e data de upload.
  - **fs.chunks**: Armazena os dados reais dos arquivos divididos em pedaços menores, facilitando o gerenciamento de grandes arquivos de dados de treinamento e modelos de machine learning.

##### **2. Hospedagem no Servidor**

O data lake está sendo **hospedado em um servidor dedicado**, que faz parte da infraestrutura maior do projeto. Este servidor permite a acessibilidade dentro da rede local, possibilitando que outras máquinas no ambiente de desenvolvimento, ou de produção, acessem o repositório central de dados e modelos.

Para verificar se o MongoDB está rodando corretamente no servidor, o comando a ser utilizado é:

```bash
sudo systemctl status mongod
```

Este comando verifica o status do serviço do MongoDB, indicando se ele está **ativo** e funcionando corretamente.

##### **3. Fluxo de Operação**

Dentro do projeto, o data lake opera da seguinte forma:

1. **Upload de arquivos de dados de treinamento**: Conjuntos de dados massivos são carregados para o GridFS, onde são automaticamente divididos e armazenados em chunks.
2. **Armazenamento dos modelos treinados**: Após o treinamento, os modelos de machine learning são enviados para o data lake para serem armazenados e reutilizados.
3. **Recuperação dos dados e modelos**: Quando necessário, os arquivos armazenados podem ser recuperados pelo GridFS, reconstruindo-os a partir dos chunks armazenados.

#### **Planos de Expansão**

Como parte do projeto maior, o data lake está planejado para crescer e incluir:

- **Versionamento de dados e modelos**, facilitando o rastreamento de diferentes versões de dados de treinamento e de modelos de machine learning.
- **Automatização de backups**, com verificações periódicas de integridade para garantir que os dados armazenados estão consistentes e seguros.
