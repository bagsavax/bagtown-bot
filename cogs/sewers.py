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
import os
import openai
from dotenv import load_dotenv
from PIL import Image, ImageOps
import numpy as np

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")    
# dotenv_path = join(dirname(__file__), '.env')



# Here we name the cog and create a new class for the cog.
class Sewers(commands.Cog, name="sewers"):
    
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="schemers", 
        description="This is a testing command that does nothing.",
    )
    async def sewerschemers(self, context: Context):
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
        name="lore",
        description="This is a testing command that does nothing.",
    )
    async def lore(self, context: Context):
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """
        # There are three basic guidelines to creating prompts:

        # Show and tell. Make it clear what you want either through instructions, examples, or a combination of the two. If you want the model to rank a list of items in alphabetical order or to classify a paragraph by sentiment, show it that's what you want.

        # Provide quality data. If you're trying to build a classifier or get the model to follow a pattern, make sure that there are enough examples. Be sure to proofread your examples — the model is usually smart enough to see through basic spelling mistakes and give you a response, but it also might assume this is intentional and it can affect the response.

        # Check your settings. The temperature and top_p settings control how deterministic the model is in generating a response. If you're asking it for a response where there's only one right answer, then you'd want to set these lower. If you're looking for more diverse responses, then you might want to set them higher. The number one mistake people use with these settings is assuming that they're "cleverness" or "creativity" controls.
        # openai.api_key = os.getenv('OPENAI_API_KEY')
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Topic: Sewers\nTwo-Sentence Cryptic Story: No one knows who lurks in the Sewers. Some say they're a group of geniuses intent on saving Bagtown. Others say they want to destroy Bagtown. \n    \nTopic: Bagtown\nTwo-Sentence Cryptic Story:",
            temperature=0.9,
            max_tokens=50,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0
            )
        # Do your stuff here
        c = response.choices[0].text
        await context.send(c)
        # Don't forget to remove "pass", I added this just because there's no content in the method.
    @commands.hybrid_command(
    name="bagperson",
    description="Will make a bag out of you",
)
    async def bagperson(self, context: Context):
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """
        img_file = "piglets-now.png"
        rgb_image = Image.open(img_file)
        rgba_image = rgb_image.convert('RGBA')
        rgba_image.save(img_file)
        img = Image.open("piglets-now.png")
        border = 256
        alpha = Image.new('L', (1024-2*border,1024-2*border), "white")
        alpha = ImageOps.expand(alpha, border)
        dem_fps = ["piglets-now.png", "piglets-now.png", "piglets-now.png"]

# Open each image in turn and push in our ready-made alpha channel
        for item in dem_fps:
            im = Image.open(item).convert('RGB')
            im.putalpha(alpha)
            im.save(f'RESULT-{item}')
        alpha.save("testpics/pillowtest.png")
        response = openai.Image.create_edit(
            image=open("RESULT-piglets-now.png", "rb"),
            # mask=open('piglets-now2.png', "rb"),
            prompt="inside an extensive sewer system that has wires and other conspicuous devices",
            n=1,
            size='512x512', 
            )
    
        image_url = response['data'][0]['url']
        await context.send(image_url)

    @commands.Cog.listener('on_message')
    async def piggies(self, message):
        """Piggies
        
        """
        if message.author == self.bot.user or message.author.bot:
            return
        if message.content.find('pig') != -1:
            await message.channel.send('piggies')


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(Sewers(bot))
