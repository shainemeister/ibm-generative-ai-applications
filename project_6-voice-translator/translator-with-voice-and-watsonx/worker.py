"""Worker module for the Babel Fish voice translator assistant.
Handles Speech-to-Text (STT), Text-to-Speech (TTS), and Watsonx LLM translation processing.
"""

import requests

from ibm_watson_machine_learning.foundation_models.utils.enums import DecodingMethods
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

# Placeholder for Watsonx API key and Project ID in case you need to use the code outside this environment.
# API_KEY = "Your WatsonX API"
PROJECT_ID = "skills-network"

# Define the credentials
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com"
    # "apikey": API_KEY
}

# Specify MODEL_ID that will be used for inferencing
MODEL_ID = "mistralai/mistral-medium-2505"

# Define the model parameters
parameters = {
    GenParams.DECODING_METHOD: DecodingMethods.GREEDY,
    GenParams.MIN_NEW_TOKENS: 1,
    GenParams.MAX_NEW_TOKENS: 1024
}

# Define the LLM
model = Model(
    model_id=MODEL_ID,
    params=parameters,
    credentials=credentials,
    project_id=PROJECT_ID
)

def speech_to_text(audio_binary):
    """Convert binary audio input to text using the Watson Speech-to-Text API."""
    # Set up Watson Speech-to-Text HTTP API URL
    base_url = '...'
    api_url = base_url + '/speech-to-text/api/v1/recognize'

    # Set up parameters for our HTTP request
    params = {
        'model': 'en-US_Multimedia',
    }

    # Send a HTTP POST request
    response = requests.post(api_url, params=params, data=audio_binary, timeout=30).json()

    # Parse the response to get our transcribed text
    text = 'null'
    if bool(response.get('results')):
        print('Speech-to-Text response:', response)
        text = response.get('results').pop().get('alternatives').pop().get('transcript')
        print('recognised text: ', text)
    return text

def text_to_speech(text, voice=""):
    """Convert text to speech audio using the Watson Text-to-Speech API."""
    # Set up Watson Text-to-Speech HTTP API URL
    base_url = '...'
    api_url = base_url + '/text-to-speech/api/v1/synthesize?output=output_text.wav'

    # Adding voice parameter in api_url if the user has selected a preferred voice
    if voice not in ("", "default"):
        api_url += "&voice=" + voice

    # Set the headers for our HTTP request
    headers = {
        'Accept': 'audio/wav',
        'Content-Type': 'application/json',
    }

    # Set the body of our HTTP request
    json_data = {
        'text': text,
    }

    # Send a HTTP POST request to Watson Text-to-Speech Service
    response = requests.post(api_url, headers=headers, json=json_data, timeout=30)
    print('Text-to-Speech response:', response)
    return response.content

def watsonx_process_message(user_message):
    """Process the user message with the Watsonx LLM for translation to Spanish."""
    # Set the prompt for Watsonx API - using a strict translation instruction
    prompt = f"""
        Translate the following English sentence into Spanish. 
        Reply ONLY with the translation, no explanations, no formatting, no extra text.

        English: {user_message}
        Spanish:
    """
    response_text = model.generate_text(prompt=prompt)
    print("wastonx response:", response_text)
    return response_text.strip()
