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

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
IMG_DIR = os.getenv("IMAGES_DIR")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents, case_insensitive=True)

""" Load extensions"""
async def load_cogs():

    # Find all cogs, named ext_*.py under railguessr
    cogs = []
    for file in os.listdir('railguessr'):
        if file.endswith('.py') and file != "__init__.py":
            cogs.append(f'railguessr.{file[:-3]}')

    # Loop over cogs and load them
    for cog in cogs:
        try:
            await bot.load_extension("railguessr.ext_fun")
        except Exception as e:
            print(f'Failed to load {cog} cog: {e}')


""" Confirm the bot is activated """
@bot.event
async def on_ready():
    await load_cogs()
    print(f'Initialised RailGuessr!')


# """ Process commands from messages """
# @bot.event
# async def on_message(message):
#     if (len(message.content) > 0) and (not message.content == len(message.content) * message.content[0]):
#         await bot.process_commands(message)


# Run the bot
bot.run(TOKEN)