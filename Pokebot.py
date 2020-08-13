import asyncio
import discord

from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!poke ')
Token = 'Insert Token Here'



class Pokebot(commands.Cog) :
    
    def __init__(self,bot):
        self.bot=bot
        self.counter = 0
    
    # Bot Commands
    @commands.command()
    async def ping(self,ctx):
        await ctx.send('pong!')
    
    @commands.command()
    async def exit(self,ctx):
        await ctx.send('Shutting down.')
        await self.bot.close()

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id is not self.bot.user.id and not message.content.startswith("!poke "):
            self.counter+=1

    @commands.command()
    async def count(self,ctx):
        await ctx.send(self.counter)

if __name__ == '__main__' :
    bot.add_cog(Pokebot(bot))
    bot.run(Token)
