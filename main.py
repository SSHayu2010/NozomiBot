
import discord
from discord.ext import commands
from webserver import keep_alive
from decouple import config

TOKEN = config("DISCORD_BOT_SECRET_KEY")
ENV_NAME = config("ENV_NAME")
bot = commands.Bot(command_prefix="!", debug_guilds=[869923009115357215])


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.load_extension('cogs.ranks')

if ENV_NAME == "production":
    keep_alive()

bot.run(TOKEN)
