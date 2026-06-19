# Project 3: Voice Assistant with LLM and Speech Capabilities

This project is part of the IBM Generative AI Engineering Professional Certificate (Course 6: Building Generative AI-Powered Applications with Python).

It demonstrates building a voice-enabled AI assistant using Flask, supporting both text and voice input/output, integrated with speech-to-text (STT), a Large Language Model for intelligence, and text-to-speech (TTS).

## Features

- **Dual Input Support**: Text messages or voice recording via browser microphone.
- **Voice Output**: Spoken responses using TTS.
- **Flask Backend**: Handles requests, processes audio, and coordinates STT → LLM → TTS pipeline.
- **Docker Support**: Containerized deployment for consistent environments.
- **Modern UI**: Light/dark mode toggle and responsive interface.

## Project Files

- `server.py` – Main Flask application (routes and orchestration).
- `worker.py` – Background worker for processing tasks.
- `Dockerfile` – Container configuration.
- `requirements.txt` – Python dependencies.
- `templates/index.html` – Frontend interface.
- `static/` – CSS, JS, and assets.
- `models/` – STT and TTS model configurations (lab-specific).

## Installation

```bash
# Clone the repo
git clone https://github.com/shainemeister/ibm-generative-ai-applications.git
cd ibm-generative-ai-applications/project_3-voice-assistant

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Local Development
```bash
python server.py
```
Open `http://localhost:5000` in your browser.

### Docker Deployment
```bash
docker build -t voice-assistant .
docker run -p 5000:5000 voice-assistant
```


**Note**: Full voice functionality (STT/TTS) requires IBM Watson service credentials, which are provided in the Coursera lab environment. For a fully local version using Ollama + open-source speech models, see the "Local Portfolio Adaptation" section below.

## Screenshots

*(Add screenshots here after running the app — e.g., UI with voice recording, conversation flow)*

## Technologies Used

- Python + Flask
- IBM Watson Speech-to-Text (STT) & Text-to-Speech (TTS)
- OpenAI GPT-3 (or compatible LLM)
- Docker for containerization
- HTML, CSS, JavaScript (frontend with microphone access)

## Learning Objectives Achieved

- Built a full-stack voice-enabled AI assistant.
- Integrated Speech-to-Text and Text-to-Speech services.
- Orchestrated multi-step pipeline: Voice Input → Transcription → LLM Reasoning → Spoken Output.
- Containerized the application with Docker.
- Developed a responsive web interface for voice/text interaction.
