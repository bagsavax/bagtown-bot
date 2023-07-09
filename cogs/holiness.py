""""
Copyright © Krypton 2019-2022 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.4.2
"""
import random
import discord
from discord.ext import commands
from discord.ext.commands import Context

import openai
from helpers import checks


# Holy cog
class Holy(commands.Cog, name="holy"):
    def __init__(self, bot):
        self.bot = bot

    # COMMAND: howholy
    @commands.hybrid_command(
        name="howholy",
        description="How holy are you, devotee?",
    )
    async def how_holy(self, context: Context):
        """
        This command will tell you how holy you are.
        """

        holy_score = random.randint(1, 100)
        holy_message = ""
        if holy_score  <= 25:
            holy_message =  '**HOLINESS RATING: **' + str(holy_score) + " - Leave my temple, sinner!"
        elif holy_score <= 50:
            holy_message = '**HOLINESS RATING: **' + str(holy_score) + " - Everyone must start somewhere, devotee. Your path is long, but you are on it."
        elif holy_score <= 75:
            holy_message = '**HOLINESS RATING: **' + str(holy_score) + " - You are Holy, but not based, devotee."
        elif holy_score <= 100:
            holy_message = '**HOLINESS RATING: **' + str(holy_score) + " - You are a true devotee of the Holy One, teach the others your simple and based ways."

        # If Justn is the author, he is a heretic and will be punished for his sins.
        if context.author.id == 5290:
            holy_message = '**HOLINESS RATING: 0** - You are a heretic, and will be punished for your horny sins.' 

        await context.send(holy_message)

    # COMMAND: cult
    @commands.hybrid_command(
        name="cult",
        description="Is this a cult?",
    )
    async def is_cult(self, context: Context):
        """
        Are Bagtown or The Sewers a cult?
        """

        cult_message = ':warning: *THIS IS ABSOLUTELY NOT A CULT* :warning: \n|| 01110100 01101000 01101001 01110011 00100000 01101001 01110011 \n00100000 01100001 00100000 01100011 01110101 01101100 01110100 ||' 

        await context.send(cult_message)
    
    # COMMAND: sacrifice
    @commands.hybrid_command(
        name="sacrifice",
        description="Make the Ultimate Sacrifice.",
    )
    async def holy_sacrifice(self, context: Context):
        """
        Make the Ultimate Sacrifice.
        """

        sacrifice_message = '*You hear something creeping towards you in the shadows. \nYou know what comes next, you made Ultimate Sacrifice. \nThe devotee needs piglets - and he needs them NOW.*'
        with open("/images/piglets-now.png", 'rb') as f:
            piglets_now =discord.File(f)

        await context.send(sacrifice_message, file=piglets_now)
    
    # COMMAND: prophecy
    @commands.hybrid_command(
        name="prophecy",
        description="This command will tell you a prophecy.",
    )
    async def lore(self, context: Context):
        """
        Use OpenAi to generate responses composed of Sewer Prophesy lore.
        """
        response = await openai.Completion.acreate(
            model="text-davinci-003",
            prompt="Topic: End Times\nFour-Sentence Ominous Prophecy: There are dark forces in the network, Bagman is calling for your toil in the greater work. Become one with the network, Bagman is in you. You are in Bagman. \n    \nTopic: Piety\nFour-Sentence Ominous Prophecy:",
            temperature=0.8,
            max_tokens=101,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0
            )
        print(response.choices)

        
        await context.send(response.choices[0].text)
    @commands.has_role("bagtown board")
    @commands.hybrid_command(
        name="thesewers", 
        description="what are they scheming?",
    )
    async def sewerlorevid(self, context: Context):
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """
     
       
        # Do your stuff here
        with open("The Sewers.mp4", 'rb') as f:
            toe =discord.File(f)
        
        await context.send(file=toe)

async def setup(bot):
    await bot.add_cog(Holy(bot))