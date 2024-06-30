# Tutorial to Create a Discord Bot Using the Disnake Library 💙 #1
To make it easier for you, I have broken everything down into stages.

<div align="center">
  <img src="https://media.giphy.com/media/oFo77ZD0hiusDNy55s/giphy.gif?cid=ecf05e47jzhx3ppnm3uly4jff254hq4nttqvz6hdtzqq59ms&ep=v1_gifs_search&rid=giphy.gif&ct=g"/>
    </div>

## 1. Beginning 🫡
### Python installation
1. Click [here](https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe) and you download python 3.12.4
2. Be sure to check the box next to Add Python 3.12.4 in PATH and proceed with further installation

Also: After installing **Python**, you can also install **Visual Studio Code** to edit bot files using this [link](https://code.visualstudio.com/Download)

## 2. Creating a bot 🤖
#### Create a new bot on the website [Discord Developers Portal](https://discord.com/developers/applications)
1. Go to [site](https://discord.com/developers/applications)
2. Click on the button  `New Application`

![image](https://github.com/fardieov/Tutorial-Discord-Bot/assets/169608913/cb37dc51-192b-452e-94aa-6bd53271c64e)

3. Name the robot and click  `Create`

![image](https://github.com/fardieov/Tutorial-Discord-Bot/assets/169608913/79d26d98-1d08-4479-8c0e-063cb31830fe)

4. Select a tab  `Bot`

![image](https://github.com/fardieov/Tutorial-Discord-Bot/assets/169608913/4af54839-7ace-4b12-a1aa-70d53c2b0cd3)

5. Click `Reset Token`  and save it somewhere (After reloading the page, the token will disappear and will have to be recreated if lost)

![image](https://github.com/fardieov/Tutorial-Discord-Bot/assets/169608913/dedc7f59-9783-4252-a0b4-d5fda6893184)

#### Intents
In the `Bot`  tab, enable the following checkboxes

1. `Public Bot`  - Means the bot is public and can be added by other people to their Discord servers.
2. `Presence Intent`  - Allows the bot to track users' presence, including their real-time status (e.g. online, away, busy) and activity (e.g. playing a game).
3. `Server Members Intent`  - Allows the bot to obtain information about server members, such as names, nicknames, roles, etc.
4. `Message Content Intent`  - Allows the bot to receive information about the content of messages, including text and attachments.

#### Installing dependency
We write this command in cmd  `pip install disnake`

#### Root file  `bot.py`
Customizing the bot for yourself
###### Statuses
```py
Online
status=disnake.Status.online

Offline
status=disnake.Status.offline

Do not disturb
status=disnake.Status.dnd

Not active
status=disnake.Status.idle
```

###### Activities
```py
 Playing
 activity=disnake.Game(name="game")
 
 Looks
 activity=disnake.Activity(type=disnake.ActivityType.watching, name="youtube")
 
 Listens
 activity=disnake.Activity(type=disnake.ActivityType.listening, name="music")
 
 Streaming
 activity=disnake.Streaming(name="game", url="https://www.twitch.tv/nickname") #if you remove the url argument, the button simply won’t appear, but everything will work
 
 Competes in
 activity=disnake.Activity(type=disnake.ActivityType.competing, name="creating a bot")
 ```

###### Test Guilds
This parameter means adding a test server on which slash commands will be updated immediately. If you add a large number of identifiers, the bot will start slowly, we recommend adding no more than 3

To add your server there, write this:
```py
test_guilds=[id]
 ```

To add several servers write like this
 ```py
 test_guilds=[id, id]
 ```
**Important** - If your server ID is not there, the slash command will appear/update only 10-15 minutes after it is added/changed

### Terms
Cog - bot module where commands are stored, you can create as many cogs as you like (Cleaning, Entertainment, etc.)

Token - an encrypted Discord key with which the bot is authorized

Import is a mandatory thing that adds a lot of useful things to the code, example below
 ```py
 import disnake
 from disnake.ext import commands
 ```
Event - a trigger that is activated by some action, for example on_ready - the bot is turned on (ready)

further look at the files, there I will post examples!

upd 2024 29.06
