# 🤖 Artificial Intelligence, Autonomous Agents & Threat Intelligence

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg?logo=python&logoColor=white)](https://python.org)
[![Author](https://img.shields.io/badge/Developer-Odunuga%20Fatai%20Olayinka-0A66C2.svg?logo=linkedin)](https://github.com/S23rez)
[![Gemini](https://img.shields.io/badge/AI-Google%20Gemini%202.5-8E75B2.svg?logo=google)](https://aistudio.google.com)
[![Multi-Agent](https://img.shields.io/badge/Architecture-Autonomous%20Agents-orange.svg)](#)
[![Docker](https://img.shields.io/badge/Deployment-Docker%20Compose-2496ED.svg?logo=docker)](https://docker.com)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791.svg?logo=postgresql)](https://postgresql.org)

A portfolio of advanced artificial intelligence, autonomous agent pipelines, and Large Language Model (LLM) applications developed by **Odunuga Fatai Olayinka**.

This repository explores the intersection of **Artificial Intelligence and Cybersecurity**, demonstrating how modern LLMs and agentic systems can be harnessed for autonomous open-source threat intelligence (OSINT), automated log enrichment, technical data summarization, and context-grounded retrieval-augmented generation (RAG).

---

## 🏗️ Repository Overview

```text
AI-Projects/
├── 📄 README.md                        <- Master AI Engineering Guide
├── 📂 ai-news-aggregator/              <- Autonomous Multi-Agent Intelligence Pipeline
│   ├── 📄 README.md                    <- Full System Specification
│   └── 📂 AI Aggregator/ai-news-aggregator/
│       ├── 📂 app/                     <- Agents, Scrapers, Database Models & Runner
│       └── 📂 docker/                  <- PostgreSQL & App Docker Compose
└── 📂 Mini-LLM/                        <- Gemini 2.5 Flash Retrieval-Augmented Generation
    ├── 📄 README.md                    <- Prototype Specification
    └── 📂 LLM/                         <- Grounded CLI Agent & Context Engine
        └── 📄 README.md                <- Execution Engine Architecture & Guide
```

---

## 📁 Flagship Projects & Implementations

### 1. 📰 Autonomous Multi-Agent Intelligence Aggregator (`ai-news-aggregator/`)
* **Objective:** Automates end-to-end monitoring of high-velocity technological and security intelligence feeds.
* **Agentic Architecture:**
  * **Scraper Layer:** Ingests research articles from Anthropic, OpenAI, and technical YouTube channel audio transcripts.
  * **Curator Agent:** Autonomous LLM agent filtering signal from noise and evaluating relevance.
  * **Digest Agent:** Synthesizes structured technical briefings and executive summaries.
  * **Email Agent:** Formats and dispatches automated HTML intelligence newsletters.
* **Storage & Deployment:** Persisted to PostgreSQL using SQLAlchemy models and containerized with Docker Compose.
* 🔗 **Full Documentation:** [ai-news-aggregator/README.md](file:///c:/Users/Suarez/My-Portfolios/AI-Projects/ai-news-aggregator/README.md)

---

### 2. 🤖 Mini-LLM: Context-Grounded QA Engine (`Mini-LLM/`)
* **Objective:** A lightweight Question-Answering application demonstrating prompt engineering and hallucination mitigation.
* **Technical Highlights:**
  * Powered by Google's `gemini-2.5-flash` model via the modern `google-genai` SDK.
  * Employs context-grounded prompt constraints, ensuring the model only answers based on verified organizational domain context.
  * Secure credential management via `python-dotenv`.
* 🔗 **Full Documentation:** [Mini-LLM/README.md](file:///c:/Users/Suarez/My-Portfolios/AI-Projects/Mini-LLM/README.md) · [LLM Engine Guide](file:///c:/Users/Suarez/My-Portfolios/AI-Projects/Mini-LLM/LLM/README.md)

---

## 🛡️ AI Relevance to Modern Cybersecurity

```
Threat Intelligence Automation : Ingests unstructured security bulletins and vendor advisories, converting them
                                 into structured IOCs (Indicators of Compromise) and executive alerts.
AI Safety & Defense Hardening  : Explores prompt injection prevention, context boundaries, and output validation
                                 required to safely integrate LLM assistants into security operations.
OSINT & Surface Monitoring     : Demonstrates automated scraping, transcript extraction, and content classification
                                 for continuous external threat and competitor surface monitoring.
```

---

## 👤 Author

**Odunuga Fatai Olayinka**  
Cybersecurity Specialist | Systems & Cloud Security Engineer  
* GitHub: [@S23rez](https://github.com/S23rez)
