## 🪟 Windows-এ Ollama ইন্সটল গাইড ✅

### 🔹 Step 1: ডাউনলোড করুন

👉 নিচের লিংকে যান:
🌐 [https://ollama.com/download](https://ollama.com/download)

* পেজ ওপেন হলে **“Download for Windows”** বাটনে ক্লিক করুন।
* একটি ফাইল নামবে: `OllamaSetup.exe`

---

### 🔹 Step 2: ইনস্টল করুন

1. `OllamaSetup.exe` ফাইলটিতে ডাবল ক্লিক করুন।
2. “Next”, “Install”, “Finish” — এগুলোতে ক্লিক করে স্বাভাবিকভাবে ইনস্টল শেষ করুন।
3. ইনস্টল শেষ হলে Ollama ব্যাকগ্রাউন্ডে চালু থাকবে (Windows Service হিসেবে)।

---

### 🔹 Step 3: টার্মিনাল খুলুন (PowerShell বা CMD)

1. Start মেনুতে গিয়ে **"Command Prompt"** বা **"PowerShell"** লিখে খুলুন।
2. এবার নিচের কমান্ড লিখুন:

```bash
ollama run mistral
```
---

## 📦 আপনি যেটা পাচ্ছেন আজ:

✅ Python দিয়ে বানানো একটি লোকাল HR চ্যাটবট
✅ LangChain + Ollama দিয়ে কাজ করবে
✅ আপনার প্রশ্নের উপর ভিত্তি করে “ডেটা থেকে উত্তর” দিবে (RAG System)
✅ Dummy HR policy দিয়ে শুরু করবো (আপনি চাইলে পরে নিজের Data দিবেন)

---

## 💻 ধাপ ১: আপনার কম্পিউটারে নিচের প্যাকেজগুলো ইনস্টল করুন

টার্মিনালে (PowerShell/Command Prompt) লিখুন:

```bash
pip install langchain langchain-community langchain-core faiss-cpu tiktoken
```

এগুলো না থাকলে chatbot কাজ করবে না।
(⚠️ এটা একবারই করতে হয়)

---

## 📁 ধাপ ২: `hr_policy.txt` নামে একটি ফাইল বানান

এই ফাইলটি বানিয়ে নিচের মতো কনটেন্ট বসান:

```
Company HR Policies 2024

1. Leave Policy:
- প্রতি কর্মী বছরে ২০ দিন পেইড ছুটি পায়।
- ১ বছরের বেশি চাকরি করলে ৬ মাসের মাতৃত্বকালীন ছুটি পাওয়া যায়।

2. বেতন:
- বেতনের তথ্য গোপন এবং শুধুমাত্র HR_Admin রোল দেখতে পায়।

3. Promotion Policy:
- প্রতি বছর কর্মীদের performance অনুযায়ী প্রমোশন হয়।

4. অফিস সময়সূচি:
- সকাল ৯টা থেকে বিকেল ৬টা (রবিবার থেকে বৃহস্পতিবার)।
```

---

## 🧠 ধাপ ৩: Python কোড রান করুন

নিচের কোডটা `chatbot.py` নামে সেভ করে চালান:

```python
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter

# Step 1: Load document
loader = TextLoader("hr_policy.txt", encoding="utf-8")
documents = loader.load()

# Step 2: Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

# Step 3: Vector embeddings
# embeddings = OllamaEmbeddings(model="nomic-embed-text")
embeddings = OllamaEmbeddings(model="nomic/embedding")
db = FAISS.from_documents(texts, embeddings)

# Step 4: Create chatbot
llm = Ollama(model="mistral")
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

# Step 5: User input loop
print("🤖 HR Chatbot চালু ✅ (exit লিখে বের হোন)\n")
while True:
    query = input("🧑 আপনি: ")
    if query.lower() == "exit":
        print("বিদায়! 😊")
        break
    answer = qa.run(query)
    print("🤖 HR Bot:", answer, "\n")
```

---

## 🧪 এখন চালান:

```bash
python chatbot.py
```

---

## 🗣️ উদাহরণ প্রশ্ন করুন:

```
আমি কি maternity leave নিতে পারবো?
আমার ছুটি কতো?
office কবে খোলা থাকে?
```

---

## ⏭️ পরবর্তী ধাপ?

* ✅ Role-Based Answer দিতে চাইলে: আমি দেখাবো কিভাবে HR/Admin/Employee আলাদা access পাবে
* ✅ আপনার নিজস্ব HR ফাইল দিতে চাইলে: আমি সেটাও ইনডেক্স করে দিব

আপনি লিখুন:

> “এখন role-based access চাই”
> অথবা
> “আমার নিজের data দিয়ে chatbot বানাও”

আমি সেই অনুযায়ী পরের ধাপ দেখিয়ে দিব। 🚀
