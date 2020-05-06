# AquilaRP

> A python script that provides a Discord Rich Presence description for osu! but it's AQN.

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence) [![license](https://img.shields.io/github/license/qwertyquerty/pypresence.svg?style=for-the-badge)](https://github.com/qwertyquerty/pypresence/blob/master/LICENSE)

# Hows it Work

Get the current game activity through the process title of `osu!.exe`.

![](https://i.imgur.com/UiOtyuB.png)

It gets the process title every three seconds, but the occupancy rate in the background is low enough to be ignored.

# Stuff is good, but why

![](https://i.imgur.com/MVRbjl8.png)

Some people want to show their Rich-Presence but dont want to get a report for it. But at the same time, they really want to show the fact that **I am AQN user**. AquilaRP is for them.

## What will it display

AquilaRP will not display any ign, only show the server you are currently on. And the beatmap you are currently playing, and which player is spectating by you.

# How to use

- Download compiled file in [Release](https://github.com/Kotoki1337/AquilaRP/releases).
- Put it where you cant forget (I dont care you putting **AquliaRP** next to **AQN** LOL).
- Open it and forget it.

## Building from Source

Don't want to use my client id? Build AquilaRP from source fairly easily.

Prerequisites:
- [Python 3.8.2](https://www.python.org/)
- [pypresence](https://github.com/qwertyquerty/pypresence)
- [pygetwindow](https://github.com/asweigart/PyGetWindow)
- [pyinstaller](https://pypi.org/project/PyInstaller/) (You can get this using `pip install pyinstaller`)

**Windows**

1. Any `clone` method you want to use
2. Make you own big brain code here.
3. Open `cmd` and run `pyinstaller -F main.py` in cmd folder.

**Linux**

I don't use Linux. If you are all using Linux, building python should not be difficult for you

# WIP
- [ ] Support AQN replay editor.
- [ ] Identify in-game beatmap edit.
- [ ] Custom text.
- [ ] Python GUI(?)
