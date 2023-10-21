from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

from func import load_pdf


PATH = "CSV_Base/FAQ_FDV_Zenko_V1.2.pdf"
data = load_pdf(PATH)
OPENAI_API_KEY = open("API_KEY", "r").read()
PINECONE_API_KEY = "7ff48757-3d6c-4dd1-b78c-a2d4e49177c9"
PINECONE_API_ENV = "gcp-starter"

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(data)

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_API_ENV  # next to api key in console
)
index_name = "faq" # put in the name of your pinecone index here

docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
chain = load_qa_chain(llm, chain_type="stuff")
query = input("ASK:")
docs = docsearch.similarity_search(query)
