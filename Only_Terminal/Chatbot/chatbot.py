import csv
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

# Step 1: CSV থেকে ডাটা পড়ে একটানা টেক্সট বানানো
def read_csv_as_text(file_path):
    with open(file_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        text = ""
        for row in reader:
            # উদাহরণ হিসেবে leave_policy.csv এর জন্য
            text += f"Employee {row['EmployeeName']} ({row['EmployeeID']}) is allowed {row['AllowedDays']} days {row['LeaveType']} in {row['Year']}, taken {row['TakenDays']} days.\n"
    return text

# CSV ফাইলের নাম এখানে সেট করো
csv_file = "leave_policy.csv"

# Step 2: ডাটা লোড ও Document এ রূপান্তর
data_text = read_csv_as_text(csv_file)
documents = [Document(page_content=data_text)]

# Step 3: টেক্সট স্প্লিট করা (chunk বানানো)
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

# Step 4: এম্বেডিং তৈরি
embeddings = OllamaEmbeddings(model="nomic-embed-text")
db = FAISS.from_documents(texts, embeddings)

# Step 5: LLM ও QA Chain তৈরি
llm = OllamaLLM(model="mistral")
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

# Step 6: ইউজার ইন্টারফেস (ইনপুট আউটপুট লুপ)
print("\n🤖 Chatbot চালু ✅ (exit লিখে বের হোন)\n")
while True:
    query = input("🧑 আপনি: ")
    if query.lower() == "exit":
        print("বিদায়! 😊")
        break
    answer = qa.invoke({"query": query})
    print("🤖 Bot:", answer["result"], "\n")
