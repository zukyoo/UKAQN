from pypresence import Presence
import pygetwindow as gw
import win32com.client
from tkinter import font
from tkinter import *
import time
import sys
import os

path = 'C:\Windows\System32\drivers\etc'
os.chdir(path)
file = 'hosts'

client_id = "707510270771068945"
RPC = Presence(client_id)
RPC.connect()

def read_hosts():
    with open(file, 'r') as fs:
        data = fs.readlines()
    return data

def getActive():
    tittle = gw.getActiveWindowTitle()
    keyword = "osu!"
    keyword_full = "osu!  - "
    if keyword in str(tittle):
        if keyword_full in str(tittle):
            state = tittle.replace("osu!  - ", "")
        else:
            state = "Idle"
        if state == "osu!":
            state = "Idle"
        elif "watching" in state:
            specname = tittle.replace("osu!  -  (watching ", "").replace(")", "")
            state = f"Spectating {specname}"
    else:
        state = "AFK"
    return state

def check_server():
    datas = read_hosts()
    if "ppy.sh" in str(datas):
        if "163.172.255.98" in str(datas):
            server = "gatari"
        elif "159.65.235.81" in str(datas):
            server = "akatsuki"
        elif "88.198.32.213" in str(datas):
            server = "kawata"
        elif "51.15.26.118" in str(datas):
            server = "ripple"
        elif "47.89.44.19" in str(datas):
            server = "ppy.sb"
        else:
            server = "unknown"
    else:
        server = "bancho"
    return server

def setActive():
    state = getActive()
    server = check_server()
    if state == "AFK" or state == "Idle":
        RPC.update(details = state, large_image= "aqn", large_text="TheAquila Client", small_image = server, small_text = f"Playing on {server} server")
    else:
        RPC.update(details = state, state = "Getting good", large_image="aqn", large_text="TheAquila Cilent", small_image = server, small_text = f"Playing on {server} server")

def check_exsit(process_name):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    if len(processCodeCov) > 0:
        setActive()
    else:
        RPC.clear()

print("Version: 1.0.0-prerelease\n")

while True:
    check_exsit("osu!.exe")
    time.sleep(3)