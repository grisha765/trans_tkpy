from deep_translator import GoogleTranslator
from config.config import Config
import sys
from core.clipboard import get_clipboard_text, get_clipboard_primary_text

def translate_text(text):
    translated_text = GoogleTranslator(source='auto', target=Config.trans_lang).translate(text)
    return translated_text

def update_translation(root, messagebox, subprocess, use_primary, translation_label):
    text = get_clipboard_primary_text(messagebox, subprocess) if use_primary["use"] else get_clipboard_text(messagebox, subprocess)
    if not text:
        messagebox.showwarning("Warning", "No text found in clipboard.")
        root.destroy()
        sys.exit()
    translated_text = translate_text(str(text))
    translation_label.config(text=translated_text)

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
