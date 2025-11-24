import ssl
import discord
import asyncio
import json
import random
import datetime
import math
from discord.ext import commands
from discord import File
from dotenv import load_dotenv
import re
import os
import importlib.metadata

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
IMG_DIR = os.getenv("IMAGES_DIR")
# VERSION = importlib.metadata.version("RailGuessr") # Doesn't work while package not installed

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents, case_insensitive=True)


""" Confirm the bot is activated """
@bot.event
async def on_ready():
    print(f'Initialised RailGuessr')


""" Process commands from messages """
@bot.event
async def on_message(message):
    if (len(message.content) > 0) and (not message.content == len(message.content) * message.content[0]):
        await bot.process_commands(message)


# Run the bot
bot.run(TOKEN)