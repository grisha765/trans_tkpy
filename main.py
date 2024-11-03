from core.daemon import key_daemon, find_keyboard
from core.window import window
from config.config import Config
from config import logging_config
import threading, time, sys
logging = logging_config.setup_logging(__name__)
logging.info(f"Script initialization, logging level: {Config.log_level}")

def daemon_listener(active_device):
    find_keyboard(active_device)
    while True:
        if key_daemon(active_device['keyboard']):
            start_window()

def start_window():
    root = window()
    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()

if __name__ == '__main__':
    if "-d" in sys.argv:
        logging.info("Starting in daemon mode")
        active_device = {"keyboard": None}

        daemon_thread = threading.Thread(target=daemon_listener, args=(active_device,))
        daemon_thread.daemon = True
        daemon_thread.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logging.info("Script terminated by user.")
    else:
        logging.info("Starting in standard mode")
        start_window()
