import urllib.parse
import requests
from config.config import Config
from core.clipboard import get_clipboard_text, get_clipboard_primary_text
from config import logging_config
logging = logging_config.setup_logging(__name__)

def translate_text(text):
    in_lang = Config.in_trans_lang
    out_lang = Config.out_trans_lang
    logging.debug(f"In trans lang: {in_lang}")
    logging.debug(f"Out trans lang: {out_lang}")
    logging.debug(f"In text: {text}")
    text = urllib.parse.quote(text)
    try:
        response = requests.get(f"{Config.lingva_url}/api/v1/{in_lang}/{out_lang}/{text}", timeout=int(Config.request_timeout))
        if response.status_code == 200:
            data = response.json().get("translation", "Translate not found")
            logging.debug(f"Out text: {data}")
            return data
        else:
            msg = f"Error request: {response.status_code}"
            logging.error(msg)
            return msg
    except requests.Timeout:
        msg = f"Error request: Request timed out"
        logging.error(msg)
        return msg
    except requests.RequestException as e:
        msg = f"Error request: {e}"
        logging.error(msg)
        return msg

def update_translation(root, messagebox, subprocess, use_primary, translation_label):
    text = get_clipboard_primary_text(messagebox, subprocess) if use_primary["use"] else get_clipboard_text(messagebox, subprocess)
    if not text:
        import sys
        messagebox.showwarning("Warning", "No text found in clipboard.")
        root.destroy()
        sys.exit()
    translated_text = translate_text(str(text))
    translation_label.config(text=translated_text)

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
