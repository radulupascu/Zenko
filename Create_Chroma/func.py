from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
import pandas as pd

def load_pdf(PATH):
  load_dotenv()
  loader = PyPDFLoader(PATH)
  return loader.load()

def load_csv(PATH):
  return pd.read_csv(PATH, encoding='ISO-8859-1', on_bad_lines='skip')
  

def csv_to_text(data, delimiter='\t'):
    """
    Convert data from a CSV file to plain text.

    Args:
        file_path (str): The path to the CSV file.
        delimiter (str): The delimiter used to separate values (default is tab '\t').

    Returns:
        str: The CSV data formatted as plain text.
    """
    text = data.to_string(index=False)
    return text

def split_text(data, chunk_size=500, chunk_overlap=50):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  return text_splitter.split_documents(data)

def get_embeddings(API_KEY):
  return OpenAIEmbeddings(openai_api_key=API_KEY)