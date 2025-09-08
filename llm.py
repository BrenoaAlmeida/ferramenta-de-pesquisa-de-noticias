from copyreg import pickle
import os
import streamlit as st
import pickle
from dotenv import load_dotenv
import time
import langchain
from langchain import OpenAi
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter #Separa os caracteres de um texto em Arrays de X Caracteres de forma recursiva de acordo com X separadores
from langchain.document_loaders import UnstructuredURLLoader #Carrega text de uma pagina a partir de uma URL
from langchain.embeddings import OpenAiEmbeddings
from langchain.vectorstores import FAISS

load_dotenv()

llm = OpenAi(temperature=0, max_tokens=500)

loader = UnstructuredURLLoader(urls=[
    "https://edition.cnn.com/2025/08/01/investing/us-stock-market",
    "https://edition.cnn.com/2025/07/11/investing/us-stock-market"
])

data = loader.load()
len(data)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split(data);
len(chunks)

embedings = OpenAiEmbeddings()

#FAISS é uma ferramenta de embedding de vetores
vector_index = FAISS.from_documents(chunks, embedings)

file_path = "vector_index.pkl"

if(os.path.exists(file_path)):
    with open(file_path, "wb") as f:
        vector_index = pickle.load(f)    

else:
#store index locally
    with open(file_path, "wb") as f:
        pickle.dump(vector_index, f)

chain = RetrievalQAWithSourcesChain(llm=llm, retrivar=vector_index.as_retriever())

query = "What is the current state of the US stock market?"

langchain.debug = True

result = chain({"question": query}, return_only_outputs=True)
print(result)

