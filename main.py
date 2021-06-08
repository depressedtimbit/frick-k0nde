import logging
from os import getenv
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.utils import get



banwords = ['h0nde', 'twitter.com/h0nde'] # Ban-words for Detecting
log_channel = getenv('log_channel') # Name of channel of logs
ban_text = 'User {0} (ID: `{1}`) was banned, take a sip 🥤'
ban_reason = "Take a sip 🥤"


# Setting up Logging
logging.basicConfig(
  format='[%(asctime)s][%(levelname)s][%(name)s]: %(message)s',
  level=logging.INFO
)
log = logging.getLogger('bot')

# Loads Predefined Environment Variables
load_dotenv()

# Initialize Bot Class
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='%', help_command=None, intents=intents)


# Event: On Bot is Ready
@bot.event
async def on_ready():
  log.info('Bot is Ready as {0}!'.format(bot.user))


# Event: On Member is Joined to Guild
@bot.event
async def on_member_join(member):
  for word in banwords:
    if member.name.lower().find(word):
      await member.ban(reason=ban_reason)
      channel = get(member.guild.channels, name='general')
      await channel.send(ban_text.format(member.mention, member.id))
      break

# Running Bot from Bot Token
bot.run(getenv('token'))
