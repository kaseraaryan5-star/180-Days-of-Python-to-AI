# 180 Days of Python to AI

My structured journey from Python fundamentals to production-grade AI engineering. I learn one topic at a time, write the code myself, and commit it here.

**Goal:** become a job-ready AI engineer (RAG, agents, fine-tuning, APIs) and land a remote AI engineering internship.

## Roadmap progress

- ✅ **Month 1:** Python core, OOPs, logging, custom exception handling, Docker basics
- ✅ **Month 2:** Git and GitHub, NumPy, Pandas, data cleaning, PyTest
- ✅ **Month 3:** Machine learning, neural networks, backpropagation, transformers
- 🔄 **Month 4 (current):** FastAPI, vector databases, RAG, open-source contributions
- ⏳ **Month 5:** Fine-tuning (LoRA / QLoRA), multi-agent systems (LangGraph, MCP)
- ⏳ **Month 6:** Capstone projects and interview prep

## What I have covered

| Area | Topics |
|---|---|
| Python | Variables, loops, functions, data structures, OOPs (classes, inheritance), file I/O |
| Production habits | Logging (`app.log`), custom exceptions, Git branching, PyTest basics |
| Data | NumPy fundamentals and tricks, Pandas Series and DataFrames, MultiIndex, GroupBy, merging and joining, string and datetime ops |
| Visualisation | Matplotlib (basic and advanced), Seaborn |
| Machine learning | End-to-end ML workflow, EDA (univariate, bivariate), Pandas Profiling, feature engineering, scaling, encoding, ColumnTransformer, sklearn Pipelines |
| Deep learning | Perceptron, MLP, forward propagation, loss functions, gradient descent, backpropagation |
| Transformers | Self-attention, scaled dot-product attention, multi-head attention, positional encoding, layer normalization, encoder, decoder, masked attention, cross attention, inference |
| GenAI | LangChain, vector databases and embeddings (ChromaDB), RAG basics, LoRA / QLoRA fine-tuning of Llama 2 |
| Backend and tools | FastAPI basics, serving ML models with FastAPI, Docker |

## Repository structure

| Folder | Content |
|---|---|
| `01_Python_Basics` | Core Python, file I/O |
| `02_Object_Oriented_Programming` | Classes, inheritance, logging and exception utilities |
| `03_Advanced_Python_&_Logging` | Production-style logging and custom exceptions |
| `04_NumPy` | Array operations and tricks |
| `05_Pandas` | Data cleaning, profiling, analysis |
| `06_Data_Visualisation` | Matplotlib and Seaborn plots |
| `07_Machine_learning.py` | ML pipelines and preprocessing |
| `08_Deep_Learning.py` | Neural networks, backpropagation |
| `09_RAG_Pipeline.py` | Retrieval-augmented generation pipeline |
| `10_Generative_AI_Langchain.py` | LangChain and tool-using agents |
| `11_Fine_Tunning.py` | LoRA fine-tuning experiments |
| `src/` | Reusable source code |

## Related projects

- [learning-fastapi](https://github.com/kaseraaryan5-star/learning-fastapi): FastAPI endpoints (async, caching) in progress
- [docker-testapp](https://github.com/kaseraaryan5-star/docker-testapp): containerizing a Python app with Docker

## Currently building (Month 4)

- [ ] Async FastAPI endpoints with Redis caching
- [ ] Vector DB integration (Qdrant / ChromaDB)
- [ ] Production RAG pipeline with chunking strategies
- [ ] First merged open-source PR

## Setup

```bash
git clone https://github.com/kaseraaryan5-star/180-Days-of-Python-to-AI.git
cd 180-Days-of-Python-to-AI
pip install -r requirements.txt
cp .env.example .env   # then add your own API keys
```

API keys are read from a local `.env` file, which is never committed.

## Connect

[LinkedIn](https://www.linkedin.com/in/aryan-kasera-ai) | [X @KaseraAryan](https://x.com/KaseraAryan)