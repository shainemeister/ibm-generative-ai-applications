# Project 4: Generative AI-Powered Meeting Assistant (Meeting Transcriber & Summarizer)

This project is part of the **IBM Generative AI Engineering Professional Certificate (Course 6: Building Generative AI-Powered Applications with Python)**.

It demonstrates an end-to-end AI application that transcribes meeting audio recordings and generates concise summaries with key points using **OpenAI Whisper** for speech-to-text and **Llama 2** (hosted on IBM watsonx) for summarization.

## Features

- **Speech-to-Text Transcription**: Uses OpenAI Whisper to accurately transcribe audio files (supports noisy environments and multiple languages).
- **Generative Summarization**: Integrates Llama 2 via IBM watsonx to produce concise summaries and extract key points/decisions.
- **Interactive Gradio Interface**: User-friendly web UI for uploading audio and viewing results instantly.
- **Modular Scripts**:
  - Basic transcription and LLM testing.
  - Full end-to-end analyzer with WatsonxLLM integration.

## Project Files

- `simple_speech2text.py` – Basic Whisper transcription example
- `simple_llm.py` – Basic Llama 2 / WatsonxLLM text generation
- `speech2text_app.py` – Gradio web interface for transcription
- `speech_analyzer.py` – Full pipeline combining Whisper + Llama 2 summarization
- (Additional: requirements.txt, sample audio files if present)

## Installation

```bash
# Recommended: Use Python 3.11 or 3.12 (avoid 3.13 due to pandas compatibility with ibm-watson-machine-learning)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

pip install -U ibm-watson-machine-learning langchain langchain-ibm whisper gradio
# Additional common deps: torch, torchaudio, etc. (see requirements.txt if available)
```

**Note**: Set up IBM watsonx credentials (API key, project ID) for Llama 2 access.

## Usage

### 1. Basic Transcription
```bash
python simple_speech2text.py
```

### 2. Gradio Web App (Recommended)
```bash
python speech2text_app.py
```
Open the local URL (usually http://127.0.0.1:7860).

### 3. Full Speech Analyzer
```bash
python speech_analyzer.py
```

## Technologies Used

- **Python**
- **OpenAI Whisper** — Automatic Speech Recognition (ASR)
- **IBM watsonx + Llama 2** — Generative LLM for summarization & key point extraction
- **Gradio** — Interactive web interface
- **LangChain + ibm-watson-machine-learning** — LLM orchestration
- **WatsonxLLM** — Foundation model integration

## Screenshots

(Add screenshots of the Gradio interface showing upload, transcription, and summary output here.)

## Learning Objectives Achieved

- Implemented Automatic Speech Recognition with OpenAI Whisper.
- Integrated Llama 2 (via IBM watsonx) for text summarization and refinement.
- Built a user-friendly Gradio interface.
- Combined ASR + Generative AI into a complete meeting productivity tool.
- Deployed concepts from watsonx.ai (Prompt Lab, model access) and enterprise AI lifecycle.
