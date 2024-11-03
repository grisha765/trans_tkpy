import subprocess
import tkinter as tk
from tkinter import messagebox
from core.buttons import switch_source, on_copy_click, on_close_click
from core.clipboard import get_clipboard_text, get_clipboard_primary_text
from trans.base import translate_text, update_translation
from config.config import Config
from config import logging_config
logging = logging_config.setup_logging(__name__)

use_primary = {"use": True}

def window():
    root = tk.Tk()
    root.title("Text Translator")
    root.overrideredirect(True)
    x, y = map(int, Config.trans_coords().split())
    logging.debug(f"Window coords: x:{x}, y:{y}")
    root.geometry(f"+{x}+{y}")

    text = get_clipboard_primary_text(messagebox, subprocess) if use_primary else get_clipboard_text(messagebox, subprocess)
    if not text:
        import sys
        messagebox.showwarning("Warning", "No text found in clipboard.")
        root.destroy()
        sys.exit()

    out_text = translate_text(str(text))
    if "Error request:" in str(out_text):
        import sys
        messagebox.showwarning("Error", f"{out_text}")
        root.destroy()
        sys.exit()

    wraplength = root.winfo_screenwidth() // 2

    translation_label = tk.Label(root, text=out_text, wraplength=wraplength, justify="left")
    translation_label.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)

    copy_button = tk.Button(button_frame, text="Copy",
                            command=lambda: on_copy_click(root,
                                                          subprocess,
                                                          out_text))
    copy_button.pack(side=tk.LEFT, padx=5)

    source_button = tk.Button(button_frame, text="Clipboard",
                              command=lambda: switch_source(use_primary,
                                                            source_button,
                                                            lambda: update_translation(root,
                                                                                       messagebox,
                                                                                       subprocess,
                                                                                       use_primary,
                                                                                       translation_label)))
    source_button.pack(side=tk.LEFT, padx=5)

    close_button = tk.Button(button_frame, text="Close", command=lambda: on_close_click(root))
    close_button.pack(side=tk.LEFT, padx=5)

    def start_move(event):
        root.x = event.x
        root.y = event.y

    def stop_move(event):
        root.x = None
        root.y = None

    def on_motion(event):
        deltax = event.x - root.x
        deltay = event.y - root.y
        x = root.winfo_x() + deltax
        y = root.winfo_y() + deltay
        root.geometry(f"+{x}+{y}")

    translation_label.bind("<ButtonPress-1>", start_move)
    translation_label.bind("<ButtonRelease-1>", stop_move)
    translation_label.bind("<B1-Motion>", on_motion)
    return root

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")

