
import discord
from discord.ext import commands
from webserver import keep_alive
import os

bot = commands.Bot(command_prefix="!", debug_guilds=[869923009115357215])


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.load_extension('cogs.ranks')

keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET_KEY")

TOKEN = "OTczNDA4NDMxODE1OTQyMTY0.GCHG_r.LFh1560BiLYSMLEXB7qxaYb5n43dT2sjNlYCpw"
bot.run(TOKEN)
