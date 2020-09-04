from Trainer import *
from PokeAPI import *

import asyncio
import discord
import os
import random
import requests

from discord.ext import commands

Token = 'Insert Token Here'

SPAWN_COUNTER = 1
SPAWN_LIMIT = 3

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
        self.pokemon = {}

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

    # TODO
    @commands.command()
    async def catch(self,ctx,name=''):
        
        # Check for a Pokemon name
        if name == '':
            await ctx.send('Please enter a name of Pokemon.')
            return

        pass

    # Returns a list of Pokemon images available for capture
    @commands.command()
    async def available(self,ctx):
        for key in self.pokemon.keys():
            img_file = self.generate_filename(key)
            with open(img_file, 'rb') as fp:
                send_file = discord.File(fp)
                await ctx.send('Who\'s that Pokemon?', file=send_file)

    # TODO: Remove before final version
    @commands.command()
    async def test(self,ctx,name):
        pass

    # TODO: Remove before final version
    @commands.command()
    async def exit(self,ctx):
        await ctx.send('Shutting Down.')
        await self.bot.close()

        if self.bot.is_closed():
            print('Bot shut down successfully.')
        else:
            print('Bot did not terminate properly.')

        # Clear image cache
        self.clear_cache()

    # Bot Listeners

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as')
        print(self.bot.user.name)
        print(self.bot.user.id)
        print('------')

        # Clear image cache
        self.clear_cache()

    @commands.Cog.listener()
    async def on_message(self,message):
        
        # Increment counter for every non-command message
        if message.author.id is not self.bot.user.id and not message.content.startswith("!poke "):
            self.counter+=1
        
            # Check if a Pokemon should be spawned
            if self.counter == SPAWN_COUNTER:
                
                # Reset counter to 0
                self.counter = 0

                # Repeatedly generate Pokemon until a unique Pokemon is found
                while 1:

                    # Generate a random number
                    randNum = random.randint(LOW_BOUND,HIGH_BOUND)

                    # Check if the file exists already in cache
                    if str(randNum) + '.png' in os.listdir('image_cache/'):
                        continue
                    else:
                        break

                # Check to see if the spawn limit has been reached
                if len(self.pokemon) == SPAWN_LIMIT:

                    # Search for the oldest Pokemon
                    oldest_key = 0
                    oldest_time = 0
                    for key,poke in self.pokemon.items():
                        if poke.creation_time < oldest_time or oldest_time == 0:
                            oldest_key = key

                    # Despawn the oldest pokemon
                    del self.pokemon[str(oldest_key)]

                    # Remove image file from cache
                    try:
                        old_filename = self.generate_filename(oldest_key)
                        os.remove(old_filename)
                    except:
                        await message.channel.send('Error despawning old Pokemon.')
                        return

                # Spawn Pokemon in Discord
                try:

                   # Generate Pokemon data
                    new_pokemon = PokeInfo(str(randNum))

                    # Add Pokemon to dictionary
                    self.pokemon[str(randNum)] = new_pokemon

                    # Pull the sprite from the internet
                    sprite = requests.get(str(new_pokemon.sprite))

                    # Generate new filename
                    new_filename = self.generate_filename(randNum)

                    # Save image to a file
                    with open(new_filename, 'wb') as fd:
                        fd.write(sprite.content)
                        fd.close()

                    # Send image to Discord
                    with open(new_filename, 'rb') as fp:
                        img = discord.File(fp)
                        await message.channel.send('Who\'s that Pokemon?', file=img)

                except:
                    await message.channel.send('Error retrieving pokemon data.')
                    return

    # Auxiliary Functions

    # Generates a filepath for a given Pokemon numebr
    def generate_filename(self,num):
        return 'image_cache/img' + str(num) + '.png'

    # Clears image_cache (used upon startup and shutdown)
    def clear_cache(self):
        for file in os.listdir('image_cache/'):
            os.remove('image_cache/' + str(file))

if __name__ == '__main__' :
    bot.add_cog(Pokebot(bot))
    bot.run(Token)