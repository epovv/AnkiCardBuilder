Python 3.8.1


# Anki Card Builder
This is a little script to create note for your anki deck, like word:translate

<p align="center">
	<img src="https://github.com/epovv/AnkiCardBuilder/blob/master/content/example.png" width="800">
</p>

At this moment supports only Yandex Dictionary(Its free)
 - https://tech.yandex.com/dictionary/
 
## Start info

First you need:
 - [AnkiConnect add-on](https://ankiweb.net/shared/info/2055492159) (code 2055492159)
 - [Yandex API key for dictionary](https://tech.yandex.com/keys/get/?service=dict)

## Install

There are two ways:
- You can use the executable

1. For Windows 10 64-bit [Download executable](https://github.com/epovv/AnkiCardBuilder/releases/latest)
2. Put config.txt in folder with executable

- Sorce code

1. Install Python 3.8.1
2. Download source code
3. In console go to folder with code
4. Create venv (python -m venv venv)
5. Enter venv (venv\Scripts\activate)
6. pip install -r requirement.txt

And u can compile your own program with pyinstaller

1. pip install pyinstaller
2. in your created venv run command pyinstaller --onefile main.py
3. Dont forget put config.txt in folder with executable

## Usage

1. You need fill config.txt
- api_key=Your API key
- lang_from=en - Language code from which the translation is needed
- lang_to=ru - Language code for translation
- anki_model_name=default - Anki card template(For now use the standard)
- anki_deck_name=default - Your Anki deck
- anki_host=http://localhost:8765 - AnkiConnect add-on host(default is http://localhost:8765)

For executable
- just run and write word

For source
- in your created venv run script (python main.py)
- just run and write word