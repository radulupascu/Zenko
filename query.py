import os
from IPython.display import display
import ipywidgets as widgets
import pandas as pd
import textract

from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
import matplotlib.pyplot as plt
from transformers import GPT2TokenizerFast
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

from langchain.chains import ConversationalRetrievalChain
# Get embedding model
# Create vector database

os.environ["OPENAI_API_KEY"]="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"
doc = PdfReader("C:/Users/Asus/PycharmProjects/pythonProject4/Attention-is-all-you-need-Paper.pdf")
raw_text = ''
for i, page in enumerate(doc.pages):
    text = page.extract_text()
    if text:
        raw_text += text
text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)
embeddings = OpenAIEmbeddings()

db = FAISS.from_texts(texts, embeddings)
open_api_key = "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"
qa = ConversationalRetrievalChain.from_llm(OpenAI(model_kwargs={"OPEN_API_KEY": "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"}, temperature=0.1), db.as_retriever())

chat_history = []

def on_submit(_):
    query = input_box.value
    input_box.value = ""

    if query.lower() == 'exit':
        print("Thank you for using the State of the Union chatbot!")
        return

    result = qa({"question": query, "chat_history": chat_history})
    chat_history.append((query, result['answer']))

    display(widgets.HTML(f'<b>User:</b> {query}'))
    display(widgets.HTML(f'<b><font color="blue">Chatbot:</font></b> {result["answer"]}'))

    print("Welcome to the Transformers chatbot! Type 'exit' to stop.")

    input_box = widgets.Text(placeholder='Please enter your question:')
    input_box.on_submit(on_submit)

    display(input_box)
plt.show()