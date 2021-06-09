import logging
import re
from os import environ
from dotenv import load_dotenv
import discord
from discord.ext import commands



regex_banwords = "(?i)^.*(?:twitter.com/)?h0nde" # Regex of ban words
ban_text = 'User {0} (ID: `{1}`) was kicked, take a sip :cup_with_straw:'
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
  if re.match(regex_banwords, member.name):
    await member.ban(reason=ban_reason)
    if environ.get('log_channel'):
      channel = await bot.fetch_channel(environ.get('log_channel'))
      await channel.send(ban_text.format(member.mention, member.id))

# Running Bot from Bot Token
bot.run(environ.get('token'))
