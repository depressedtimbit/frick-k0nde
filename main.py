import os
import string 
import discord
from discord.ext import commands

client = discord.Client()

client = commands.Bot(help_command=None) 

intents = discord.Intents.default()
intents.presences = True

@client.event
async def on_member_join(member):
  if member.name.lower.find('twitter.com/h0nde') >= 1:
    member.kick(reason="take a sip 🥤")
    channel = await client.fetch_channel(os.getenv("log_channel"))
    channel.send('user kicked ({}), take a sip 🥤'.format(member.id))

client.run(os.getenv("token")) 