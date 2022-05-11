
from operator import truediv
from pickle import TRUE
from sys import prefix
import discord


client = discord.Client()

boss_hp = 7500

# all fields are optional
embed = discord.Embed(title="Kokkoro - Rank Info", description="",
                      URL="https://example.com/", colour=discord.Colour(0x6cfa4f))
# change this link to an image link, e.g a cdn.discord image
embed.add_field(name="Rank", value="10-2 (Abril, 2022)", inline=True)
embed.add_field(name="Estrellas", value=":star: :star: :star: :star: :star:", inline=True)
embed.add_field(name="Nivel UE", value="1", inline=True)
embed.add_field(name="Restricciones / Notas adicionales", value="Requiere nivel 121 si aun la tienes", inline=True)
embed.set_thumbnail(url="https://media.discordapp.net/attachments/972431199974871050/973136078305370124/kokkoro.png")
embed.set_image(url="https://i.imgur.com/3UuPZFP.jpeg")
embed.set_footer(text="AnneBot")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ok'):
        global boss_hp
        await message.channel.send(f'A2 Current {boss_hp}')

    if message.content.startswith('!hit'):
        boss_hp -= 1000
        await message.channel.send(f'A2 Current {boss_hp}')

    if message.content.startswith('!kokkoro'):
        await message.channel.send(embed=embed)

TOKEN = "OTczNDA4NDMxODE1OTQyMTY0.GCHG_r.LFh1560BiLYSMLEXB7qxaYb5n43dT2sjNlYCpw"
client.run(TOKEN)
