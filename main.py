import tkinter as tk
from tkinter import messagebox
from deep_translator import GoogleTranslator
import subprocess
import sys

def get_clipboard_text():
    try:
        return subprocess.check_output(["wl-paste"]).decode("utf-8").strip()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get clipboard text: {e}")
        return ""

def get_clipboard_primary_text():
    try:
        return subprocess.check_output(["wl-paste", "--primary"]).decode("utf-8").strip()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get clipboard text: {e}")
        return ""

def switch_source():
    global use_primary
    use_primary = not use_primary
    source_button.config(text="Clipboard" if use_primary else "Primary")
    update_translation()

def translate_text(text, target_lang):
    translated_text = GoogleTranslator(source='auto', target=f'{target_lang}').translate(f"{text}")
    return translated_text

def update_translation():
    global translated_text
    text = get_clipboard_primary_text() if use_primary else get_clipboard_text()
    if not text:
        messagebox.showwarning("Warning", "No text found in clipboard.")
        root.destroy()
        sys.exit()
    translated_text = translate_text(str(text), str(lang_arg))
    translation_label.config(text=translated_text)

def on_copy_click():
    subprocess.call(["wl-copy", f"{translated_text}"])
    root.destroy()

def on_close_click():
    root.destroy()

x, y = sys.argv[2], sys.argv[3]
    
root = tk.Tk()
root.title("Text Translator")
root.overrideredirect(True)
root.geometry(f"+{x}+{y}")
#root.maxsize(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2)

use_primary = True
lang_arg = sys.argv[1] if len(sys.argv) > 1 else 'en'
text = get_clipboard_primary_text() if use_primary else get_clipboard_text()
if not text:
    messagebox.showwarning("Warning", "No text found in clipboard.")
    root.destroy()
    sys.exit()

translated_text = translate_text(str(text), str(lang_arg))

wraplength = root.winfo_screenwidth() // 2

translation_label = tk.Label(root, text=translated_text, wraplength=wraplength, justify="left")
translation_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

copy_button = tk.Button(button_frame, text="Copy", command=on_copy_click)
copy_button.pack(side=tk.LEFT, padx=5)

source_button = tk.Button(button_frame, text="Clipboard", command=switch_source)
source_button.pack(side=tk.LEFT, padx=5)

close_button = tk.Button(button_frame, text="Close", command=on_close_click)
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

root.mainloop()
