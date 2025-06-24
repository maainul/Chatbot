from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain.chains import RetrievalQA
import csv
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

# ✅ Step 4: Read CSV and prepare documents
def read_csv_as_text(file_path):
    with open(file_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        text = ""
        for row in reader:
            text += (
                f"Employee {row['EmployeeName']} ({row['EmployeeID']}) is allowed "
                f"{row['AllowedDays']} days {row['LeaveType']} in {row['Year']}, "
                f"taken {row['TakenDays']} days.\n"
            )
    return text

csv_file = "leave_policy.csv"
data_text = read_csv_as_text(csv_file)
documents = [Document(page_content=data_text)]

# ✅ Step 5: Text split & Vector DB
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(documents)
embeddings = OllamaEmbeddings(model="nomic-embed-text")
db = FAISS.from_documents(texts, embeddings)

# ✅ Step 6: LLM and QA chain
llm = OllamaLLM(model="mistral")
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

# ✅ Step 7: Chat endpoint
@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    query = req.message
    response = qa_chain.invoke({"query": query})
    return {"reply": response["result"]}




















































# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from langchain_ollama import OllamaLLM

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],  # React runs এখানে
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# llm = OllamaLLM(model="mistral", temperature=0.7)

# class ChatRequest(BaseModel):
#     message: str


# @app.post("/chat")
# async def chat_endpoint(req: ChatRequest):
#     prompt = req.message
#     response = llm.invoke(prompt)
#     return {"reply": response}