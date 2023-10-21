from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from func import load_pdf


PATH = "CSV_Base/FAQ_FDV_Zenko_V1.2.pdf"
data = load_pdf(PATH)

print (f'You have {len(data)} document(s) in your data')
print (f'There are {len(data[-1].page_content)} characters in your document')