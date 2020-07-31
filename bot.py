import asyncio
import discord
from discord.ext import commands
import random

client = discord.Client()
bot = commands.Bot(command_prefix='!')

# Bot Commands
@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

@bot.command()
async def exit(ctx):
    await ctx.send('Shutting down.')
    await bot.close()

@bot.command()
async def quote(ctx):
    responses = open('quotes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

bot.run('NzM4MTk4NzkwNjk5MzUyMTE1.XyIbMg.VO_yepVM3qJqBgmR4NnOzaPktko')

