# 🚗 Multi-Agent Sales System (Groq + Gemini Edition)

This project demonstrates a multi-agent AI system for car sales, adapted to use Groq for high-speed inference and Google's Gemini for research tasks.

  <!-- Replace with the actual image URL -->

## 🎯 Overview

This system uses three specialized AI agents to create a seamless customer experience:

-   **John (Sales Expert)**: Handles customer interactions, powered by a high-capability Groq model.
-   **Dru (Research Specialist)**: Performs vehicle research and technical analysis using Gemini Pro.
-   **Boss (Business Coordinator)**: Manages inventory and pricing decisions with a strategic Groq model.

## 🚀 Quick Start

### Prerequisites

-   Python 3.8+
-   Groq API Key
-   Google AI (Gemini) API Key

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/jomasego/multiagent_sales.git
    cd multiagent_sales/multiagent_sales_app
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up API keys:**

    Create a `.env` file in the `multiagent_sales_app` directory and add your API keys:

    ```env
    GROQ_API_KEY="your_groq_api_key"
    GEMINI_API_KEY="your_gemini_api_key"
    ```

### Running the Application

```bash
streamlit run app.py
```

Open your browser to `http://localhost:8501` to interact with the sales system.
