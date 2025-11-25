import asyncio
import discord
from discord.ext import commands


""" This cog contains the 'help' extension """
class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command to list all the commands
    @commands.command(name='commands', pass_context=True)
    async def commands(self, ctx, category: str = ""):

        # Define the command groups.
        command_groups = {
            "Game": "Commands for playing RailGuessr.",
            "Fun": "Random functions of the bot.",
            "Help": "Get assistance with bot operation.",
            "Admin": "Restricted to bot administrators.",
        }

        # If argument not supplied, list arguments.
        if category.upper() not in [i.upper() for i in list(command_groups.keys())]:
            embed = discord.Embed(
                title='Help: Commands List',
                description='Commands are grouped into the following categories:',
                colour=discord.Colour.purple()
            )

            # Populate the embed with command groups and their descriptions.
            txt = ""
            for key, value in command_groups.items():
                txt += f"• **{key}**: {value}\n"
            embed.add_field(name='', value=txt, inline=False)
            embed.add_field(name='Use `.commands <category>` for a list of all commands.', value="", inline=False)
            await ctx.channel.send(embed=embed)


# Setup the cog
async def setup(bot):
    await bot.add_cog(HelpCog(bot))