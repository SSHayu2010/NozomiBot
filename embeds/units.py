
import discord

from .constants import (
    ALL_STARS,
    RANK_INFO,
    RANK_LABEL,
    STAR_LABEL,
    UE_LEVEL_LABEL,
    NOTES_LABEL,
    ANNE_BOT_LABEL,
    UNIT_PHY_TYPE,
    FIELD_NAME,
    FIELD_RANK,
    FIELD_STARS,
    FIELD_UE_LEVEL,
    FIELD_NOTES,
    FIELD_IMAGE,
    FIELD_THUMBNAIL,
    FIELD_SPECIFIC_RANK,
    FIELD_UNIT_TYPE,
)
from .services import (
    extract_unit_database_from_csv,
    get_current_date,
    refactor_unit_name,
    transform_unit_data_to_objects,
)


# Constants for all characters
PHY_COLOR = discord.Colour(0x6cfa4f)
MAGIC_COLOR = discord.Colour.blurple()


def generate_embed_for_unit(unit_data):
    """Generate an embed for a unit"""
    last_update = get_current_date()
    color = PHY_COLOR if unit_data.get(FIELD_UNIT_TYPE, UNIT_PHY_TYPE) == UNIT_PHY_TYPE else MAGIC_COLOR
    unit_name = str(unit_data.get(FIELD_NAME))
    unit_correct_name = refactor_unit_name(str(unit_data.get(FIELD_NAME)))
    embed_unit = discord.Embed(title=f"{unit_correct_name} - {RANK_INFO}", description="", colour=color)
    embed_unit.add_field(name=RANK_LABEL, value=f"{unit_data.get(FIELD_RANK)} ({last_update})", inline=True)
    embed_unit.add_field(name=STAR_LABEL, value=ALL_STARS.get(unit_data.get(FIELD_STARS, '1')), inline=True)
    embed_unit.add_field(name=UE_LEVEL_LABEL, value=unit_data.get(FIELD_UE_LEVEL, '1'), inline=True)
    embed_unit.add_field(name=NOTES_LABEL, value=unit_data.get(FIELD_NOTES, 'No hay restricciones'), inline=True)
    embed_unit.set_thumbnail(url=unit_data.get(FIELD_THUMBNAIL))
    embed_unit.set_image(url=unit_data.get(FIELD_IMAGE))
    embed_unit.set_footer(text=ANNE_BOT_LABEL)
    return unit_name, embed_unit


def generate_embeds():
    """Generate all embeds for all units"""
    fields, rows = extract_unit_database_from_csv()
    unit_database = transform_unit_data_to_objects(fields, rows)
    unit_embeds = {}
    magic_units = []
    physical_units = []
    for unit_data in unit_database:
        unit_name, embed_unit = generate_embed_for_unit(unit_data)
        unit_embeds[unit_name] = embed_unit
        if unit_data.get(FIELD_UNIT_TYPE) == UNIT_PHY_TYPE:
            physical_units.append(unit_name)
        else:
            magic_units.append(unit_name)
    return unit_embeds, physical_units, magic_units


def generate_embed_unit_list(phy_units, magic_units):
    """Generate a list of units"""
    phy_units_reformated = 'None\n'
    for phy_unit in phy_units:
        phy_units_reformated += f"{refactor_unit_name(phy_unit)}\n"

    magic_units_reformated = 'None\n'
    for magic_unit in magic_units:
        magic_units_reformated += f"{refactor_unit_name(magic_unit)}\n"

    embed_list = discord.Embed(
        title="Lista de personajes - AnneBot",
        description="Lista de personajes que se pueden consultar:",
        colour=discord.Colour(0x6cfa4f)
    )
    embed_list.add_field(name="Fisicos", value=f'```{phy_units_reformated}```', inline=True)
    embed_list.add_field(name="Magicos", value=f'```{magic_units_reformated}```', inline=True)
    embed_list.set_thumbnail(url="https://i.imgur.com/p9U644y.jpg")
    return embed_list
