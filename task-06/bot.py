import discord
from discord.ext import commands
import scraper
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!help"):
        await message.channel.send("!live : Get live scores\n!csv : Get live scores in a CSV file")

    elif message.content.startswith("!live"):
        msg = scraper.find_scores()
        await message.channel.send(msg[0])
        await message.channel.send(msg[1])

    elif message.content.startswith("!csv"):
        scraper.find_scores()
        await message.channel.send(file=discord.File('scores.csv'))

client.run(os.getenv('TOKEN'))