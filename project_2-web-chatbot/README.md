# Project 2: Web Chatbot

---

This project is part of the IBM Generative AI Engineering Professional Certificate (Course 6: Building Generative AI-Powered Applications with Python).

It demonstrates building a conversational AI chatbot similar to ChatGPT using open-source Large Language Models (LLMs) from Hugging Face, with conversation history management, and integrating it into a web interface using Flask.

## Features

- **Terminal Chatbot**: Interactive command-line chatbot powered by open-source LLMs.
- **Conversation History**: Maintains recent context (last several turns) for coherent multi-turn conversations.
- **Multiple Model Support**: Includes implementations for both seq2seq (BlenderBot) and modern causal chat models (SmolLM2).
- **Web Integration (In Progress)**: Flask backend + frontend for browser-based chatting (planned next step).

## Project Files

- `chatbot.py` – Terminal chatbot using `facebook/blenderbot-400M-distill`
- `chatbot_llm.py` – Terminal chatbot using `HuggingFaceTB/SmolLM2-360M-Instruct` with proper chat templates and system prompt
- `requirements.txt` – Python dependencies for the project

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### 1. Terminal Chatbot (BlenderBot)
```bash
python chatbot.py
```
Type messages and press Enter. Type `exit` to quit. Maintains short conversation history.

### 2. Terminal Chatbot (SmolLM2 - Recommended for modern chat format)
```bash
python chatbot_llm.py
```
Uses structured chat roles and apply_chat_template. Type `exit` to quit.

### 3. Web Chatbot Interface (Coming Next)
Flask-powered web application with a simple HTML/JS frontend that communicates with the backend LLM.

## Screenshots

**Terminal Chatbot Demo**

*(Screenshots to be added after web interface completion)*

## Technologies Used

- Python
- Hugging Face Transformers
- PyTorch
- (Planned) Flask for web backend
- HTML/CSS/JavaScript for frontend

## Learning Objectives Achieved

- Loaded and initialized open-source LLMs and tokenizers from Hugging Face.
- Implemented conversation history management to provide context to the model.
- Generated responses with controlled sampling parameters for natural dialogue.
- Built foundation for integrating the chatbot into a Flask web application.