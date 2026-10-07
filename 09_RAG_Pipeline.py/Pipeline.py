import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings # Agar aap OpenAI use kar rahe hain toh OpenAIEmbeddings import karein
from langchain_community.vectorstores import Chroma
from langchain.chain import RetrievalQA
from langchain_community.llms import Ollama # Ya OpenAI LLM

# ===================================================
# TUTORIAL 3 & 4: DETAILED STEP-BY-STEP RAG PIPELINE
# ===================================================

print("1. Environment aur Libraries loaded successfully!\n")

# ---------------------------------------------------
# STEP 1: Document Loading
# ---------------------------------------------------
print("--- STEP 1: Loading PDF Document ---")
# Apni kisi bhi PDF ka path yahan dein
pdf_path = "sample.pdf" 

if os.path.exists(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    print(f"Total pages loaded in document: {len(docs)}")
    print(f"Sample content from page 1:\n{docs[0].page_content[:200]}...\n")
else:
    print(f"Warning: '{pdf_path}' nahi mili. Kripya sahi path dein.")

# ---------------------------------------------------
# STEP 2: Text Splitting (Chunks mein todna)
# ---------------------------------------------------
print("--- STEP 2: Splitting Text into Chunks ---")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200
)
# Agar docs loaded hain tabhi split karein
final_documents = text_splitter.split_documents(docs) if 'docs' in locals() else []
print(f"Total chunks created: {len(final_documents)}")
if len(final_documents) > 0:
    print(f"First chunk preview:\n{final_documents[0].page_content[:300]}...\n")

# ---------------------------------------------------
# STEP 3: Vector Embeddings & ChromaDB Storage
# ---------------------------------------------------
print("--- STEP 3: Creating Embeddings & Storing in ChromaDB ---")
# Free local embeddings ke liye Ollama ya OpenAI embeddings use kar sakte hain
embeddings = OllamaEmbeddings(model="llama3") 

# Documents ko vector mein convert karke local disk par 'chroma_db' folder mein save karna
db = Chroma.from_documents(
    documents=final_documents, 
    embedding=embeddings, 
    persist_directory="./chroma_db"
)
print("ChromaDB vector database successfully initialized and saved locally!\n")

# ---------------------------------------------------
# STEP 4: Retriever Setup & Testing (Tutorial 4)
# ---------------------------------------------------
print("--- STEP 4: Setting up Retriever ---")
retriever = db.as_retriever(
    search_type="similarity", 
    search_kwargs={"k": 3} # Top 3 most relevant chunks fetch honge
)

# Test query karke check karte hain ki database se data aa raha hai ya nahi
test_query = "Aapka jo bhi sawal ho document se related"
relevant_chunks = retriever.get_relevant_documents(test_query)
print(f"Test Query ke liye {len(relevant_chunks)} relevant chunks retrieve hue hain.\n")

# ---------------------------------------------------
# STEP 5: Q&A Chain Setup & LLM Integration (Tutorial 4)
# ---------------------------------------------------
print("--- STEP 5: Setting up Q&A Chain with LLM ---")
llm = Ollama(model="llama3") # Ya OpenAI(model="gpt-3.5-turbo")

# RetrievalQA chain banana jo retriever aur LLM ko jodta hai
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True # Yeh batayega ki answer kis page/chunk se aaya hai
)

# ---------------------------------------------------
# STEP 6: Running Final Query
# ---------------------------------------------------
print("--- STEP 6: Executing Final Query ---")
query = "Explain the main topic discussed in this document."
response = qa_chain({"query": query})

print("\n================ AI RESPONSE ================")
print(response["result"])
print("=============================================\n")

print("--- Source Documents References ---")
for i, doc in enumerate(response["source_documents"]):
    print(f"Source {i+1} (Page {doc.metadata.get('page', 'N/A')}): {doc.page_content[:150]}...\n")