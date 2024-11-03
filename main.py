from config.config import Config
from config import logging_config
logging = logging_config.setup_logging(__name__)

logging.info(f"Script initialization, logging level: {Config.log_level}")
logging.debug(f"coords: {Config.coords_var()}")
logging.debug(f"lang: {Config.trans_lang}")

if __name__ == '__main__':
    from core.window import window
    root = window()
    root.mainloop()
