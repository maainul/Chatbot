from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain.text_splitter import CharacterTextSplitter

# Step 1: Load document
loader = TextLoader("hr_policy.txt", encoding="utf-8")
documents = loader.load()

# Step 2: Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

# Step 3: Vector embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")  # Ensure model is pulled
db = FAISS.from_documents(texts, embeddings)

# Step 4: Create chatbot with RetrievalQA
llm = OllamaLLM(model="mistral")  # Make sure 'mistral' model is pulled
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

# Step 5: User input loop
print("🤖 HR Chatbot চালু ✅ (exit লিখে বের হোন)\n")
while True:
    query = input("🧑 আপনি: ")
    if query.lower() == "exit":
        print("বিদায়! 😊")
        break
    answer = qa.invoke({"query":query})
    print("🤖 HR Bot:", answer["result"], "\n")
