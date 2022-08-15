import os, random, discord

from dotenv import load_dotenv
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GUILD_ID = int(os.getenv('GUILD_ID'))
CHANNEL = int(os.getenv('BOT_CMD'))

client = commands.Bot(command_prefix='!')
slash = SlashCommand(client, sync_commands=True)

"""Start up bot status message on boot"""
@client.event
async def on_ready(): await client.change_presence(activity=discord.Game('/ping me'))

"""Filter message based on author and occasionally 'uwuify' read message"""
@client.event
async def on_message(message):
    if message.author == client.user: return                # checks if professor
    if message.channel.id != CHANNEL: return                # checks if from bot channel
    

@slash.slash(name='ping', description="ping RobBot", guild_ids=[GUILD_ID])
async def _(ctx:SlashContext): 
    await ctx.reply("Pong")

client.run(TOKEN)