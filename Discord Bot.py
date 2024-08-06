import discord 
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event  ###print console
async def on_ready():
    print(f"We have logged into {bot.user} ")


@bot.event #### ping & pong prefix command
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "!Ping":
        ping = round(bot.latency *1000)
        response = f"Pong!" 
        await message.channel.send(response) 

bot.run("YOUR BOT TOKEN")