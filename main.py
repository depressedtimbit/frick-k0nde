import os
import string 
import discord
from discord.ext import commands

client = discord.Client()

intents = discord.Intents.default()
intents.presences = True
client = commands.Bot(command_prefix ='$%', help_command=None) 

@client.event 
async def on_ready():
  print('ready')

bad_bad_names = [
  'twitter.com/h0nde', 'h0nde'
  ]

@client.event
async def on_member_join(member):  
  for item in bad_bad_names:
    if member.name.lower.find(item):
      await member.kick(reason="take a sip 🥤")
      channel = await client.fetch_channel(os.getenv("log_channel"))
      await channel.send('user kicked ({}), take a sip 🥤'.format(member.id))

client.run(os.getenv("token")) 