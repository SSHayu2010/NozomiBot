
from discord.ext import commands
from decouple import config

bot = commands.Bot(command_prefix="!", debug_guilds=[869923009115357215])


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.load_extension('cogs.ranks')

TOKEN = config("DISCORD_BOT_SECRET_KEY")

bot.run(TOKEN)
