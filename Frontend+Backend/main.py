from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain.chains import RetrievalQA
import pandas as pd



# ✅ Step 1: FastAPI init
app = FastAPI()

# ✅ Step 2: CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Step 3: Input model
class ChatRequest(BaseModel):
    message: str


# গ্লোবাল ভেরিয়েবল
employee_lookup = {}
qa_chain = None


# 📊 Read Excel and convert to text
def read_excel_as_text(file_path,sheet_name):
    # df = pd.read_excel(file_path, sheet_name="Sheet1")
    employee_lookup = {}
    df = pd.read_excel(excel_file, sheet_name)
    df['EmployeeID'] = df['EmployeeID'].astype(str).str.strip().str.upper()
    df['EmployeeName'] = df['EmployeeName'].astype(str).str.strip()
    employee_lookup = dict(zip(df['EmployeeID'], df['EmployeeName']))
    print("Look Up :",employee_lookup)
    text = ""
    for _, row in df.iterrows():
        text += f"{row['EmployeeID']} - {row['EmployeeName']}\n"
    return text, df



# 📂 Load Excel file and process documents
excel_file = "Employee_Info.xlsx"
sheet_name = "Sheet1"
data_text, df = read_excel_as_text(excel_file, sheet_name)
documents = [Document(page_content=data_text)]


# 📎 Split documents
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(documents)


# 🧬 Embedding + VectorDB
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = FAISS.from_documents(split_docs, embeddings)


# 🤖 Ollama LLM + QA chain
llm = OllamaLLM(model="mistral")
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())


# ✅ Step 7: Chat endpoint
@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    query = req.message
    words = query.split()
    print(words)
    for word in words:
        if word.upper() in employee_lookup:
            return {"reply": f"The name for {word.upper()} is: {employee_lookup[word.upper()]}"}

    if qa_chain:
        answer = qa_chain.invoke({"query": query})
        return {"reply": answer["result"]}
    else:
        return {"reply": "Please upload the Excel file first."}
