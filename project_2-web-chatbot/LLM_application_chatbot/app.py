"""
Simple Flask application that serves as a backend for a web-based chatbot.
The application uses the Hugging Face Transformers library and chatbot model(s).
"""
import json
from flask import Flask, request, render_template
from flask_cors import CORS
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)
CORS(app)

MODEL_NAME = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
conversation_history = []

@app.route('/', methods=['GET'])
def home():
    """Serve the main page of the chatbot application."""
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    """Handle incoming prompts from the frontend, 
    generate responses using the chatbot model, 
    and maintain conversation history."""
    data = request.get_data(as_text=True)
    data = json.loads(data)
    print(data) # DEBUG
    input_text = data['prompt']

	# Create conversation history string
    history = "\n".join(conversation_history)

	# Tokenize the input text and history
    inputs = tokenizer.encode_plus(history, input_text, return_tensors="pt")

    # Generate the response from the model
    outputs = model.generate(**inputs)

	# Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

	# Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)

    return response

if __name__ == '__main__':
    app.run()
