# from listeners import index
# from skills import index
# from slashCmds import index
# import logging
# import settings


import os
import settings
import discord
from discord.ext import commands
print(discord.__version__)
logger = settings.logging.getLogger("kirakota")


def run():
    intents = discord.Intents.all()
    kirakota = discord.Client(intents=intents)
    kirakota.run(settings.DISCORD_API_SECRET, root_logger=True)

    @kirakota.command()
    async def guildStats(ctx):
        guild = ctx.guild
        await on_ready(guild)

        # Print out a list of guild members
        member_list = "\n".join(
            [f"{member.name} ({member.id})" for member in guild.members])
        print(f"Guild members:\n{member_list}")

        # Print out a list of roles
        role_list = "\n".join(
            [f"{role.name} ({role.id})" for role in guild.roles])
        print(f"\nGuild roles:\n{role_list}")

        # Print out a list of categories
        category_list = "\n".join(
            [f"{category.name} ({category.id})" for category in guild.categories])
        print(f"\nGuild categories:\n{category_list}")

        # Print out a list of channels
        channel_list = "\n".join(
            [f"{channel.name} ({channel.id})" for channel in guild.channels])
        print(f"\nGuild channels:\n{channel_list}")

    @kirakota.event()
    async def on_ready(guild):
        # Print the value of "id" to see what is being passed as the argument
        print(id)
        try:
            # Try to get the guild with the specified ID
            guilds = kirakota.get_guild(id)
        except Exception as e:
            # If an exception is raised, print the exception message
            print(e)
        # Print out a list of guild members
        member_list = "\n".join(
            [f"{member.name} ({member.id})" for member in guild.members])
        print(f"Guild members:\n{member_list}")

        # Print out a list of roles
        role_list = "\n".join(
            [f"{role.name} ({role.id})" for role in guild.roles])
        print(f"\nGuild roles:\n{role_list}")

        # Print out a list of categories
        category_list = "\n".join(
            [f"{category.name} ({category.id})" for category in guild.categories])
        print(f"\nGuild categories:\n{category_list}")

        # Print out a list of channels
        channel_list = "\n".join(
            [f"{channel.name} ({channel.id})" for channel in guild.channels])
        print(f"\nGuild channels:\n{channel_list}")


if __name__ == "__main__":
    run()
