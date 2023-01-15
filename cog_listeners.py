import discord
from discord.ext import commands

class Name1(commands.Cog):

    def __init__(self, kirakota):
        self.kirakota = kirakota

async def setup(kirakota):
    await kirakota.add_cog(Name1(kirakota))

