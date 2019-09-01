# Discord-Que-Bot

## Getting Started
Make sure you have python and pip installed

First create a discord bot and add it to your discord server.

After you have create the bot create a file name .env in this directory.

```
TOKEN=YOUR DISCORD TOKEN
ACCOUNT=YOUR ACCOUNT NAME
PASSWORD=YOUR PASSWORD
```

Open powershell in working directory and run the following command
```
pip install -r /path/to/requirements.txt
```
This might take a minute

### get x and y position of mouse
This is an important step because you will the bot need P(x,y) of realm server. Just hoover over your server and run the following command in powershell
```
Add-Type -AssemblyName System.Windows.Forms
$X = [System.Windows.Forms.Cursor]::Position.X
$Y = [System.Windows.Forms.Cursor]::Position.Y
Write-Output "X: $X | Y: $Y"
```

then run this command
```
 python .\DiscordBot.py
```

Go to your channel in discord and type "que or position"


### create a shortcut
If you want a shortcut icon that start the bot, do the following.

 1. Right click anywhere on the Desktop (or in a folder) and select New Shortcut.
 2. Navigate to C:\Windows\System32\WindowsPowerShell\v1.0. and select powershell.exe
 3. Finish
 4. Right click on shortcut and select Properties to open the new window
 5. In textbox called target write C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe python .\DiscordBot.py
 6. In Start in box write: C:\yourpath
 7. Press okay





### fix image scaling in python
if the image receive in discord in not in full screen, then this should work.
 1. Go to where you have installed pythen and rightclick on python.exe and click properties
 2. Click on the compatibility tab click change high DPI settings 
 3. check Override high DPI scaling behavior 

 
