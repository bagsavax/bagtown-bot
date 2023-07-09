""""
Copyright © Krypton 2019-2022 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.4.2
"""
import os
import discord
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")    

# Here we name the cog and create a new class for the cog.
class Foot(commands.Cog, name="foot"):
    def __init__(self, bot):
        self.bot = bot
        

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
    
    @commands.hybrid_command(
        name="toe",
        description="Long piggie",
    )
    async def longtoe(self, context: Context):
        """
        Senbds the piggie gif

        :param context: The application command context.
        """
     
       
        # Do your stuff here
        with open("/images/longtoe.gif", 'rb') as f:
            toe =discord.File(f)
        
        await context.send(file=toe)
        # Don't forget to remove "pass", I added this just because there's no content in the method.
    
    @commands.hybrid_command(
    name="feet",
    description="This command summons an ai foot",
)
    async def feet(self, context: Context):
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """
        await context.send('pls be patient im a little slow at this')
        response = openai.Image.create(
        prompt="the most normal human foot possible",
        n=1,
        size='512x512', 
        )
        image_url = response['data'][0]['url']
        await context.send(image_url)

    @commands.hybrid_command(
    name="wrath",
    description="daddy")
    async def wrath(self, context: Context):
        """wrath command

        Args:
            message (_type_): _description_
        """
        with open("/images/crying zoomer.jpg",  'rb') as f:
            img =discord.File(f)

        await context.send(file=img)

    @commands.Cog.listener('on_message')
    async def piggies(self, message):
        """Piggies
        
        """
        if message.author == self.bot.user or message.author.bot:
            return
        if message.content.find('pig'.lower()) != -1:
            await message.channel.send('piggies')

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(Foot(bot))
