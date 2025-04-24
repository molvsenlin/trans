# src/translation_agent/agent_manager.py
# from src.translation_agent.translator_agent import TranslatorAgent
# from src.translation_agent.reflector_agent import ReflectorAgent
# from src.translation_agent.editor_agent import EditorAgent

from translation_agent.translator_agent import TranslatorAgent
from translation_agent.reflector_agent import ReflectorAgent
from translation_agent.editor_agent import EditorAgent

class AgentManager:
    def __init__(self):
        self.translator = TranslatorAgent()
        self.reflector = ReflectorAgent()
        self.editor = EditorAgent()

    def translate(self, source_lang, target_lang, text):
        # 1. 翻译
        t1 = self.translator.run(source_lang, target_lang, text)
        # 2. 反思
        r = self.reflector.run(source_lang, target_lang, text, t1)
        # 3. 编辑
        t2 = self.editor.run(source_lang, target_lang, text, t1, r)
        return t2
