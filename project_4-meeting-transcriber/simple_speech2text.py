"""
Simpmle Speech-to-Text Transcription using Hugging Face Transformers
"""
import os
import sys
from transformers import pipeline
import requests

# URL of the audio file to be downloaded and
# send a GET request to the URL to download the file
URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMSkillsNetwork-GPXX04C6EN/Testing%20speech%20to%20text.mp3"
); response = requests.get(URL, timeout=10)

# Define the local file path where the audio file will be saved
AUDIO_FILE_PATH = "downloaded_audio.mp3"

# Check for .mp3 file exist in the current directory before downloading the file
if os.path.exists(AUDIO_FILE_PATH):
    print("File already exists")
elif response.status_code == 200:
    # Check if the request was successful (status code 200)
    # If successful, write the content to the specified local file path
    with open(AUDIO_FILE_PATH, "wb") as file:
        file.write(response.content)
    print("File downloaded successfully")
else:
    # If the request failed, print an error message
    print("Failed to download the file")
    sys.exit()

# Initialize the speech-to-text pipeline from Hugging Face Transformers
# This uses the "openai/whisper-tiny.en" model for automatic speech recognition (ASR)
# The `chunk_length_s` parameter specifies the chunk length in seconds for processing
pipe = pipeline(
  "automatic-speech-recognition",
  model="openai/whisper-tiny.en",
  chunk_length_s=30,
)

# Perform speech recognition on the audio file
# The `batch_size=8` parameter indicates how many chunks are processed at a time
# The result is stored in `prediction` with the key "text" containing the transcribed text
prediction = pipe(AUDIO_FILE_PATH, batch_size=8)["text"]

# Print the transcribed text to the console
print(prediction)
