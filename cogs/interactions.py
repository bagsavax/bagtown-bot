import discord
from discord.ext import commands
from discord.ext.commands import Context


from helpers import checks


class Interactions(commands.Cog, name="interactions"):
    """A group of commands 

    Args:
        commands (_type_): _description_
        name (str, optional): _description_. Defaults to "interactions".
    """
    
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
    name="speak",
    description="Will make a bag out of you")
    async def ask_bagette(self, context: Context, args):
        print(context.message)
        if str(context.message.content).startswith(str(self.bot.user.id)):
            await context.message.send("Hi!")
        if context.author == self.bot.user or context.author.bot:
            return
        if str(context.message.content).startswith('<@1061873048208285721>'):
            m = str(context.message.content).strip("<@1061873048208285721>")
            await context.send('f off m8')


    @commands.hybrid_command(
    name="astro",
    description="whats my sign?")
    async def astro(self, context: Context):
        with open("baggatarius.jpeg", 'rb') as f:
            toe =discord.File(f)
        
        await context.send(file=toe)


    @commands.Cog.listener('on_message')
    async def ask_bagette(self, message,):
        print(message.content)
        if message.author == self.bot.user or message.author.bot:
            return
        if message.content.startswith('<@1061873048208285721>'):
            m = message.content.strip("<@1061873048208285721>")
            await message.channel.send('booba')

async def setup(bot):
    await bot.add_cog(Interactions(bot))