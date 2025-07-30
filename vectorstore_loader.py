import re
from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def load_vector_store():
    loader = DirectoryLoader("documents", glob="*.pdf", loader_cls=PyMuPDFLoader)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(chunks, embeddings)
    return db

def extract_amount_rupee(text):
    match = re.findall(r"₹\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?", text)
    return match[0] if match else None
