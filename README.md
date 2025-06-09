# 🛠️ AI Workflow Architect – Built in Under 1 Hour

> 🔥 I built this project in **just 1 hour** to demonstrate how fast agentic AI systems can be prototyped when you focus on modular goal execution, not just LLM completions.

---

## 🚀 What It Does

A LangGraph-powered multi-agent system that transforms natural language goals into structured task flows — then **executes them using mock tools** (like Email, LinkedIn, and Calendar APIs).

---

## 💡 Example Input
> _“Schedule a product webinar and send invites”_

### 🔄 What Happens
1. 🎯 **Goal Parsing** – Extracts the intent from user input  
2. 💬 **Clarification Agent** – Asks for more info if the goal is vague  
3. 🧠 **Fuzzy Task Planner** – Uses fuzzy match + keyword logic to map goal to tools  
4. 🔧 **Tool Executor** – Simulates execution (email/calendar/post)  
5. 🔁 **Feedback Loop** – User can say "go again" or "stop"

---

## 🧩 Tech Stack
- **LangGraph** – Agent workflow orchestration
- **Python** – CLI backend
- **Difflib + `input()`** – Fuzzy matching + interactive user feedback
- **Mock Mode** – No real APIs needed, perfect for quick demos

---

## 🔧 Tools (Mocked but Modular)
- `email_sender`
- `calendar_api`
- `linkedin_poster`
- `default_tool` (fallback for unknowns)

---

## 🧠 Smart Behaviors
- Fuzzy match for terms like “webinar”, “invite”, “schedule”
- Falls back to asking the user if the goal is unclear
- Extensible design — easily plug GPT or API tools into each node

---

## 💥 Why This Stands Out
- ⏱️ **Built in 1 hour** — shows execution speed and architectural clarity  
- 📦 **Agent-based, not just chat-based** — structured, multi-step automation  
- 🔧 **Built for real-world usage** — not just a wrapper around OpenAI