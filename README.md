# Desafio AutoU - Analisador de Emails com IA 🤖

Projeto desenvolvido como parte do desafio técnico da AutoU. A aplicação web utiliza Inteligência Artificial (Google Gemini) para classificar o conteúdo de emails em "Produtivo" ou "Improdutivo" e sugerir automaticamente uma resposta adequada, com o objetivo de otimizar o fluxo de trabalho da equipe.

---

## 🚀 Demonstração

Acesse a aplicação em funcionamento e assista ao vídeo de demonstração:

* **Aplicação no ar (Render):** **[[https://desafio-autou.onrender.com](https://desafio-autou-fgyi.onrender.com)]


---

## ✨ Funcionalidades

* **Classificação de Email:** Determina se um email requer uma ação imediata (Produtivo) ou se é uma mensagem informativa/social (Improdutivo).
* **Sugestão de Resposta:** Gera uma resposta automática, profissional e contextualmente adequada para emails produtivos.
* **Interface Simples:** Permite que qualquer usuário cole o texto de um email e obtenha a análise com um único clique.
* **Segurança:** Utiliza variáveis de ambiente para proteger a chave da API do Google, garantindo que ela não seja exposta publicamente.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído com as seguintes tecnologias:

* **Backend:** Python 3, Flask
* **Inteligência Artificial:** API do Google Gemini (modelo `models/gemini-2.5-flash`)
* **Frontend:** HTML5, CSS3, JavaScript (vanilla)
* **Servidor de Produção:** Gunicorn
* **Hospedagem (Deploy):** Render
* **Gerenciamento de Segredos:** `python-dotenv`

---

## 🖥️ Como Executar Localmente

Siga os passos abaixo para rodar o projeto em sua máquina local.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/](https://github.com/)[SEU_USUARIO_GITHUB]/[NOME_DO_SEU_REPOSITORIO]
    cd [NOME_DO_SEU_REPOSITORIO]
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Adicione sua chave da API do Google Gemini dentro dele:
        ```
        GOOGLE_API_KEY="SUA_CHAVE_API_SECRETA_AQUI"
        ```

5.  **Rode a aplicação:**
    ```bash
    python app.py
    ```

6.  **Acesse no navegador:**
    Abra [http://127.0.0.1:5000](http://127.0.0.1:5000) no seu navegador.
