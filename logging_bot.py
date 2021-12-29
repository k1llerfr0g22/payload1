from discord_webhook import *
from datetime import datetime

webhook_url = "https://discordapp.com/api/webhooks/923976550410485791/iqDWmTmpXZf37_J7nPpZADqIEc_6Ew9kJo0LI5PDwaf7HC6O1tVZalJjcKs9TCrE5tgt"

def log(event):
    now = datetime.now()
    dt_string = now.strftime("time: " + "%d.%m.%Y, %H:%M:%S")
    time = dt_string 
    webhook = DiscordWebhook(url=webhook_url, username="LOGGING BOT", content=event, avatar_url="https://cdn-icons-png.flaticon.com/512/61/61174.png")
    embed_msg = time # define that the embed msg is the time var
    embed = DiscordEmbed(title="" + embed_msg + "", color=242424) # define embed
    webhook.add_embed(embed) # add embed
    response = webhook.execute() # execute everythings