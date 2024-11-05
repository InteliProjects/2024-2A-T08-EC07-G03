# Guia de Execução do Projeto

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em seu ambiente:

- **Python 3.8+**
- **pip** (gerenciador de pacotes Python)
- **virtualenv** (opcional, mas recomendado para criar um ambiente isolado)
- **git** (para clonar o repositório, se necessário)

## Passos para Configuração

1. **Clone o Repositório** (se aplicável):

   Se você ainda não clonou o repositório, faça isso utilizando o comando:

   ```bash
   git clone https://github.com/Inteli-College/2024-2A-T08-EC07-G03.git
   cd 2024-2A-T08-EC07-G03
   cd src/backend
   ```

2. **Crie e Ative um Ambiente Virtual** (opcional, mas recomendado):

   Para manter as dependências do projeto isoladas, crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/MacOS
   venv\Scripts\activate  # Para Windows
   ```

3. **Instale as Dependências**:

   Instale as dependências do projeto listadas no arquivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o Servidor**:

   Para iniciar o servidor FastAPI, execute o seguinte comando na raiz do projeto:

   ```bash
   uvicorn src.backend.app:app --reload
   ```

   Este comando inicializará o servidor em modo de desenvolvimento, permitindo que você veja mudanças em tempo real.

5. **Acesse a API**:

   Após iniciar o servidor, você pode acessar a documentação interativa da API em:

   ```
   http://127.0.0.1:8000/docs
   ```

   Nesta página, você pode explorar e testar os endpoints disponíveis.
