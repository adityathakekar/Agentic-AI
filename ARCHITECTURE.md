# 🕵️ VC Analyst Swarm

> **Submission for Agentic AI Hackathon 2025**
> *A Sequential Multi-Agent System (MAS) for Venture Capital Due Diligence.*

## 📖 The Problem
Venture Capital research is time-consuming. Associates spend hours gathering fragmented data from the web and synthesizing it into reports. Standard LLMs often hallucinate specific market data or lack the ability to critique their own findings.

## 💡 The Solution
**VC Analyst Swarm** is an autonomous agentic pipeline that mimics a real-world research team. It is not a single chatbot, but a **Sequential Multi-Agent System** where distinct personas collaborate to produce a high-quality Investment Memo.

## 🏗️ System Architecture
We implemented a **Sequential Handoff Pattern**. The system mimics a linear assembly line where data is refined at each step.

## 🔮 Future Roadmap
While this MVP demonstrates the core Agentic Architecture, the full vision includes:
* **Vector Database Integration (RAG):** To store and recall previous investment memos.
* **Human-in-the-Loop Mode:** allowing a senior partner to approve the "Skeptic's" findings before the report is generated.
* **Multi-Modal Analysis:** Using Gemini 1.5 Pro to analyze PDF pitch decks and charts, not just text search.


### The Agent Workflow
```mermaid
graph LR
    A[User Input] -->|Topic| B(🕵️ Researcher Agent)
    B -->|Tool Call| C{DuckDuckGo Search}
    C -->|Raw Data| B
    B -->|Synthesized Findings| D(📝 Editor Agent)
    D -->|Formatting Rules| E[📄 Final Investment Memo]


