# src/translation_agent/translator_agent.py
# from src.translation_agent.prompt_templates import PROMPTS
# from src.translation_agent.utils import get_completion
from .prompt_templates import PROMPTS
from .utils import get_completion
class TranslatorAgent:
    """
    负责从源语言翻译到目标语言的智能体。
    """
    def run(self, source_lang: str, target_lang: str, text: str, country: str = "") -> str:
        system_msg = PROMPTS["translator"]["system"].format(
            source_lang=source_lang, target_lang=target_lang, country=country
        )
        prompt = PROMPTS["translator"]["user"].format(
            source_lang=source_lang, target_lang=target_lang, text=text, country=country
        )
        return get_completion(prompt, system_message=system_msg)
