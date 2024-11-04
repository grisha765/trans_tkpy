from evdev import InputDevice, categorize, ecodes, list_devices
import select
from config.config import Config
from config import logging_config
logging = logging_config.setup_logging(__name__)

def find_keyboard(active_device):
    def find_all_keyboard_devices():
        devices = [InputDevice(path) for path in list_devices()]
        keyboards = []
        for device in devices:
            capabilities = device.capabilities().get(ecodes.EV_KEY, [])
            if ecodes.KEY_A in capabilities and ecodes.KEY_Z in capabilities:
                keyboards.append(device)
        return keyboards

    keyboard_devices = find_all_keyboard_devices()
    if not keyboard_devices:
        logging.error("No keyboard devices found.")
    else:
        device_info = "\n".join(f" - {device.name} at {device.path}" for device in keyboard_devices)
        logging.debug(f"Detected keyboard devices:\n{device_info}")

        while not active_device["keyboard"]:
            r, _, _ = select.select(keyboard_devices, [], [])
            for device in r:
                for event in device.read():
                    if event.type == ecodes.EV_KEY:
                        active_device["keyboard"] = device
                        break
                if active_device["keyboard"]:
                    break

        logging.info(f"Active keyboard detected: {active_device['keyboard'].name} at {active_device['keyboard'].path}")

def key_daemon(active_device):
    keys = Config.keys
    logging.debug(f"Set keys: {keys}")
    key_states = {key: False for key in keys}
    for event in active_device.read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            if key_event.keystate == key_event.key_down:
                #print(f"Key pressed: {key_event.keycode}")
                pass
            elif key_event.keystate == key_event.key_up:
                #print(f"Key released: {key_event.keycode}")
                pass

            if key_event.keystate == key_event.key_down:
                if key_event.keycode in key_states:
                    key_states[key_event.keycode] = True
                if all(key_states.values()):
                    logging.debug(f"{' + '.join(keys)} pressed")
                    return True

            elif key_event.keystate == key_event.key_up:
                if key_event.keycode in key_states:
                    key_states[key_event.keycode] = False

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
