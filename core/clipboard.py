def get_clipboard_text(messagebox, subprocess):
    try:
        return subprocess.check_output(["wl-paste"]).decode("utf-8").strip()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get clipboard text: {e}")
        return ""

def get_clipboard_primary_text(messagebox, subprocess):
    try:
        return subprocess.check_output(["wl-paste", "--primary"]).decode("utf-8").strip()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get clipboard text: {e}")
        return ""

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
