# 🔍 Ferramenta de Pesquisa de Notícias com IA

Este projeto é uma aplicação web interativa, construída com **Streamlit**, que permite aos usuários extrair informações e obter respostas a partir do conteúdo de artigos online. Utilizando a poderosa arquitetura de **Geração Aumentada por Recuperação (RAG)**, a ferramenta processa URLs, cria um banco de dados de vetores e, em seguida, utiliza um **Grande Modelo de Linguagem (LLM)** da **AWS Bedrock** para responder a perguntas com base nos dados fornecidos, citando as fontes originais.

### ✨ Destaques do Projeto

* **Extração de Dados:** Processa automaticamente o conteúdo de URLs de notícias fornecidas pelo usuário.

* **Geração Aumentada por Recuperação (RAG):** Uma arquitetura robusta que garante respostas precisas e baseadas em fatos, minimizando alucinações.

* **Armazenamento Eficiente:** Utiliza **FAISS** para criar e salvar um índice local de vetores, otimizando o processo de recuperação.

* **Interface Intuitiva:** Uma interface de usuário simples e limpa, desenvolvida com Streamlit, facilita a interação e o uso da ferramenta.

* **Integração com AWS Bedrock:** Demonstra proficiência em modelos de linguagem de ponta e infraestrutura da AWS.

### 🚀 Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.

* **Streamlit:** Framework para a construção da interface web.

* **LangChain:** Orquestrador para a construção de pipelines de LLM.

* **AWS Bedrock:** Plataforma que fornece acesso a modelos de fundação de alta performance.

* **FAISS:** Biblioteca para busca de similaridade e agrupamento de vetores.

* **UnstructuredURLLoader:** Utilizado para carregar e extrair dados de URLs.

### ⚙️ Instalação e Configuração

Siga estes passos para configurar e executar o projeto em sua máquina local.

1. **Clone o repositório:**
```
git clone https://github.com/BrenoaAlmeida/ferramenta-de-pesquisa-de-noticias.git  
cd ferramenta-de-pesquisa-de-noticias
```

2. **Crie e ative um ambiente virtual (recomendado):**

```
python -m venv venv  
source venv/bin/activate
```


3. **Instale as dependências do projeto:**

```
pip install -r pacotes.txt
```

4. **Configure as credenciais e modelos da AWS:**
Crie um arquivo chamado `.env` na raiz do projeto e adicione as seguintes variáveis, substituindo os valores pelos seus:

AWS_MODEL=VALOR_EXEMPLO_AWS  
EMBEDDINGS_MODEL_ID=VALOR_EXEMPLO_EMBEDDING  


*Certifique-se de ter as credenciais da AWS configuradas em seu ambiente local (via `~/.aws/credentials` ou variáveis de ambiente) com permissão para acessar o serviço Bedrock.*

### 💻 Como Usar

1. **Execute a aplicação Streamlit:**
```
streamlit run app.py
```

2. A aplicação será aberta automaticamente em seu navegador.

3. Na barra lateral, insira até três URLs de artigos de notícias.

4. Clique no botão "Processar URLs".

5. Aguarde o processo de carregamento e criação do índice FAISS.

6. Após a conclusão, insira sua pergunta na caixa de texto.

7. A ferramenta responderá com base no conteúdo dos artigos, fornecendo a resposta e as fontes utilizadas.

### 👤 Autor

* **\[Breno Gonçales de Almeida\]** - \[[LinkedIn](https://www.linkedin.com/in/brenogoncalvesalmeida/)\]