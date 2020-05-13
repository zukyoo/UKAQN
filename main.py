from pypresence import Presence
import pygetwindow as gw
import win32com.client
import requests
import time
import os

osu_close = False
gameOpend = False

state = any
active = any

version = "1.0.3"

r = requests.get('https://api.github.com/repos/zukyoo/UKAQN/releases/latest')
latest = r.json()["tag_name"]

path = 'C:\Windows\System32\drivers\etc'
os.chdir(path)
file = 'hosts'

client_id = "709493460494975068"
RPC = Presence(client_id)
RPC.connect()

def read_hosts():
    with open(file, 'r') as fs:
        data = fs.readlines()
    return data

def getActive():
    global state
    global active
    tittle = gw.getActiveWindowTitle()
    keyword = "osu!"
    keyword_full = "osu!  - "
    if keyword in str(tittle):
        if keyword_full in str(tittle):
            if ".osu" in str(tittle):
                state = tittle.replace("osu!  - ", "").replace(".osu", "")
                active = "Editing beatmap"
            else:
                state = tittle.replace("osu!  - ", "")
                active = "Playing"
        else:
            state = "Idle"
        if state == "osu!":
            state = "Idle"
        elif "watching" in state:
            specname = tittle.replace("osu!  -  (watching ", "").replace(")", "")
            state = f"Spectating {specname}"
            active = "Spectating"
    else:
        state = "AFK"
    return state, active

def check_server():
    datas = read_hosts()
    if "ppy.sh" in str(datas):
        if "163.172.255.98" in str(datas):
            server = "gatari"
            serverl = "Gatari"
        elif "64.225.106.19" in str(datas):
            server = "akatsuki"
            serverl = "Akatsuki"
        elif "88.198.32.213" in str(datas):
            server = "kawata"
            serverl = "Kawata"
        elif "51.15.26.118" in str(datas):
            server = "ripple"
            serverl = "Ripple"
        elif "3.136.108.8" in str(datas):
            server = "the_realm"
            serverl = "The Realm"
        elif "35.178.22.234" in str(datas):
            server = "ryumi"
            serverl = "Ryumi"
        elif "95.179.225.194" in str(datas):
            server = "realistik"
            serverl = "Realistik"
        elif "194.34.133.95" in str(datas):
            server = "ainu"
            serverl = "Ainu"
        elif "148.251.234.42" in str(datas):
            server = "enjuu"
            serverl = "Enjuu"
        else:
            server = "unknown"
            serverl = "an unknown server"
    else:
        server = "bancho"
        serverl = "Bancho"
    return server
    return serverl

def setActive():
    state, active = getActive()
    server = check_server()
    serverl = check_server()
    if state == "AFK" or state == "Idle":
        RPC.update(details = state, large_image= "aqn", large_text="UK!AQN Client", small_image = server, small_text = f"Playing on {serverl}")
    else:
        RPC.update(details = state, state = active, large_image="aqn", large_text="UK!AQN Client", small_image = server, small_text = f"Playing on {serverl}")

def check_exsit(process_name):
    global osu_close
    global gameOpend
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    if len(processCodeCov) > 0:
        osu_run = True
        setActive()
        if osu_run == True and osu_close == True and gameOpend != True:
            print("osu! is running, UK!AQN started.")
            osu_close = False
            gameOpend = True
    else:
        osu_run = False
        RPC.clear()
        if osu_run != True and osu_close != True and gameOpend == True:
            print("osu! has been closed. If you want UK!AQN to continue working, please start it up again!")
            osu_close = True
            gameOpend = False
        elif osu_run != True and osu_close != True and gameOpend != True:
            print("osu! is not running. Please start osu!")
            osu_close = True
            gameOpend = False

    return osu_run

print(F"Version: {version}\nhttps://github.com/zukyoo/UKAQN")
if latest != version:
    print("There is a new update. Please go to the GitHub repo and download the newest version!")
else:
    print("")
	
while True:
    check_exsit("osu!.exe")
    time.sleep(3)
