import asyncio
import discord
from discord.ext import commands
import json
import random

""" This cog contains the 'fun' extension """
class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Ping / Pong to check the bot is working
    @commands.command(name='ping', pass_context=True)
    async def ping(self, ctx):
        await ctx.send('pong!')


    # Fax the victim a funny image
    @commands.command(name='fax', pass_context=True)
    async def fax(self, ctx, recepient: discord.User):
        await ctx.message.delete()
        id = recepient.id
        txt = f"<@{id}>, you are receiving a fax. Please standby...\n\n"
        message = await ctx.send(txt)

        # Open the file
        with open('Data/fax.json', 'r') as json_file:
            faxes = json.load(json_file)

        max_id = len(faxes)
        id = random.randint(0, max_id)
        fax = faxes[f'{id}']

        for i in range(len(fax)):
            await asyncio.sleep(random.random() / 2)
            new_msg = txt
            for j in range(i+1):
                new_msg += f'{fax[j]}\n'
            await message.edit(content=new_msg)

    @fax.error
    async def fax_error(self, ctx, error):
        print(f'fax_error: {error}')

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='Error: Missing Argument',
                description=f'The correct syntax is: `.fax <user>`',
                colour=discord.Colour.red()
            )
            await ctx.send(embed=embed)

# Setup the cog
async def setup(bot):
    await bot.add_cog(FunCog(bot))