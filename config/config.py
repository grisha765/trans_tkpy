import os

class Config:
    log_level: str = "INFO"
    get_coords: str = "hyprctl cursorpos |  sed 's/,//g'"
    trans_lang: str = "ru"
    
    @classmethod
    def load_from_env(cls):
        for key, value in cls.__annotations__.items():
            env_value = os.getenv(key.upper())
            if env_value is not None:
                if isinstance(value, int):
                    setattr(cls, key, int(env_value))
                elif isinstance(value, list):
                    setattr(cls, key, env_value.split(","))
                else:
                    setattr(cls, key, env_value)
    @classmethod
    def coords_var(cls):
        with os.popen(cls.get_coords) as stream:
            result = stream.read().strip()
        return result

Config.load_from_env()

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
