import asyncio
import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')

# Bot ommands
@bot.command
async def ping(ctx):
    await ctx.send('pong!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

<<<<<<< HEAD
bot.run('Insert Token Here')
=======
client.run('Insert Token Here')
>>>>>>> 09ac4a3f09bc972cc94ac56aab72a04fea315170
