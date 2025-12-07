# Trialsense — Pharmacovigilance AI Agents (Starter Repository)

This project provides a clean, modular starter implementation of a multi-agent
pharmacovigilance system. It demonstrates:

- PDF/text ingestion
- Adverse Drug Reaction (ADR) extraction using an LLM
- Validation of ADR reports using an LLM
- A simple FAISS-based vector search pipeline (RAG-style)
- A runnable `main.py` pipeline

This is a lightweight starter version designed for extension into a production-grade PV AI system.

---

## 🚀 Quick Start

### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
