# tests/test_translation.py

import unittest
from src.translation_agent.agent_manager import AgentManager

class TestTranslation(unittest.TestCase):

    def setUp(self):
        self.manager = AgentManager()

    def test_translation(self):
        input_text = "The quick brown fox."
        src_lang = "English"
        tgt_lang = "Chinese"
        result = self.manager.translate(src_lang, tgt_lang, input_text)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)  # 确保返回了翻译结果

if __name__ == "__main__":
    unittest.main()
