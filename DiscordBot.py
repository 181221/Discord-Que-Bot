import discord
import subprocess, sys
import os
import time
from PIL import Image, ImageGrab
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

FILE_NAME="screen.jpg"
TOKEN = os.getenv("TOKEN")
PATH_TO_SCRIPT = ".\init.ps1"
POWER_COMMAND = ["powershell.exe", "-ExecutionPolicy", "ByPass", PATH_TO_SCRIPT]

client = discord.Client()


def start():
    p = subprocess.Popen(POWER_COMMAND, stdout=sys.stdout)
    p.communicate()


@client.event
async def on_ready():
    print("The bot is ready!")

@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return

    if message.content.lower() == "que":
        await channel.send('Relax, I will que up for you :D')
        start()
        time.sleep(15)
        ImageGrab.grab().save(FILE_NAME, "JPEG")
        await channel.send(file=discord. File(FILE_NAME))
        os.remove(FILE_NAME)


client.run(TOKEN)
