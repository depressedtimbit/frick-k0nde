import os
import string 
import discord
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix = os.getenv(prefix), help_command=None) 

intents = discord.Intents.default()
intents.presences = True

bad_bad_names = [
  'twitter.com/h0nde', 'h0nde', 'honde'
  ]
#lower case only, anyone who's username contains a string is this list will be kicked

@client.event(enabled=False)
async def on_member_join(member):
  if member.name.lower() in bad_bad_names:
    member.kick(reason="take a sip 🥤")
    channel = await client.fetch_channel(os.getenv("log_channel"))
    channel.send('user kicked ({}), take a sip 🥤'.format(member.id))\
  else:
     return()
client.run(os.getenv("token")) 