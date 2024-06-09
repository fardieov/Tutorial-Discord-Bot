import disnake
from disnake.ext import commands
import os
intents = disnake.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, test_guilds=[id])

@bot.event
async def on_ready():
  print("Bot is ready!")


for file in os.listdir("./cogs"):
  if file.endswith(".py"):
    bot.load_extension(f"cogs.{file[:-3]}")

bot.run('TOKEN') #Your token
