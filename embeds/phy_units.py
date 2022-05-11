
import discord

from .constants import (
    LAST_UPDATE,
    FIVE_STAR,
    RANK_INFO,
    RANK_LABEL,
    STAR_LABEL,
    UE_LEVEL_LABEL,
    NOTES_LABEL,
    ANNE_BOT_LABEL,
)


# Constants for all characters
PHY_COLOR = discord.Colour(0x6cfa4f)

# Unit vars
KOKKORO_RANK = '10-2'
KOKKORO_STARS = FIVE_STAR
KOKKORO_UE_LEVEL = '1'
KOKKORO_NOTES = 'Requiere nivel 121 si aun la tienes'
KOKKORO_IMAGE = 'https://i.imgur.com/3UuPZFP.jpeg'
KOKKORO_THUMBNAIL = 'https://media.discordapp.net/attachments/972431199974871050/973136078305370124/kokkoro.png'

# Unit embed
KOKKORO_EMBED = discord.Embed(title=f"Kokkoro - {RANK_INFO}", description="", colour=PHY_COLOR)
KOKKORO_EMBED.add_field(name=RANK_LABEL, value=f"{KOKKORO_RANK} {LAST_UPDATE}", inline=True)
KOKKORO_EMBED.add_field(name=STAR_LABEL, value=KOKKORO_STARS, inline=True)
KOKKORO_EMBED.add_field(name=UE_LEVEL_LABEL, value=KOKKORO_UE_LEVEL, inline=True)
KOKKORO_EMBED.add_field(name=NOTES_LABEL,
                        value=KOKKORO_NOTES, inline=True)
KOKKORO_EMBED.set_thumbnail(
    url=KOKKORO_THUMBNAIL
)
KOKKORO_EMBED.set_image(url=KOKKORO_IMAGE)
KOKKORO_EMBED.set_footer(text=ANNE_BOT_LABEL)


PHY_CHARACTERS = {
    'kokkoro': KOKKORO_EMBED,
}
