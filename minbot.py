

import discord




token = "MTA2MTg3MzA0ODIwODI4NTcyMQ.G8Kgq7.lpOhg3Y_OwAn0FD0iiM6n4TyfRi6MOXLl4vxN4"
# This example requires the 'message_content' intent.


intents = discord.Intents.default()
intents.typing = True
intents.presences = False
intents.message_content = True

client = discord.Client(intents=intents)
print(client)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    content = message.content.lower()
    print(content)

    if message.author == client.user:
        return

    if content.startswith('hello'):
        await message.channel.send('We are the bagettes')
    if content.startswith('who came up with the name?'):
        await message.channel.send('Artie')
    if content.startswith('cum'):
        await message.channel.send('geeee')
    if content.startswith('bags'):
        await message.channel.send('Yes, Master?')
    if content.startswith('who are you?'):
        await message.channel.send('I am Bagette, the #1 bot in Bagtown')

    if content.startswith('where do the sewers go?'):
        await message.channel.send('They say they lead to another town. A utopia of sorts. Where bags are flying freely in the skies')
        # 

client.run(token)



