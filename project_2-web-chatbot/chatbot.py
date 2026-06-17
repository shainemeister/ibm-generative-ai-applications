"""
A simple chatbot using the Facebook BlenderBot model.
This chatbot maintains a short conversation history to provide context for responses.
"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Specify the model name from Hugging Face
MODEL_NAME = "facebook/blenderbot-400M-distill"

# Load model and tokenizer from Hugging Face
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
print("Chatbot ready! (type 'exit' to quit)\n")
conversation_history = []

while True:
    # Keep only recent conversation history to fit within model limits
    conversation_history = conversation_history[-6:]
    history_string = "\n".join(conversation_history)

    input_text = input("> ")

    if input_text.lower() == "exit":
        break


    prompt = history_string + f"\nUser: {input_text}\nBot:"

    inputs = tokenizer(
    prompt,
    return_tensors="pt",
    truncation=True,
    max_length=512
    )

    # Generate response with some sampling parameters to make it more conversational
    outputs = model.generate(
        **inputs,
        max_new_tokens=60,
        no_repeat_ngram_size=3,
        repetition_penalty=1.3,
        do_sample=True,
        temperature=0.6,
        top_p=0.85
    )

    # Decode the generated response and clean it up
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    print("Bot:", response)

    # Save bot response and user input to conversation history
    conversation_history.append(f"User: {input_text}")
    conversation_history.append(f"Bot: {response}")
