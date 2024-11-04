import os
from typing import get_type_hints

class Config:
    log_level: str = "INFO"
    coords_cmd: str = "echo 0 0" #x=0, y=0
    in_trans_lang: str = "auto"
    out_trans_lang: str = "ru"
    lingva_url: str = "http://golyam.ddns.cam:3000/"
    request_timeout: int = 20
    keys: list = ["KEY_LEFTALT", "KEY_LEFTSHIFT", "KEY_R"]
    
    @classmethod
    def load_from_env(cls):
        type_hints = get_type_hints(cls)
        for key, var_type in type_hints.items():
            env_value = os.getenv(key.upper())
            if env_value is not None:
                if var_type == int:
                    setattr(cls, key, int(env_value))
                elif var_type == list:
                    setattr(cls, key, env_value.split(","))
                else:
                    setattr(cls, key, env_value)
    @classmethod
    def trans_coords(cls):
        try:
            with os.popen(cls.coords_cmd) as proc:
                result = proc.read().strip()
            return result
        except Exception as e:
            print(f"Error executing command '{cls.coords_cmd}': {e}")
            return "0 0"

Config.load_from_env()

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
