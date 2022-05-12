import discord
from discord.ext import commands
from embeds.units import generate_embeds
from discord.commands import Option


class Ranks(commands.Cog):  # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot):  # this is a special method that is called when the cog is loaded
        self.bot = bot
        self.unit_embeds = generate_embeds()

    @commands.slash_command(description="Units - Rank Info")
    async def urank(self, ctx, character: Option(str)):
        character = character.lower()
        if character in self.unit_embeds:
            await ctx.respond(embed=self.unit_embeds[character], ephemeral=True)
        else:
            await ctx.respond(F'El personaje {character} no fue encontrado', ephemeral=True)


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Ranks(bot))  # add the cog to the bot
