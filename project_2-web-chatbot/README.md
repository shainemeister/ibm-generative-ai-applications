# Project 2: Web Chatbot

This project is part of the IBM Generative AI Engineering Professional Certificate (Course 6: Building Generative AI-Powered Applications with Python).

It demonstrates building a conversational AI chatbot similar to ChatGPT using open-source Large Language Models (LLMs) from Hugging Face Transformers, with conversation history management, and a full web interface using Flask (backend + HTML/CSS/JS frontend).

## Features

- **Terminal Chatbot**: Interactive command-line chatbots powered by open-source LLMs (BlenderBot and SmolLM2 variants).
- **Conversation History**: Maintains recent context across turns for more coherent multi-turn conversations.
- **Web Chatbot Application**: Complete Flask-based web app with a polished chat UI, including user/bot avatars, loading indicators, and real-time messaging.
- **Docker Support**: Includes Dockerfile for containerized deployment of the web application.
- **Multiple Model Support**: Ready for both seq2seq and modern instruct/chat models.

## Project Files

- `chatbot.py` – Terminal chatbot using `facebook/blenderbot-400M-distill`
- `chatbot_llm.py` – Terminal chatbot using `HuggingFaceTB/SmolLM2-360M-Instruct` with chat templates
- `flask_app.py` – Basic Flask backend for the chatbot
- `LLM_application_chatbot/` – Full web application:
  - `app.py` – Flask backend with routes for home and chat
  - `templates/index.html` – Chat interface template
  - `static/` – CSS, JavaScript, images (avatars, logos, favicon)
  - `Dockerfile` – Container configuration
  - `requirements.txt` – Dependencies for the web app
- `requirements.txt` – Root dependencies

## Installation

```bash
pip install -r requirements.txt
```

For the full web app, navigate to the `LLM_application_chatbot` directory and use its requirements/Dockerfile as needed.

## Usage

### 1. Terminal Chatbot (BlenderBot)
```bash
python chatbot.py
```

### 2. Terminal Chatbot (SmolLM2)
```bash
python chatbot_llm.py
```

### 3. Web Chatbot (Flask)
```bash
cd LLM_application_chatbot
python app.py
```
Then open http://127.0.0.1:5000 in your browser. The interface supports sending messages and displays responses with avatars and loading states.

Docker usage (from within `LLM_application_chatbot`):
```bash
docker build -t llm-chatbot .
docker run -p 5000:5000 llm-chatbot
```

## Screenshots

**Web Chatbot Interface**

*(Add screenshots of the running Flask chat UI here)*

**Terminal Chatbot Demo**

*(Optional terminal screenshots)*

## Technologies Used

- Python
- Hugging Face Transformers + PyTorch
- Flask + Flask-CORS
- HTML, CSS, JavaScript (vanilla)
- Docker (for deployment)

## Learning Objectives Achieved

- Loaded and ran open-source conversational LLMs from Hugging Face.
- Implemented conversation history management for context-aware responses.
- Built a full-stack web chatbot with Flask backend and interactive frontend.
- Created a containerized deployment option with Docker.
- Integrated frontend JavaScript with backend LLM inference in real time.