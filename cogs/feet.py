""""
Copyright © Krypton 2019-2022 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.4.2
"""
import discord
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks
from PIL import Image
# Here we name the cog and create a new class for the cog.
class Foot(commands.Cog, name="foot"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="toe",
        description="This is a testing command that does nothing.",
    )
    async def longtoe(self, context: Context):
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """
     
       
        # Do your stuff here
        with open("longtoe.gif", 'rb') as f:
            toe =discord.File(f)
        
        await context.send(file=toe)
        # Don't forget to remove "pass", I added this just because there's no content in the method.
    
    @commands.hybrid_command(
    name="feet",
    description="This is a testing command that does nothing.",
)
    async def feet(self, context: Context):
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """
     
       
        # Do your stuff here
        with open("longtoe.gif", 'rb') as f:
            toe =discord.File(f)
        
        await context.send(file=toe)

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(Foot(bot))
