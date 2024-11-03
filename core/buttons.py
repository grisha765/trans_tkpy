from config import logging_config
logging = logging_config.setup_logging(__name__)

def switch_source(use_primary, source_button, update_translation):
    if use_primary["use"] == True:
        use_primary["use"] = False
    else:
        use_primary["use"] = True
    source_button.config(text="Clipboard" if use_primary["use"] else "Primary")
    logging.debug(f"use primary: {use_primary["use"]}")
    update_translation()

def on_copy_click(root, subprocess, translated_text):
    subprocess.call(["wl-copy", f"{translated_text}"])
    root.destroy()

def on_close_click(root):
    root.destroy()

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
