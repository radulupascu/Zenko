from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader

def load_pdf(PATH):
  load_dotenv()
  loader = PyPDFLoader(PATH)
  return loader.load()

def add_data():
  pass