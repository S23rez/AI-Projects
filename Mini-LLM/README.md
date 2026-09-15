# Mini-LLM 🤖

A lightweight, context-grounded Question-Answering (QA) application powered by the modern Google Gemini API (`google-genai` SDK) and Gemini 2.5 Flash model.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Repository Structure](#-repository-structure)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Future Roadmap](#-future-roadmap)
- [License](#-license)

---

## 🎯 Overview

**Mini-LLM** serves as a foundational prototype for building domain-specific LLM agents and Retrieval-Augmented Generation (RAG) pipelines. It prompts Google's `gemini-2.5-flash` model with customized domain context (e.g., company background, services, location) to deliver precise, context-aware answers while gracefully handling out-of-scope inquiries.

---

## ✨ Key Features

- **Gemini 2.5 Integration**: Uses the new official `google-genai` SDK for high-performance generation.
- **Context-Grounded QA**: Prevents hallucination by instructing the LLM to ground answers in provided background context.
- **Interactive CLI**: Simple command-line interface for querying company and service details.
- **Modular Design**: Separates data context, API interactions, and agent configuration.
- **Secure Configuration**: Uses `python-dotenv` for API key management without exposing credentials.

---

## 📁 Repository Structure

```text
Mini-LLM/
├── LLM/
│   ├── Agent.py       # Main CLI agent & Gemini API prompt execution engine
│   ├── data.py        # Knowledge base & context definitions
│   └── llm_agent.py   # Agent module scratchpad / extension entry point
├── .env               # Environment variable configuration (API keys)
└── README.md          # Project documentation
```

---

## 📋 Prerequisites

- **Python 3.10+**
- A **Google Gemini API Key** (obtainable via [Google AI Studio](https://aistudio.google.com/))

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/Mini-LLM.git
   cd Mini-LLM
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   # Windows (PowerShell)
   python -m venv LLM/.virt
   .\LLM\.virt\Scripts\Activate.ps1

   # macOS / Linux
   python3 -m venv LLM/.virt
   source LLM/.virt/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install google-genai python-dotenv requests
   ```

4. **Configure Environment Variables**
   Create or update the `.env` file inside the `LLM/` folder (or project root):
   ```env
   API_KEY=your_gemini_api_key_here
   ```

---

## 🚀 Usage

Run the main agent script from your terminal:

```bash
python LLM/Agent.py
```

### Example Interaction

```text
Welcome to Suarez Corporation
What would you like know: What services does Suarez Corporation offer?

Response:
Suarez Corporation specializes in Cloud Service Provision and is located in Ohio, USA.
```

---

## 🗺️ Future Roadmap

- [ ] **Vector Database Integration**: Store and query embeddings using ChromaDB / FAISS.
- [ ] **Data Pipeline & Ingestion**: Dynamically fetch external datasets (e.g., JSON endpoints, web docs).
- [ ] **RAG Orchestrator**: Build multi-step retrieval and reranking layers.
- [ ] **Web UI**: Deploy an interactive frontend interface (Streamlit / Gradio).

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more details.
