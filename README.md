# Agentic-AI
VC Analyst Swarm is an Agentic AI Architecture designed to automate Venture Capital due diligence. Unlike a standard chatbot, this project uses a Multi-Agent System (MAS) where distinct AI personas collaborate to produce a balanced Investment Memo:  🕵️ The Researcher and The Editor

# 🕵️ VC Analyst Swarm

> **Winner/Participant: Agentic AI Hackathon 2024**
> *Built with Google Gemini 1.5 & Python*

## 📖 Overview
VC Analyst Swarm is an **Agentic AI Architecture** designed to automate Venture Capital due diligence. 

Unlike a standard chatbot, this project uses a **Multi-Agent System (MAS)** where distinct AI personas collaborate to produce a balanced Investment Memo:
1.  **🕵️ The Researcher:** Scours the live web for market data and competitors.
2.  **📝 The Editor:** Synthesizes the raw data into a structured, professional report.

## ⚙️ Architecture
The system utilizes a **Sequential Handoff Pattern**:

`[User Topic]` → `[Researcher Agent]` → `[Tool Use: DuckDuckGo]` → `[Editor Agent]` → `[Final Report]`

### Technical Highlights
-   **Engine:** Google Gemini 1.5 (Auto-detects Flash/Pro).
-   **Tooling:** Custom Python wrapper for `DuckDuckGoSearch`.
-   **Design:** Modular `SwarmManager` class for easy scalability.

## 🚀 How to Run
1.  Clone the repo:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/VC-Analyst-Swarm.git](https://github.com/YOUR_USERNAME/VC-Analyst-Swarm.git)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the Swarm:
    ```bash
    export GOOGLE_API_KEY=your_key_here
    python main.py
    ```

## 📂 Project Structure
-   `src/agents.py`: Contains the logic for the Researcher and Editor agents.
-   `src/tools.py`: Handles web search and data retrieval.
-   `main.py`: Entry point for the application.
