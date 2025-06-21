# 🚗 Advanced Multi-Agent Car Sales System (Groq + Gemini Edition)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-🦜🔗-green.svg)](https://langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-⚡️-orange.svg)](https://groq.com/)
[![Gemini](https://img.shields.io/badge/Gemini-✨-red.svg)](https://ai.google.dev/)
[![Streamlit](https://img.shields.io/badge/Streamlit-🎈-red.svg)](https://streamlit.io/)

> **A sophisticated multi-agent AI system for intelligent car sales, demonstrating advanced agent coordination, real-time research, and professional sales workflows, all powered by high-speed Groq inference.**

---

## 🏗️ Architecture

The system orchestrates three specialized AI agents, each with a distinct role, to create a seamless and intelligent customer experience. LangChain provides the agent framework, Streamlit powers the user interface, and Groq's LPU ensures near-instant responses.

<p align="center">
  <img src="https://raw.githubusercontent.com/jomasego/multiagent_sales/main/diagram.png" alt="Architecture Diagram" width="700"/>
</p>

### 🤖 Meet the Agents

| Agent | Model | Role | Specialization |
|-------|-------|------|----------------|
| **🎯 John** | `llama3-70b-8192` (Groq) | Sales Expert | Customer interaction, sales process, negotiation |
| **🔬 Dru** | `gemini-pro` (Google AI) | Research Specialist | Vehicle research, technical analysis, market data |
| **🏢 Boss** | `llama3-70b-8192` (Groq) | Business Coordinator | Inventory management, pricing, business policies |

---

## ✨ Key Features

- **🚀 High-Speed Inference**: Near-instant agent responses powered by Groq's LPU technology.
- **🧠 Intelligent Agent Coordination**: Seamless communication between specialized agents for a comprehensive sales workflow.
- **🔍 Smart Inventory Search**: AI-powered vehicle matching against a local CSV database.
- **🌐 Real-time Research**: On-demand technical details and market data provided by the Gemini-powered research agent.
- **💼 Professional Sales Process**: The system can handle the entire sales funnel, from initial greeting to negotiation.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- A [Groq API Key](https://console.groq.com/keys)
- A [Google AI (Gemini) API Key](https://ai.google.dev/)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/jomasego/multiagent_sales.git
    cd multiagent_sales
    ```

2.  **Create a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

4.  **Configure environment variables:**
    Create a file named `.env` in the project root and add your API keys:
    ```env
    GROQ_API_KEY="gsk_..."
    GEMINI_API_KEY="AIza..."
    ```

5.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

6.  **Access the interface:**
    Open your browser to `http://localhost:8501` and start chatting with John!

---

## 📖 Usage Examples

Once the application is running, you can interact with the sales agent. Here are a few examples:

-   **Initial Contact:** `"Hi, I'm looking for a car"`
-   **Specific Requirements:** `"I want a red sedan that's less than 2 years old"`
-   **Technical Inquiry:** `"What safety features does the Tesla Model 3 have for babies?"`
-   **Negotiation:** `"Can you offer any discount on the Ford Mustang?"`

---

## 🛠️ Technical Stack

-   **🤖 AI Models**: Groq `llama3-70b-8192`, Google `gemini-pro`
-   **🔗 Agent Framework**: LangChain
-   **🖥️ Frontend**: Streamlit
-   **📊 Data**: Pandas
-   **🐍 Language**: Python 3.8+
