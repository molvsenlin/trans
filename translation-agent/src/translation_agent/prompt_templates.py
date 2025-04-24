# src/translation_agent/prompt_templates.py
PROMPTS = {
    "translator": {
        "system": "You are a professional translator. Translate from {source_lang} to {target_lang} ({country}).",
        "user": "Please translate the following {source_lang} text into {target_lang} ({country}):\n{text}"
    },
    "reflector": {
        "system": "You are a professional bilingual translation critic, fluent in {source_lang} and {target_lang}.",
        "user": (
            "Original {source_lang} text:\n{source_text}\n\n"
            "Translation in {target_lang}:\n{translation}\n\n"
            "Please critically evaluate the translation. Highlight any issues and give suggestions to improve it."
        )
    },
    "editor": {
        "system": "You are a translation editor, fluent in {source_lang} and {target_lang}.",
        "user": (
            "Original text ({source_lang}):\n{source_text}\n\n"
            "Initial translation ({target_lang}):\n{translation}\n\n"
            "Improvement suggestions:\n{suggestions}\n\n"
            "Please revise the translation based on the suggestions, and return the improved version."
        )
    }
}
