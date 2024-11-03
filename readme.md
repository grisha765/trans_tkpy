# trans_tkpy
This Python script enables quick translation of text from the primary clipboard to a specified language. It utilizes the Google Translate API for translation and tkinter for the graphical user interface. The script automatically detects the language of the text in the clipboard and translates it to the specified target language.

### Demo

![Translate RU to EN](.github/assets/demo.gif)

### Build

1. **Clone the repository**: Clone this repository using `git clone`.
2. **Create Virtual Env**: Create a Python Virtual Env `venv` to download the required dependencies and libraries.
3. **Download Dependencies**: Download the required dependencies into the Virtual Env `venv` using `pip`.
4. **Download dependencies for your OS**: Download Tkinter's stain for your Linux distribution.

```bash
git clone https://github.com/grisha765/trans_tkpy.git
cd trans_tkpy
python3 -m venv .venv
.venv/bin/pip3 install -r requirements.txt
sudo apt-get install python3-tk wl-clipboard #debian
sudo dnf install python3-tkinter wl-clipboard #fedora
sudo pacman -S tk wl-clipboard #arch
```

### Install binary
- **Download binary**: https://github.com/grisha765/trans_tkpy/releases
    ```bash
    wget -O ~/.local/bin/trans_tkpy \
    $(curl -s https://api.github.com/repos/grisha765/trans_tkpy/releases/latest \
    | grep "browser_download_url.*main" \
    | cut -d '"' -f 4) \
    && chmod +x ~/.local/bin/trans_tkpy
    ```

### Usage

1. Select the `text` that needs to be translated.
2. Run the script with the desired target language specified as a `env` export.
3. The translated text will be displayed in a window that follows your `coords`.
4. You can copy the translated text to the `clipboard` or close the window as needed.

- Other working env's:
    ```env
    LOG_LEVEL="INFO"
    TRANS_COORDS="X Y"
    IN_TRANS_LANG="auto"
    OUT_TRANS_LANG="ru"
    LINGVA_URL="https://lingva.ml/"
    REQUEST_TIMEOUT="20"
    ```

- Use script:
    - Simple set window pos:
        ```bash
        TRANS_COORDS="100 100" \
        OUT_TRANS_LANG="ru" \
        trans_tkpy
        ```

    - Use `hyprland` func for get cursor position:
        ```bash
        TRANS_COORDS=$(hyprctl cursorpos |  sed 's/,//g') \
        OUT_TRANS_LANG="ru" \
        trans_tkpy
        ```

### Features

1. Retrieves text from the primary `clipboard` for translation.
2. Translates text to the desired language using the `Lingva Translate API`.
3. Dynamically positions the translation window based on `coords` location.
4. Allows copying of translated text to the `clipboard`.
