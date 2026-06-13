"""
Gradio Demo Script
This script is part of IBM Generative AI Applications project.
"""
import gradio as gr

def greet(name, intensity):
    """
    A simple greeting function with basic parameters to generate a greeting message.
    """
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch(server_name="0.0.0.0", server_port= 7860)
