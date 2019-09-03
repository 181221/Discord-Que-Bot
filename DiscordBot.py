import discord
import subprocess
import sys
import os
import time
from PIL import Image, ImageGrab
from dotenv import load_dotenv, find_dotenv
from AzureOcr import OCR

load_dotenv(find_dotenv())

FILE_NAME = "screen.jpg"
TOKEN = os.getenv("TOKEN")
PATH_TO_SCRIPT = ".\init.ps1"
POWER_COMMAND = ["powershell.exe",
                 "-ExecutionPolicy", "ByPass", PATH_TO_SCRIPT]
client = discord.Client()

azure = False  # set this to false if you do not want Azure Cognitive Service to get text from image.You will need to create an istance of OCR
hasOpenWow = False


def start():
    p = subprocess.Popen(POWER_COMMAND, stdout=sys.stdout)
    p.communicate()


@client.event
async def on_ready():
    print("The bot is ready!")


@client.event
async def on_message(message):
    channel = message.channel
    global hasOpenWow
    if message.author == client.user:
        return

    if message.content.lower() == "position":
        if hasOpenWow:
            channel.send("Getting position in que")
            time.sleep(5)
            ImageGrab.grab().save(FILE_NAME, "JPEG")
            ocr = OCR()
            ocr.recognize_text(FILE_NAME)
            await channel.send(ocr.estimated_que_time + "\n" + ocr.position_in_que)
            ocr.recognize_text(FILE_NAME)
        else:
            await channel.send("wow is not running, run the que command to start")

    if message.content.lower() == "que":
        await channel.send('Relax, I will que up for you :D')
        start()
        time.sleep(5)
        ImageGrab.grab().save(FILE_NAME, "JPEG")
        await channel.send(file=discord.File(FILE_NAME))
        if azure:
            hasOpenWow = True
            ocr = OCR()
            ocr.recognize_text(FILE_NAME)
            if(ocr.estimated_que_time and ocr.position_in_que):
                await channel.send(ocr.estimated_que_time + "\n" + ocr.position_in_que)
            else:
                await channel.send("failed to get estimated time")

        os.remove(FILE_NAME)


client.run(TOKEN)
