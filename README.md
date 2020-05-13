# UK!AQN

> A python script that provides a Discord Rich Presence for osu!, except its UK!AQN :sunglasses:

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence) [![license](https://img.shields.io/github/license/qwertyquerty/pypresence.svg?style=for-the-badge)](https://github.com/qwertyquerty/pypresence/blob/master/LICENSE)

## What does it do/show?

UK!AQN will not display any ign, it will only show the server you are currently on and the beatmap you are currently playing/editing.

# How to use

- Download the latest version from [Releases](https://github.com/zukyoo/UKAQN/releases).
- Put the exe anywhere accessable.
- Run it and you're done!

## Building from Source

Want to make your own edits/use your own Client ID? Simple:

Prerequisites:
- [Python 3.8.2](https://www.python.org/)
- [pypresence](https://github.com/qwertyquerty/pypresence)
- [pygetwindow](https://github.com/asweigart/PyGetWindow)
- [pyinstaller](https://pypi.org/project/PyInstaller/) (You can get this using `pip install pyinstaller`)

**Windows**

1. Clone/download this github repo.
2. Make any changes to main.py
3. Open `cmd` and run `pyinstaller -F main.py` in the folder you are editing in.
