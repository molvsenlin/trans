# import sys
# import os

# # 将 src 目录添加到 sys.path 中
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


# import shutil
# import tempfile
# import gradio as gr
# from translation_agent.agent_manager import AgentManager
# from file_handler import extract_text_from_pdf, extract_text_from_word  # type: ignore


# # 初始化 AgentManager
# manager = AgentManager()

# def translate_text(source_lang, target_lang, text):
#     """翻译文本"""
#     final_translation = manager.translate(source_lang, target_lang, text)
#     return final_translation

# def handle_file_upload_and_translate(file, source_lang, target_lang, input_text):
#     """处理文件上传并进行翻译"""
#     # 如果有上传的文件，优先处理文件
#     if file is not None:
#         # 检查文件类型并提取文本
#         if file.name.endswith('.pdf'):
#             text = extract_text_from_pdf(file.name)
#         elif file.name.endswith('.docx'):
#             text = extract_text_from_word(file.name)
#         else:
#             return "Unsupported file format. Please upload a PDF or Word document."
#     elif input_text:
#         # 如果没有上传文件，使用用户输入的文本
#         text = input_text
#     else:
#         return "Please provide text either by uploading a document or entering text."

#     # 调用翻译功能
#     translated_text = translate_text(source_lang, target_lang, text)
#     return translated_text

# # 定义界面的样式
# css = """
#     .container {
#         max-width: 800px;
#         margin: 0 auto;
#         padding: 20px;
#         background-color: #f9f9f9;
#         border-radius: 10px;
#         box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
#     }
#     .gradio-container {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         height: 100vh;
#         font-family: Arial, sans-serif;
#     }
#     .gradio-row {
#         padding: 10px 0;
#     }
#     .gradio-button {
#         background-color: #007bff;
#         color: white;
#         border-radius: 8px;
#         padding: 12px;
#         border: none;
#         font-size: 16px;
#     }
#     .gradio-button:hover {
#         background-color: #0056b3;
#     }
#     .gr-textbox {
#         border-radius: 8px;
#         padding: 10px;
#         font-size: 14px;
#     }
#     .gr-dropdown {
#         border-radius: 8px;
#     }
# """

# # 创建 Gradio 界面
# interface = gr.Interface(
#     fn=handle_file_upload_and_translate,
#     inputs=[
#         gr.File(label="Upload a Word or PDF document (optional)", file_count="single", type="filepath", elem_id="file-upload"),  # 文件上传（可选）
#         gr.Dropdown(["English", "Chinese", "French", "Spanish"], label="Source Language", elem_id="source-lang"),  # 源语言
#         gr.Dropdown(["English", "Chinese", "French", "Spanish"], label="Target Language", elem_id="target-lang"),  # 目标语言
#         gr.Textbox(lines=5, placeholder="Enter text to translate...", label="Text to Translate (optional)", elem_id="input-text")  # 文本输入（可选）
#     ],
#     outputs=gr.Textbox(label="Translated Text", elem_id="output-text"),  # 翻译结果输出
#     title="🌐 Multi-Agent Translation Platform",
#     description="This platform uses multiple AI agents to translate, review, and edit text. You can upload a document or enter text directly to get a translation.",
#     css=css
# )

# # 启动 Gradio 应用
# if __name__ == "__main__":
#     interface.launch()
















# import sys
# import os

# # 将 src 目录添加到 sys.path 中
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


# import shutil
# import tempfile
# import gradio as gr
# from translation_agent.agent_manager import AgentManager
# from file_handler import extract_text_from_pdf, extract_text_from_word  # type: ignore
# # app/app.py


# # 初始化 AgentManager
# manager = AgentManager()

# def translate_text(source_lang, target_lang, text):
#     """翻译文本"""
#     final_translation = manager.translate(source_lang, target_lang, text)
#     return final_translation

# def handle_file_upload_and_translate(file, source_lang, target_lang, input_text):
#     """处理文件上传并进行翻译"""
#     # 如果有上传的文件，优先处理文件
#     if file is not None:
#         # 检查文件类型并提取文本
#         if file.name.endswith('.pdf'):
#             text = extract_text_from_pdf(file.name)
#         elif file.name.endswith('.docx'):
#             text = extract_text_from_word(file.name)
#         else:
#             return "Unsupported file format. Please upload a PDF or Word document."
#     elif input_text:
#         # 如果没有上传文件，使用用户输入的文本
#         text = input_text
#     else:
#         return "Please provide text either by uploading a document or entering text."

#     # 调用翻译功能
#     translated_text = translate_text(source_lang, target_lang, text)
#     return translated_text

# # 创建 Gradio 界面
# interface = gr.Interface(
#     fn=handle_file_upload_and_translate,
#     inputs=[
#         gr.File(label="Upload a Word or PDF document (optional)"),  # 文件上传（可选）
#         gr.Dropdown(["English", "Chinese", "French", "Spanish"], label="Source Language"),  # 源语言
#         gr.Dropdown(["English", "Chinese", "French", "Spanish"], label="Target Language"),  # 目标语言
#         gr.Textbox(lines=5, placeholder="Enter text to translate...", label="Text to Translate (optional)")  # 文本输入（可选）
#     ],
#     outputs=gr.Textbox(label="Translated Text"),  # 翻译结果输出
#     title="Multi-Agent Translation Platform",
#     description="This platform uses multiple AI agents to translate, review, and edit text. You can upload a document or enter text directly."
# )

# # 启动 Gradio 应用
# if __name__ == "__main__":
#     interface.launch()




import sys
import os
import shutil
import tempfile
import gradio as gr

# 将 src 目录添加到 sys.path 中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from translation_agent.agent_manager import AgentManager
from file_handler import extract_text_from_pdf, extract_text_from_word  # type: ignore

manager = AgentManager()

def handle_file_upload_and_translate(file, source_lang, target_lang, input_text, history):
    """
    处理输入并翻译，同时更新并返回历史记录。
    history: 存储为 List[Tuple[原文, 译文]]
    """
    # 确定待翻译文本
    if file is not None:
        # 同前：大小检查、临时复制、提取
        if os.path.getsize(file.name) > 10 * 1024 * 1024:
            return history, "文件过大（>10MB）。"
        tmp_dir = tempfile.mkdtemp()
        tmp_path = os.path.join(tmp_dir, os.path.basename(file.name))
        shutil.copy(file.name, tmp_path)
        try:
            if file.name.lower().endswith('.pdf'):
                text = extract_text_from_pdf(tmp_path)
            else:
                text = extract_text_from_word(tmp_path)
        finally:
            shutil.rmtree(tmp_dir, ignore_errors=True)
    elif input_text and input_text.strip():
        text = input_text.strip()
    else:
        return history, "请提供文本或上传文件。"

    # 翻译
    translated = manager.translate(source_lang, target_lang, text)

    # 更新历史：在最前面插入
    history = history or []
    history.insert(0, (f"[{source_lang}] {text}", f"[{target_lang}] {translated}"))

    # 构造要显示的多行历史字符串
    history_str = "\n\n".join([f"原文：{orig}\n译文：{trans}" for orig, trans in history])

    return history, history_str

with gr.Blocks(css=None) as demo:
    # 用于存储历史的 State
    history = gr.State([])

    gr.Markdown("## 🌐 Multi-Agent Translation Platform with History")

    with gr.Row():
        file_input = gr.File(label="Upload Word/PDF (optional)", type="filepath")
        src_lang = gr.Dropdown(["English", "Chinese", "French", "Spanish"], label="Source Language")
        tgt_lang = gr.Dropdown(["English", "Chinese", "French", "Spanish"], label="Target Language")

    input_text = gr.Textbox(lines=3, placeholder="Or enter text to translate...", label="Text Input")
    translate_btn = gr.Button("Translate", elem_id="translate-btn", variant="primary")

    output = gr.Textbox(label="Translation Output", interactive=False)
    history_box = gr.Textbox(label="Translation History", interactive=False)

    # 点击按钮时调用，并更新 output 与 history_box
    translate_btn.click(
        fn=handle_file_upload_and_translate,
        inputs=[file_input, src_lang, tgt_lang, input_text, history],
        outputs=[history, history_box]
    )

if __name__ == "__main__":
    demo.launch(share=True)