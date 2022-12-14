import os

import discord
import re

token = os.environ.get("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

exp = re.compile(".*[aeiouy]r[.?!,]?", re.IGNORECASE)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    words = message.content.split()
    for word in words:
        if exp.match(word):
            await message.channel.send(f'{word}? I hardly even know her')
            return

client.run(token)
