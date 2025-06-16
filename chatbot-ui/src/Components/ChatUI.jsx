import { useState } from "react";

export default function ChatUI() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { role: "user", content: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");

    setTimeout(() => {
      const botMsg = {
        role: "bot",
        content: "আমি বুঝেছি: " + input,
      };
      setMessages((prev) => [...prev, botMsg]);
    }, 800);
  };

  return (
    <div className="app">
      <aside className="sidebar">
        <h2>ChatBot</h2>
        <ul className="chat-list">
          <li className="active">General</li>
          <li>HR</li>
          <li>Sales</li>
        </ul>
      </aside>

      <main className="chat-main">
        <div className="top-bar">What are you working on?</div>

        <div className="chat-box">
          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.role}`}>
              <span className="message-content">{msg.content}</span>
            </div>
          ))}
        </div>

        <div className="input-area">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="আপনার প্রশ্ন লিখুন..."
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </main>
    </div>
  );
}
