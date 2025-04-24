import sys
import os

# 将 src 目录添加到 sys.path 中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))



# 然后导入模块
from translation_agent.translator_agent import TranslatorAgent
from translation_agent.reflector_agent import ReflectorAgent
from translation_agent.editor_agent import EditorAgent

if __name__ == "__main__":
    translator = TranslatorAgent()
    reflector = ReflectorAgent()
    editor = EditorAgent()

    text = "Language models are transforming AI development."
    t1 = translator.run("English", "Chinese", text)
    print("初步翻译：", t1)

    suggestions = reflector.run("English", "Chinese", text, t1)
    print("翻译反思建议：", suggestions)

    t2 = editor.run("English", "Chinese", text, t1, suggestions)
    print("优化后翻译：", t2)
