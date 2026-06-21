Update README.md with the following structure and update to reflect the current Project 5 content:
Note: Code has been updated / refactored to make use of Ollama running locally.

# Project 1: Image Captioning with Generative AI

This project is part of the IBM Generative AI Engineering Professional Certificate (Course 6).

It demonstrates building an automated image captioning tool using the BLIP model from Hugging Face Transformers and a user-friendly web interface with Gradio.

## Features

- **Local Directory Captioning**: Processes all images in a folder and generates meaningful captions.
- **URL/Web Scraping Captioning**: Extracts and captions images from any webpage.
- **Interactive Gradio Web App**: Upload images via browser for instant captions.
- Supports both `blip-image-captioning-base` (lightweight) and can be upgraded to Blip2.

## Project Files

- `automate_local_captioner.py` – Batch process local images
- `automate_url_captioner.py` – Caption images from a webpage
- `image_captioning_app.py` – Gradio web interface
- `sample_images/` – Test images
- `myapp/` – Additional app structure (optional)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### 1. Local Captioning
```bash
python automate_local_captioner.py
```
Update `image_dir` in the script to point to your image folder.

### 2. Web/URL Captioning
```bash
python automate_url_captioner.py
```
Update the `URL` variable as needed.

### 3. Gradio Web Interface (Recommended)
```bash
python image_captioning_app.py
```
Open the local URL shown in the terminal (usually http://127.0.0.1:7860).

## Screenshots

**Gradio Interface**

![Image Captioning App](image_captioning_app_screenshot.png)

**Hello World Test App**

![Hello Screenshot](hello_screenshot.png)

## Technologies Used

- Python
- Hugging Face Transformers (BLIP model)
- Gradio
- Pillow (PIL)
- BeautifulSoup + requests (for URL mode)

## Learning Objectives Achieved

- Implemented image captioning with BLIP from Hugging Face.
- Built a user-friendly Gradio interface.
- Adapted the tool for real-world scenarios (local files and web URLs).

---

Original Source Code: `git clone https://github.com/ibm-developer-skills-network/wbphl-build_own_chatbot_without_open_ai.git`