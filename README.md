# Autonomous Financial Risk & Operations Agent

An event-driven, AI-powered financial risk analysis system that performs
real-time transaction evaluation using LLMs, Retrieval-Augmented Generation (RAG),
Kafka streaming, and a production-ready FastAPI service.

---

## 🚀 Key Capabilities

- 🔍 Real-time transaction risk detection
- 🧠 Multi-step AI reasoning with GPT + Groq fallback
- 📚 Context-aware decisions using ChromaDB (RAG)
- ⚡ Event-driven architecture with Kafka
- 🌐 REST API exposure via FastAPI
- 🛡️ Safe failure & escalation design
- 🧩 Modular, extensible architecture

---

## 🧠 High-Level Architecture

                    ┌────────────────────────┐
                    │  Client / REST API     │
                    │  (FastAPI / UI)        │
                    └───────────┬────────────┘
                                │
                                ▼
        ┌──────────────────────────────────────────┐
        │           AI Orchestrator                 │
        │        process_transaction()              │
        └───────────┬──────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
┌───────────────────┐   ┌──────────────────────────┐
│ Risk Detector     │   │ Kafka Consumer            │
│ (Groq → GPT)      │   │ Topic: transactions       │
└─────────┬─────────┘   └──────────────────────────┘
          │
   LOW    │    MEDIUM / HIGH
          │
          ▼
┌──────────────────────────────────────────┐
│ Risk Reasoner (GPT)                       │
│ + Retrieval-Augmented Generation (RAG)   │
└───────────────┬──────────────────────────┘
                │
                ▼
        ┌──────────────────────┐
        │ ChromaDB             │
        │ - Risk Rules         │
        │ - Customer History   │
        └──────────────────────┘
                │
                ▼
┌──────────────────────────────────────────┐
│ Decision Engine                           │
│ ALLOW / BLOCK / ESCALATE                 │
└───────────────┬──────────────────────────┘
                │
        ┌───────┴────────┐
        ▼                ▼
┌──────────────┐  ┌──────────────────┐
│ Kafka Topic  │  │ Logs / Audit Trail│
│ decisions    │  └──────────────────┘
└──────────────┘


---

## 🧩 Core Components

### AI Agents
- **Risk Detector**: Fast classification using Groq (fallback to GPT)
- **Risk Reasoner**: Deep reasoning with explanations using GPT
- **Decision Engine**: Enforces safety rules and escalation

### RAG Layer
- **ChromaDB** for persistent vector storage
- Stores:
  - Risk rules
  - Customer history
  - Compliance notes

### Streaming
- Kafka topics:
  - `transactions` → input
  - `decisions` → AI output

### API
- FastAPI REST interface
- Swagger UI at `/docs`

---

## ⚙️ Tech Stack

- Python 3.10+
- uv (dependency management)
- FastAPI + Uvicorn
- OpenAI + Groq
- ChromaDB
- Kafka (Confluent)
- Docker & Docker Compose

---

## ▶️ Running Locally

### 1. Start Kafka
```bash
docker compose up -d

uv run python -m scripts.seed_chroma

uv run python -m streaming.consumer

uv run uvicorn api.app:app --reload


