"""
This is a simple web app for generating captions for images using a trained model.
"""

import gradio as gr

def greet(name):
    """Greet the user by name."""
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch(server_name="0.0.0.0", server_port= 7860)
