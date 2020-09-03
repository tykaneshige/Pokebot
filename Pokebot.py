from Trainer import *

import asyncio
import discord
import random

from discord.ext import commands

Token = 'Insert Token Here'

LOW_BOUND = 1
HIGH_BOUND = 151

start_text = """ 
Hello there! Welcome to the world of Pokémon!
My name is Oak! People call me the Pokémon Prof!
This world is inhabited by creatures called Pokémon!
For some people, Pokémon are pets. Others use them for fights...
Your very own Pokémon adventure is about to unfold!
A world of dreams and adventures with Pokémon awaits! Let\'s go!
"""

client = discord.Client()
bot = commands.Bot(command_prefix='!poke ')

class Pokebot(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot

        self.trainers = {}
        self.pokemon = []

        self.counter = 0
    
    # Bot Commands

    # Basic Connection Tests
    @commands.command()
    async def ping(self,ctx):
        await ctx.send('pong!')

    # Start Command
    @commands.command()
    async def start(self,ctx,name=''):

        # Check for a trainer name
        if name == '':
            await ctx.send('Please pass a name. (Format: \' !poke start <trainer_name>\'')
            return

        # Check if the trainer exists 
        if ctx.author.id not in self.trainers:

            # Add discord ID to trainer list
            self.trainers[ctx.author.id] = Trainer(name)

            # Append a line to the opening text
            opening_text = start_text + 'Welcome to the world of Pokemon, {}!'.format(name)

            # Opening prompt from Professor Oak
            await ctx.send(opening_text)

        else:
            await ctx.send("You are already a Trainer!")
            return

    # Returns a list of all trainers in the server
    @commands.command()
    async def trainers(self,ctx):

        # Compile a trainer list
        trainer_list = ''
        for trainer in self.trainers.values():
            trainer_list += str(trainer.name)

        # Send the trainer list to the server
        await ctx.send(trainer_list)

    # Rename the trainer owned by the user who made the request
    @commands.command()
    async def rename(self,ctx,name=''):
        
        # Check for a trainer name
        if name == '':
            await ctx.send('Please enter pass a name.')
            return
        
        try:

            # Verify if trainer name is already in use
            for trainer in self.trainers.values():
                if trainer.name == name:
                    await ctx.send('\'{}\' is already taken.'.format(name))
                    return
            
            # Change trainer name
            self.trainers[ctx.author.id].name = name

            await ctx.send('Successfully changed trainer name.')

        except:
            await ctx.send('Error renaming trainer.')

    # TODO: Remove before final version
    @commands.command()
    async def count(self,ctx):
        await ctx.send(self.counter)

    # TODO: Remove before final version
    @commands.command()
    async def exit(self,ctx):
        await ctx.send('Shutting Down.')
        await self.bot.close()

        if self.bot.is_closed():
            print('Bot shut down successfully.')
        else:
            print('Bot did not terminate properly.')

    # Bot Listeners

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as')
        print(self.bot.user.name)
        print(self.bot.user.id)
        print('------')

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id is not self.bot.user.id and not message.content.startswith("!poke "):
            self.counter+=1
        
            if self.counter == 5:
                self.counter = 0
                randNum = random.randint(LOW_BOUND,HIGH_BOUND)
                await message.channel.send("A wild Pokemon #" + str(randNum) +" has appeared!")

if __name__ == '__main__' :
    bot.add_cog(Pokebot(bot))
    bot.run(Token)