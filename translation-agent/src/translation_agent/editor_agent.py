# src/translation_agent/editor_agent.py
# from src.translation_agent.prompt_templates import PROMPTS
# from src.translation_agent.utils import get_completion

from .prompt_templates import PROMPTS
from .utils import get_completion

class EditorAgent:
    """
    编辑智能体：根据反思建议优化翻译结果。
    """
    def run(self, source_lang: str, target_lang: str, original_text: str, translation: str, suggestions: str) -> str:
        system_msg = PROMPTS["editor"]["system"].format(
            source_lang=source_lang, target_lang=target_lang
        )
        prompt = PROMPTS["editor"]["user"].format(
            source_lang=source_lang,
            target_lang=target_lang,
            source_text=original_text,
            translation=translation,
            suggestions=suggestions
        )
        return get_completion(prompt, system_message=system_msg)
