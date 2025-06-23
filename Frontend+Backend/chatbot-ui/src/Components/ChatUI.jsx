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
