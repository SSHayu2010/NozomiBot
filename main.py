
from operator import truediv
from pickle import TRUE
from sys import prefix
import discord
from discord.ext import commands
from discord.commands import Option
from embeds import PHY_CHARACTERS

bot = commands.Bot(command_prefix="!", debug_guilds=[869923009115357215])

boss_hp = 7500

# all fields are optional
embed = discord.Embed(title="Kokkoro - Rank Info", description="",
                      colour=discord.Colour(0x6cfa4f))
# change this link to an image link, e.g a cdn.discord image
embed.add_field(name="Rank", value="10-2 (Abril, 2022)", inline=True)
embed.add_field(name="Estrellas", value=":star: :star: :star: :star: :star:", inline=True)
embed.add_field(name="Nivel UE", value="1", inline=True)
embed.add_field(name="Restricciones / Notas adicionales", value="Requiere nivel 121 si aun la tienes", inline=True)
embed.set_thumbnail(url="https://media.discordapp.net/attachments/972431199974871050/973136078305370124/kokkoro.png")
embed.set_image(url="https://i.imgur.com/3UuPZFP.jpeg")
embed.set_footer(text="AnneBot")


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.slash_command(description="Units - Rank Info")
async def urank(ctx, character: Option(str)):
    character = character.lower()
    if character in PHY_CHARACTERS:
        await ctx.respond(embed=PHY_CHARACTERS[character], ephemeral=True)
    else:
        await ctx.respond(F'El personaje {character} no fue encontrado', ephemeral=True)


TOKEN = "OTczNDA4NDMxODE1OTQyMTY0.GCHG_r.LFh1560BiLYSMLEXB7qxaYb5n43dT2sjNlYCpw"
bot.run(TOKEN)
