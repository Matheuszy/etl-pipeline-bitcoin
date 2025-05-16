## Pré-requisitos

Antes de executar o projeto, você precisará ter o seguinte instalado:

* **Python 3.7 ou superior:** A linguagem de programação utilizada.
* **pip:** O gerenciador de pacotes do Python.
* **PostgreSQL:** O banco de dados para armazenar os dados do Bitcoin. Certifique-se de ter um servidor PostgreSQL rodando e as credenciais de acesso configuradas.
* **Conta na Coinbase (opcional):** Para acessar a API de preços (embora seja pública e não requeira autenticação para este endpoint).
* **Conta na Groq (opcional):** Para utilizar o modelo de linguagem `llama-3.3-70b-versatile` com a biblioteca Agno. Você precisará configurar as credenciais no seu ambiente.

## Configuração

1.  **Clone o repositório:**
    ```bash
    
    ```

2.  **Crie e configure o arquivo `.env`:**
    Crie um arquivo `.env` na raiz do projeto e adicione a URL de conexão do seu banco de dados PostgreSQL. Exemplo:
    ```
    DATA_BASE_URL="postgresql://usuario:senha@host:porta/nome_do_banco"
    ```
    Substitua `usuario`, `senha`, `host`, `porta` e `nome_do_banco` pelas suas informações de conexão.

3.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # No macOS e Linux
    venv\Scripts\activate.bat  # No Windows
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure o banco de dados:**
    Certifique-se de que o banco de dados especificado na `DATA_BASE_URL` existe e que as credenciais estão corretas. O script `data_ingestion/load.py` irá criar a tabela `bitcoin_dados` se ela não existir.

## Execução

1.  **Execute o pipeline de dados:**
    Abra um terminal e navegue até a pasta raiz do projeto (`cripto_dashboard`). Execute o seguinte comando para iniciar a coleta e o armazenamento dos dados:
    ```bash
    python pipeline.py
    ```
    Este script rodará continuamente, coletando dados a cada 15 segundos. Mantenha este terminal aberto.

2.  **Execute o dashboard Streamlit:**
    Abra um novo terminal, navegue até a pasta `dashboard`:
    ```bash
    cd dashboard
    ```
    E execute o aplicativo Streamlit:
    ```bash
    streamlit run app.py
    ```
    O dashboard será aberto automaticamente no seu navegador web.

3.  **Execute o agente inteligente:**
    Abra um novo terminal, navegue até a pasta `agent`:
    ```bash
    cd agent
    ```
    E execute o script do agente:
    ```bash
    python agent.py
    ```
    Este script mostrará as interações do agente com o banco de dados no seu terminal.

## Observações

* O script `pipeline.py` precisa estar rodando em segundo plano para que os dados sejam continuamente atualizados no banco de dados e, consequentemente, no dashboard.
* Certifique-se de que as variáveis de ambiente no arquivo `.env` estejam corretamente configuradas para permitir a conexão com o banco de dados.
* Para utilizar o agente, você precisará ter a biblioteca `agno` e as credenciais da Groq configuradas no seu ambiente.

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma sugestão de melhoria ou encontrar algum problema, sinta-se à vontade para abrir uma issue ou enviar um pull request.