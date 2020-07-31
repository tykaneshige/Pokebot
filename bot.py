import asyncio
import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!poke ')

# Bot ommands
@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

@bot.command()
async def exit(ctx):
    await ctx.send('Shutting down.')
    await bot.close()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

bot.run('NzM4MTk4NzkwNjk5MzUyMTE1.XyIbMg.TCublKX6CjNp3U2R9PZUZobY8ow')
