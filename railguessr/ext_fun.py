import asyncio
import discord
from discord.ext import commands

""" This cog contains the 'fun' extension """
class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', pass_context=True)
    async def ping(self, ctx):
        await ctx.send('pong!')

# Setup the cog
async def setup(bot):
    await bot.add_cog(FunCog(bot))