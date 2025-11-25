import asyncio
import discord
from discord.ext import commands


""" Class containing command information """
class Command:
    def __init__(self, name, description, syntax):
        self.name = name
        self.description = description
        self.syntax = syntax


""" Class for groups of commands """
class CommandGroup:
    def __init__(self, name: str, description: str, *commands):
        self.name = name
        self.description = description
        self.commands = commands


# Populate the command groups
command_group_help = CommandGroup(
    "Help",
    "Commands to help you use the bot.",
    Command('commands', 'List available commands in given category.', '`.commands [category]`')
)
command_group_fun = CommandGroup(
    "Fun",
    "A variety of silly commands.",
    Command('ping', 'Pong!', '`.ping`'),
    Command('fax', 'Send a user a random fax message.', '`.fax <user>`')
)


""" This cog contains the 'help' extension """
class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command to list all the commands
    @commands.command(name='commands', pass_context=True)
    async def commands(self, ctx, category: str = ""):

        # Define the command groups.
        command_groups = [command_group_help, command_group_fun]

        # If argument not supplied, list arguments.
        if category == "":
            embed = discord.Embed(
                title='Help: Commands List',
                description='Commands are grouped into the following categories:',
                colour=discord.Colour.purple()
            )

            # Populate the embed with command groups and their descriptions.
            txt = ""
            for command_group in command_groups:
                txt += f"• **{command_group.name}**: {command_group.description} ({len(command_group.commands)} commands)\n"
            embed.add_field(name='', value=txt, inline=False)
            embed.add_field(name='', value="Use `.commands <category>`.", inline=False)
            await ctx.channel.send(embed=embed)

        # A valid category has been given
        elif category.upper() in [i.name.upper() for i in command_groups]:

            # Retrieve the command group
            command_group_index = [i.name.upper() for i in command_groups].index(category.upper())
            command_group = command_groups[command_group_index]

            embed = discord.Embed(
                title='Help: Commands List',
                description=f'The following commands are available in category `{command_group.name}`:',
                colour=discord.Colour.purple()
            )

            # Populate the embed with command groups and their descriptions.
            txt = ""
            for command in command_group.commands:
                txt += f"`{command.syntax}`: {command.description}\n"
            embed.add_field(name='', value=txt, inline=False)
            await ctx.channel.send(embed=embed)


        # Throw an error message indicating the user to provide a command category
        else:
            embed = discord.Embed(
                title='Error: Invalid Argument',
                description='You have provided an invalid command category. See list below:',
                colour=discord.Colour.red()
            )

            # Populate the embed with command groups and their descriptions.
            txt = ""
            for command_group in command_groups:
                print(command_group)
                txt += f"• **{command_group.name}**: {command_group.description} ({len(command_group.commands)} commands)\n"
            embed.add_field(name='', value=txt, inline=False)
            embed.add_field(name='', value="Use `.commands <category>`.", inline=False)
            await ctx.channel.send(embed=embed)


# Setup the cog
async def setup(bot):
    await bot.add_cog(HelpCog(bot))