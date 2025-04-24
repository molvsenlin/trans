# app/translator_ui.py

import gradio as gr

def create_ui(translate_function):
    """
    创建 Gradio 界面
    """
    interface = gr.Interface(
        fn=translate_function,
        inputs=[
            gr.inputs.Dropdown(["English", "Chinese", "French", "Spanish"], label="Source Language"),
            gr.inputs.Dropdown(["English", "Chinese", "French", "Spanish"], label="Target Language"),
            gr.inputs.Textbox(lines=5, placeholder="Enter text to translate...", label="Text to Translate")
        ],
        outputs=[
            gr.outputs.Textbox(label="Final Translation")
        ],
        title="Multi-Agent Translation Platform",
        description="This platform uses multiple AI agents to translate, review, and edit text."
    )
    return interface
