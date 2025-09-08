import os
import streamlit as st
from langchain_aws import ChatBedrock, BedrockEmbeddings
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

MODEL_ID = os.getenv("AWS_MODEL")
EMBEDDINGS_MODEL_ID = os.getenv("EMBEDDINGS_MODEL_ID")

llm = ChatBedrock(
    model_id=MODEL_ID,
    model_kwargs={
        "max_tokens": 512,
        "temperature": 0.7,
        "top_p": 0.9,
    },
)

st.title("Ferramenta de Pesquisa de Notícias")
st.sidebar.title("URLs do artigo")

urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]
process_url_clicked = st.sidebar.button("Processar URLs")
status = st.empty()

file_path = "faiss_index"

if process_url_clicked:
    loader = UnstructuredURLLoader(urls=[u for u in urls if u.strip()])
    data = loader.load()
    status.text("(1/5) Carregando dados...")

    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", "."],
        chunk_size=1000,
    )
    docs = text_splitter.split_documents(data)
    status.text("(2/5) Separando em chunks...")

    embeddings = BedrockEmbeddings(model_id=EMBEDDINGS_MODEL_ID)

    vector_store = FAISS.from_documents(docs, embeddings)
    status.text("(3/5) Gerando embeddings...")

    vector_store.save_local(file_path)
    status.success("(4/5) FAISS salvo com sucesso!")

query = st.text_input("Pergunta:")

if query.strip():
    if os.path.exists(file_path):
        status.text("(5/5) Carregando FAISS...")
        embeddings = BedrockEmbeddings(model_id=EMBEDDINGS_MODEL_ID)
        vector_store = FAISS.load_local(
            file_path, embeddings, allow_dangerous_deserialization=True
        )

        chain = RetrievalQAWithSourcesChain.from_llm(
            llm=llm, retriever=vector_store.as_retriever()
        )

        with st.spinner("Respondendo pergunta..."):
            result = chain({"question": query}, return_only_outputs=True)

        st.header("Resposta:")
        st.write(result["answer"])

        sources = result.get("sources", "")
        if sources:
            st.subheader("Fontes:")
            for source in sources.split("\n"):
                st.write(source)

        status.empty()
    else:
        st.warning("Nenhum índice encontrado. Clique em 'Processar URLs'.")
