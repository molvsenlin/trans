# src/translation_agent/reflector_agent.py
# from src.translation_agent.prompt_templates import PROMPTS
# from src.translation_agent.utils import get_completion

from .prompt_templates import PROMPTS
from .utils import get_completion

class ReflectorAgent:
    """
    反思智能体：根据原文和译文提出改进建议。
    """
    def run(self, source_lang: str, target_lang: str, original_text: str, translated_text: str) -> str:
        system_msg = PROMPTS["reflector"]["system"].format(
            source_lang=source_lang, target_lang=target_lang
        )
        prompt = PROMPTS["reflector"]["user"].format(
            source_lang=source_lang,
            target_lang=target_lang,
            source_text=original_text,
            translation=translated_text
        )
        return get_completion(prompt, system_message=system_msg)
