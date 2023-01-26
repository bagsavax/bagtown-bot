from discord.ext import commands
from discord.ext.commands import Context
from helpers import checks





class Responses(commands.Cog, name="responses"):
    
    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener('on_message')
    async def bagette(self, message):
        """Piggies
        
        """
        b= "bagette"
        if message.author == self.bot.user or message.author.bot:
            return
        if message.content.lower().find('bagette') != -1:
            await message.channel.send('can i help you')

    @commands.Cog.listener('on_message')
    async def iwillpat(self, message):    
        if message.author == 745044163170402365:
            await message.channel.send("ooooo ooo wienie boy weinie boy")
    
    @commands.Cog.listener('on_message')
    async def geeee(self, message):
        """Piggies
        
        """
        if message.author == self.bot.user or message.author.bot:
            return
        if message.content.lower().find('cum') != -1:
            await message.channel.send('geeee')


async def setup(bot):
    await bot.add_cog(Responses(bot))