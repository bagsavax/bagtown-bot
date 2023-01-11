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

# Here we name the cog and create a new class for the cog.
class Holy(commands.Cog, name="holy"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="howholy",
        description="How holy are you, devotee?",
    )
    async def how_holy(self, context: Context):
        """
        This command will tell you how holy you are.
        """
     
       
        # Generate random number between 1-100
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
    


    @commands.hybrid_command(
        name="prophecy",
        description="This command will tell you a prophecy.",
    )
    async def lore(self, context: Context):
        """
        Use OpenAi to generate responses composed of Sewer Prophesy lore.
        """
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Topic: End Times\nFive-Sentence Ominous Prophecy: There are dark forces in the network, Bagman is calling for your toil in the greater work. Become one with the network, Bagman is in you. You are in Bagman. \n    \nTopic: Piety\nFive-Sentence Ominous Prophecy:",
            temperature=0.8,
            max_tokens=101,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0
            )
        # Do your stuff here
        
        await context.send(response.choices[0].text)
        # Don't forget to remove "pass", I added this just because there's no content in the method.
  

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    print(Holy)
    await bot.add_cog(Holy(bot))