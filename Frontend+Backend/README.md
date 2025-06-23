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
ollama pull mistral
ollama pull nomic-embed-text
```
### Test Run

```
ollama run mistral
ollama run nomic-embed-text
```
### List 
```
ollama list
```

## 💻 ধাপ ১: আপনার কম্পিউটারে নিচের প্যাকেজগুলো ইনস্টল করুন

টার্মিনালে (PowerShell/Command Prompt) লিখুন:

```bash
pip install langchain langchain-community langchain-core faiss-cpu tiktoken

pip install -U langchain-ollama
```

এগুলো না থাকলে chatbot কাজ করবে না।
(⚠️ এটা একবারই করতে হয়)

---

## 📁 ধাপ ২: `leave_policy.txt` নামে একটি ফাইল বানান

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


দারুণ প্রশ্ন, Mainul! 😊
আমার (মানে ChatGPT-এর) UI যেটা তুমি এখন দেখছো — এটা বানানো হয়েছে **React.js** দিয়ে, আর backend-এ আছে **Python-based microservices**, পাশাপাশি **OpenAI API**।
এটা খুবই modern, scalable ও user-friendly।

---

## ✅ তোমার জন্য কোনটা ভালো হবে?

### তুমি যেহেতু MERN Stack এবং DevOps দুটিতেই কাজ করো, তাই আমি suggest করবো:

### 👉 **Frontend**: React.js + Tailwind CSS

### 👉 **Backend**: FastAPI (Python-based)

---

### 🎯 কেন এই কম্বিনেশন?

| Layer      | Technology   | কারণ                                                                             |
| ---------- | ------------ | -------------------------------------------------------------------------------- |
| UI         | React.js     | Reusable components, SPA support, chat-style layout সহজে করা যায়                 |
| Styling    | Tailwind CSS | Utility-first CSS framework, দ্রুত UI বানানো যায়                                 |
| API Server | FastAPI      | Fast, async-supported, Python-এ হওয়ায় তোমার LangChain ও Ollama সহজে integrate হয় |
| LLM Engine | Ollama       | Local model চলবে fast, secure এবং free                                           |

---

## ✅ তোমার Project Structure কেমন হতে পারে:

```
📦 chatbot-app/
├── frontend/          # React.js app
│   ├── App.jsx
│   ├── ChatUI.jsx
│   └── ...
├── backend/           # FastAPI backend
│   ├── main.py        # API endpoints
│   ├── chatbot.py     # LangChain logic
│   └── ...
```

---

## 🎯 আমরা কী বানাতে যাচ্ছি?

✅ A simple yet modern **Chat UI** using **React.js + Tailwind CSS**
✅ Chat box, message bubbles, input field, and loading state
✅ Later, we’ll connect this UI to your backend (FastAPI + Ollama)

---

## 📁 Project Structure (Frontend Only)

```
chatbot-frontend/
├── public/
├── src/
│   ├── components/
│   │   └── ChatBox.jsx
│   ├── App.jsx
│   ├── index.js
├── tailwind.config.js
├── package.json
```

---

## ✅ Step-by-Step Instructions

### Step 1: Initialize Project

```bash
npm create vite@latest chatbot-ui -- --template react
cd chatbot-ui
npm install
```

### Step 2: Build Chat UI

#### 🧩 `src/components/ChatBox.jsx`

```jsx
import { useState } from "react";

export default function ChatUI() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [activeTab, setActiveTab] = useState("General");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMsg = { role: "user", content: input, tab: activeTab };
    setMessages(prev => [...prev, userMsg]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });
      const data = await res.json();
      setMessages(prev => [
        ...prev,
        { role: "bot", content: data.reply, tab: activeTab },
      ]);
    } catch (err) {
      setMessages(prev => [
        ...prev,
        { role: "bot", content: "🚨 Server error!", tab: activeTab },
      ]);
    }

    setLoading(false);
  };

  const filteredMessages = messages.filter(msg => msg.tab === activeTab);

  return (
    <div className="app">
      <aside className="sidebar">
        <h2>ChatBot</h2>
        <ul className="chat-list">
          {["General", "HR", "Sales"].map(tab => (
            <li
              key={tab}
              className={tab === activeTab ? "active" : ""}
              onClick={() => setActiveTab(tab)}
            >
              {tab}
            </li>
          ))}
        </ul>
      </aside>

      <main className="chat-main">
        <div className="top-bar">🔍 {activeTab} বিভাগে আছেন</div>

        <div className="chat-box">
          {filteredMessages.map((msg, index) => (
            <div key={index} className={`message ${msg.role}`}>
              <span className="message-content">{msg.content}</span>
            </div>
          ))}

          {loading && (
            <div className="message bot typing-indicator">
              <span className="message-content">...</span>
            </div>
          )}
        </div>

        <div className="input-area">
          <input
            value={input}
            onChange={e => setInput(e.target.value)}
            placeholder="আপনার প্রশ্ন লিখুন..."
            onKeyDown={e => e.key === 'Enter' && sendMessage()}
          />
          <button onClick={sendMessage} disabled={loading}>
            {loading ? "..." : "Send"}
          </button>
        </div>
      </main>
    </div>
  );
}

```

#### 🧩 `src/App.jsx`

```jsx
import React from "react";
import ChatBox from "./components/ChatBox";

function App() {
  return (
    <div className="bg-gray-50 min-h-screen">
      <ChatBox />
    </div>
  );
}

export default App;
```

---

### ✅ Step 4: Run the App

```bash
npm start
```

Now visit `http://localhost:5173` — তুমি দেখতে পাবে একটা clean, modern chat interface.

---

### 🔗 Next Step:

Ready hole backend বানাবো — যা Ollama + LangChain এর সাথে connect করবে।

**তুমি কি প্রস্তুত backend part এর জন্য?** 😎📡


## 🧠 Next Step:

তুমি চাইলে আমি এখন তোমার জন্য FastAPI-based backend তৈরি করে দিতে পারি, যেখানে এই React UI 👉 Ollama + LangChain-এর সাথে সংযোগ করবে।

**তুমি কি backend চাও এখন?** ✅🧠


## এবার **backend তৈরি করবো React UI‑এর সাথে কাজ করার জন্য।** নিচে আমি ওয়ানস্টপ **FastAPI + Ollama** বেজড backend কোড দিচ্ছি, যা React‑এর fetch কল দিয়ে chat endpoint থেকে উত্তর দিবে।

---

## 🛠️ সেটআপ ধাপে ধাপে

### 1️⃣ Python Dependencies ইনস্টল করো:

```bash
pip install fastapi uvicorn langchain-community fastapi-cors
pip install ollama
```

### 2️⃣ `main.py` – FastAPI + Ollama Backend

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_ollama import OllamaLLM

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React runs এখানে
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = OllamaLLM(model="mistral", temperature=0.7)

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    prompt = req.message
    response = llm.invoke(prompt)
    return {"reply": response}
```

🔥 এখানে আমরা `Ollama` ব্যবহার করেছি লোকাল LLM চালানোর জন্য, আর FastAPI দিয়ে `/chat` endpoint তৈরি করেছি।

---

### 3️⃣ Server চালাও:

```bash
uvicorn main:app --reload --port 8000
```

---

## ✅ ✅ ✅ চূড়ান্ত ‑ Summary

| অংশ         | ✨ কাজ                             |
| ----------- | --------------------------------- |
| **FastAPI** | `/chat` endpoint, CORS enabled ✔  |
| **Ollama**  | লোকাল LLM, `mistral` মডেল ব্যবহার |
| **React**   | fetch call, মেসেজ UI অটো রেন্ডার  |

---

## Relode App : uvicorn main:app --reload --port 8000
