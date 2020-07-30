import asyncio
import discord

client = discord.Client()
prefix = '!'
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith(prefix + 'test'):
        counter = 0
        tmp = await message.channel.send('Calculating messages...')
        '''
        async for log in guild.audit_logs(limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
        '''
        await message.channel.send('I can\'t count')
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await message.channel.send('Done sleeping')
    elif message.content.startswith(prefix + 'ping'):
        tmp = await message.channel.send('pong!')




client.run('Insert Token Here')