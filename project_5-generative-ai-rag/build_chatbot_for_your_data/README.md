# Project 5: Generative AI RAG Chatbot for Private Data (Local Ollama)

This project is part of the IBM Generative AI Engineering Professional Certificate (Course 6, Module 5).

It demonstrates building a fully local Retrieval-Augmented Generation (RAG) chatbot that can upload a PDF and answer questions about its private content using open-source models running via Ollama. No cloud APIs or external LLM services are required.

> **Note**: The original IBM lab used IBM watsonx + Llama models. This version has been refactored to run 100% locally with Ollama for better privacy, reliability, and reproducibility.

## Features

- **PDF Upload & Analysis**: Upload any PDF document for processing.
- **Private RAG Chatbot**: Ask natural language questions about the uploaded document's content.
- **Fully Local Execution**: Uses Ollama for both the LLM and embeddings — all data stays on your machine.
- **Modern LangChain Pipeline**: Document loading, chunking, vector storage (Chroma), and retrieval chain.
- **Simple Web Interface**: Clean Flask + HTML/CSS/JS frontend for chatting.
- **Chat History**: Maintains conversation context.

## Project Structure

```
project_5-generative-ai-rag/build_chatbot_for_your_data/
├── README.md
├── requirements.txt
├── server.py                 # Flask backend
├── worker.py                 # RAG logic + Ollama integration
├── templates/
│   └── index.html
├── static/
│   ├── script.js
│   └── style.css
└── Worker_completed.py       # Reference / original version
```

## Technologies Used

- **Python** + **Flask** (web backend)
- **Ollama** (local LLM & embeddings inference)
- **LangChain** (RAG orchestration, document loading, chains)
- **Chroma** (vector database)
- **PyPDFLoader** + RecursiveCharacterTextSplitter (PDF handling)
- **OllamaEmbeddings** (`nomic-embed-text`)
- **OllamaLLM** (custom GGUF model via Ollama)

## Prerequisites

1. Install [Ollama](https://ollama.com/)
2. Pull the required models:
   ```bash
   ollama pull nomic-embed-text
   ollama pull hf.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF:gemma4-v2-Q8_0.gguf
   ```
   (Or use a standard model like `llama3` or `gemma2` for easier reproducibility.)
3. Python 3.10+ recommended

## Installation

```bash
cd project_5-generative-ai-rag/build_chatbot_for_your_data
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Usage

1. **Start Ollama** (make sure it's running in the background)
2. **Run the Flask server**:
   ```bash
   python server.py
   ```
3. Open your browser to `http://localhost:8000`
4. Upload a PDF using the interface
5. Start asking questions about the document content

The chatbot will retrieve relevant chunks from your PDF and generate answers grounded in the document.

## How It Works (RAG Flow)

1. Upload PDF → `PyPDFLoader` + text splitter creates chunks
2. Embed chunks with `OllamaEmbeddings` → store in Chroma vector DB
3. User question → Retrieve top relevant chunks (MMR)
4. Stuff retrieved context into prompt → `OllamaLLM` generates answer
5. Response returned to the web UI

## Learning Objectives

- Implemented a complete local RAG pipeline for private documents
- Replaced cloud LLM (watsonx) with local Ollama inference
- Built a functional web chatbot with Flask + LangChain
- Gained practical experience with document loaders, vector stores, and retrieval chains

## Original Lab Reference

This implementation is based on the original IBM lab:

```bash
git clone https://github.com/ibm-developer-skills-network/wbphl-build_own_chatbot_without_open_ai.git
```

The original lab used IBM watsonx.ai with Llama models. This refactored version replaces that with a fully local Ollama + LangChain stack while preserving the core learning goals.

## Notes & Improvements

- The implementation uses a custom GGUF model loaded via Ollama. For most users, switching to a standard model like `llama3` or `gemma2` in `worker.py` is recommended for easier setup.
- `langchain_classic` imports are used for compatibility; future updates can migrate fully to current LangChain patterns.
- This local version provides better privacy and avoids API key / quota issues from the original lab.

Original IBM lab source (for reference): IBM Generative AI Engineering Certificate - Course 6, Module 5