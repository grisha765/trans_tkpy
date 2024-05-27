# trans_tkpy
This Python script enables quick translation of text from the primary clipboard to a specified language. It utilizes the Google Translate API for translation and tkinter for the graphical user interface. The script automatically detects the language of the text in the clipboard and translates it to the specified target language.
### Initial Setup

1. **Clone the repository**: Clone this repository using `git clone`.
2. **Create Virtual Env**: Create a Python Virtual Env `venv` to download the required dependencies and libraries.
3. **Download Dependencies**: Download the required dependencies into the Virtual Env `venv` using `pip`.
4. **Download dependencies for your OS**: Download Tkinter's stain for your Linux distribution.

```shell
git clone https://github.com/grisha765/trans_tkpy.git
cd trans_tkpy
python3 -m venv venv
venv/bin/pip3 install -r requirements.txt
sudo apt-get install python3-tk wl-clipboard #debian
sudo dnf install python3-tkinter wl-clipboard #fedora
sudo pacman -S tk wl-clipboard #arch
```

#### Bonus
1. **Download binary**: https://github.com/grisha765/trans_tkpy/releases

### Usage
1. Select the text that needs to be translated.
2. Run the script with the desired target language specified as a command-line argument.
3. The translated text will be displayed in a window that follows your mouse cursor.
4. You can copy the translated text to the clipboard or close the window as needed.

```shell
venv/bin/python3 main.py ru
```
read [ISO_639-1](https://en.wikipedia.org/wiki/ISO_639-1)

### Features

1. Retrieves text from the primary clipboard for translation.
2. Translates text to the desired language using the Google Translate API.
3. Dynamically positions the translation window based on mouse cursor location.
4. Allows copying of translated text to the clipboard.
5. Provides a user-friendly graphical interface for ease of use.
