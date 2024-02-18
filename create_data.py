from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import os

#os.environ['OPENAI_API_KEY'] = "add your key here"
def get_data_from_web(url):
   loader = WebBaseLoader(url)
   document =loader.load()
   chunks = make_chunks(document)
   vector_db = make_vector(chunks)
   return vector_db

def make_chunks(document):
   splitter = RecursiveCharacterTextSplitter()
   docs = splitter.split_documents(document)
   return docs

def make_vector(chunks):
   vector_store = Chroma.from_documents(chunks,OpenAIEmbeddings())
   return vector_store
   