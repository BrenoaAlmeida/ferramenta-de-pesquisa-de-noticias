import os
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader #Permite carregar dados a partir de um arquivo de texto
from langchain.document_loaders.csv_loader import CSVLoader #Permite carregar dados a partir de um arquivo de XLSX
from langchain.document_loaders import UnstructuredURLLoader #Carrega text de uma pagina a partir de uma URL
from langchain.text_splitter CharacterTextSplitter #Separa os caracteres de um texto em Arrays de X Caracteres de acordo com um separador
from langchain.text_splitter RecursiveCharacterTextSplitter #Separa os caracteres de um texto em Arrays de X Caracteres de forma recursiva de acordo com X separadores

load_dotenv()
TEXT_FILE_LOCATION = os.getenv("TEXT_FILE_LOCATION")
CSV_FILE_LOCATION = os.getenv("CSV_FILE_LOCATION")

#TODO: IMPLEMENTAR Conversão de Texto para EMBEDDING
SENTENCE_TRANSFORMER = os.getenv("SENTENCE_TRANSFORMER")

def TextLoad():
    loader = TextLoader(TEXT_FILE_LOCATION)
    data = loader.load()
    print(data[0].metadata, data[0].page_content)

def CsvLoad():
    loader = CSVLoader(CSV_FILE_LOCATION, source_column="title")
    data = loader.load()
    print(data[0].metadata, data[0].page_content)

def UrlLoader():
    loader = UnstructuredURLLoader(urls=[
        "https://edition.cnn.com/2025/08/01/investing/us-stock-market",
        "https://edition.cnn.com/2025/07/11/investing/us-stock-market"
    ])
    data = loader.load()
    print(data[0])
    print(data[0].metadata)

def CharacterTextSplitter():
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=200,
        chunk_overlap=0
    )

    chunks = splitter.split(TEXT_FILE_LOCATION);
    print(chunks)

    for chunk in chunks:
        print(len(chunk))

def RecursiveCharacterTextSplitter():
    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", "."],
        chunk_size=200,
        chunk_overlap=0
    )

    chunks = splitter.split(TEXT_FILE_LOCATION);
    print(chunks)

    for chunk in chunks:
        print(len(chunk))


if __name__ == "__main__":
    TextLoad()