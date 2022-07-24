from discord_webhook import *
from datetime import datetime

webhook_url = {insert webhook url here}

def log(event):
    now = datetime.now()
    dt_string = now.strftime("time: " + "%d.%m.%Y, %H:%M:%S")
    time = dt_string 
    webhook = DiscordWebhook(url=webhook_url, username="LOGGING BOT", content=event, avatar_url="https://cdn-icons-png.flaticon.com/512/61/61174.png")
    embed_msg = time # define that the embed msg is the time var
    embed = DiscordEmbed(title="" + embed_msg + "", color=242424) # define embed
    webhook.add_embed(embed) # add embed
    response = webhook.execute() # execute everythings
