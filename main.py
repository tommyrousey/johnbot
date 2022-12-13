import os

import discord
from pronouncing import rhymes

token = os.environ.get("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    words = message.content.split()
    for word in words:
        if word in rhymes('her'):
            await message.channel.send(f'{word}? I don\'t even know her')
            return

client.run(token)
