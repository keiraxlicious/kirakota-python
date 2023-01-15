#guild stats pagimation

import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = discord.Client(intents=intents)
members = (); member_id = ()

roles = (); role_id = ()

cat = (); cat_id = ()

chan = (); chan_id = ()
#Pagination
class DataGrab(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.TheData = {}
        self.Page = 0
        self.DataPost = {}
        members = (); member_id = ()

        roles = (); role_id = ()

        cat = (); cat_id = ()

        chan = (); chan_id = ()

    async def Data(self,ctx):        
        guild = ctx.guild
        members = [f"{member.name}"for member in guild.members]
        member_id = [f"{member.id}"for member in guild.members]

        roles = [f"{role.name}"for role in guild.roles]
        role_id = [f"{role.id}"for role in guild.roles]

        cat = [f"{category.name}"for category in guild.categories]
        cat_id = [f"{category.id}"for category in guild.categories]

        chan = [f"{channel.name}"for channel in guild.channels]
        chan_id = [f"{channel.id}"for channel in guild.channels]

        member_list = "\n".join([f"[{member.name}]({member.id})" for member in guild.members])
        role_list = "\n".join([f"[{role.name}]({role.id})" for role in guild.roles])
        category_list = "\n".join([f"[{category.name}]({category.id})" for category in guild.categories])
        channel_list = "\n".join([f"[{channel.name}]({channel.id})" for channel in guild.channels])

    @commands.command()
    async def PartyLikeTheCIA(self, ctx):
        # this Guild object holds all the info you want, now we just need to sift though it.
        self.TheData = ctx.guild
        Embed = discord.Embed(title=self.TheData.name,
                description=f"This Server has \n {len(self.TheData.members)} Users \n {len(self.TheData.roles)} Roles\n and {len(self.TheData.channels)} channels in {len(self.TheData.categories)} categories",
                colour=discord.Colour(0xe91e63))
        Embed.add_field(name="Member Names", value=f"\n{len(self.TheData.members)}")
        Embed.add_field(name="Member ID's", value=f"{len(self.TheData.roles)}", inline=True)
        Embed.add_field(name="Member ID's", value=f"{len(self.TheData.roles)}", inline=False)
        Embed.add_field(name="Member ID's", value=f"{len(self.TheData.roles)}", inline=True)


        DataMessage = await ctx.send(embed=Embed)
        self.DataPost[DataMessage] = {"User": ctx.author}
    @discord.ui.button(label="Page 1", style=discord.ButtonStyle.blurple)
    async def page1(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        self.Page = 0

async def setup(bot):
    await bot.add_cog(DataGrab(bot))


#all files saved from main


# from listeners import index
# from skills import index
# from slashCmds import index
# import logging
# import settings
import os
import discord 
from discord.ext import commands
import settings
print(discord.__version__)
#logger = settings.logging.getLogger("kirakota")
# member_list = {}
# role_list = {}
# category_list = {}
# channel_list = {}
# member_list_data = (f"\nGuild members:\n{member_list}")
# role_list_data = (f"\nGuild roles:\n{role_list}")
# category_list_data = (f"\nGuild channels:\n{category_list}")
# channel_list_data = (f"\nGuild channels:\n{channel_list}")


def run():
    intents = discord.Intents.all()
    kirakota = commands.Bot(command_prefix="!", intents=intents)
    kirakota.run(settings.DISCORD_API_SECRET, root_logger=True)
    # logger.info(f"User: {kirakota.user} (ID: {kirakota.user.id})")
    # @kirakota.event()
    # async def on_ready(ctx):
    #     guild = ctx.guild
    #     await on_ready(guild)

    #     # Print out a list of guild members
    #     member_list = "\n".join(
    #         [f"{member.name} ({member.id})" for member in guild.members])
    #     print(f"Guild members:\n{member_list}")
    #     member_list_data = (f"\nGuild members:\n{member_list}")
    #     await ctx.send(f"\nGuild members:\n{member_list}")

    #     # Print out a list of roles
    #     role_list = "\n".join(
    #         [f"{role.name} ({role.id})" for role in guild.roles])
    #     print(f"\nGuild roles:\n{role_list}")
    #     role_list_data = (f"\nGuild roles:\n{role_list}")
    #     await ctx.send(f"\nGuild roles:\n{role_list}")

    #     # Print out a list of categories
    #     category_list = "\n".join(
    #         [f"{category.name} ({category.id})" for category in guild.categories])
    #     print(f"\nGuild categories:\n{category_list}")
    #     category_list_data = (f"\nGuild categories:\n{category_list}")
    #     await ctx.send(f"\nGuild categories:\n{category_list}")

    #     # Print out a list of channels
    #     channel_list = "\n".join(
    #         [f"{channel.name} ({channel.id})" for channel in guild.channels])
    #     print(f"\nGuild channels:\n{channel_list}")
    #     channel_list_data = (f"\nGuild channels:\n{channel_list}")
    #     await ctx.send(f"\nGuild channels:\n{channel_list}")
    
    # @kirakota.command()
    # async def data():
    #     await kirakota.send(f"\n{member_list_data}\n{role_list_data}\n{category_list_data}\n{channel_list_data}")
    
    @kirakota.event()
    async def on_ready():

            
        for root, dirs, files in os.walk(settings.CMDS_DIR):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    extension_name = file_path.replace(settings.CMDS_DIR, "").replace(os.sep, ".")[:-3]
                    await kirakota.load_extension(extension_name)
            
        for root, dirs, files in os.walk(settings.COGS_DIR):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    extension_name = file_path.replace(settings.COGS_DIR, "").replace(os.sep, ".")[:-3]
                    await kirakota.load_extension(extension_name)
        # for cmd_file in settings.CMDS_DIR.glob("*.py"):
        #     if cmd_file.name != "__init__.py":
        #         await kirakota.load_extension(f"cmds.{cmd_file.name[:-3]}")
        
        # for cog_file in settings.COGS_DIR.glob("*.py"):
        #     if cog_file.name != "__init__.py":
        #         await kirakota.load_extension(f"listeners/*.{cog_file.name[:-3]}")
    @kirakota.command()
    async def load(ctx, cog: str):
        await kirakota.load_extension(f"cogs.{cog.lower()}")
    @kirakota.command()
    async def unload(ctx, cog: str):
        await kirakota.unload_extension(f"cogs.{cog.lower()}")
    @kirakota.command()
    async def reload(ctx, cog: str):
        await kirakota.unload_extension(f"cogs.{cog.lower()}")
        await kirakota.reload_extension(f"cogs.{cog.lower()}")

    kirakota.run(settings.DISCORD_API_SECRET, root_logger=True)
if __name__ == "__main__":
    run()


# def run():
#     intents = discord.Intents.all()
#     kirakota = commands.Bot(command_prefix="!", intents=intents)
#     kirakota.run(settings.DISCORD_API_SECRET, root_logger=True)
#     # logger.info(f"User: {kirakota.user} (ID: {kirakota.user.id})")


#     @kirakota.command()
#     async def guildStats(ctx):
#         guild = ctx.guild
#         await on_ready(guild)

#         # Print out a list of guild members
#         member_list = "\n".join(
#             [f"{member.name} ({member.id})" for member in guild.members])
#         print(f"Guild members:\n{member_list}")

#         # Print out a list of roles
#         role_list = "\n".join(
#             [f"{role.name} ({role.id})" for role in guild.roles])
#         print(f"\nGuild roles:\n{role_list}")

#         # Print out a list of categories
#         category_list = "\n".join(
#             [f"{category.name} ({category.id})" for category in guild.categories])
#         print(f"\nGuild categories:\n{category_list}")

#         # Print out a list of channels
#         channel_list = "\n".join(
#             [f"{channel.name} ({channel.id})" for channel in guild.channels])
#         print(f"\nGuild channels:\n{channel_list}")

#     @kirakota.event()
#     async def on_ready(guild):
#         # Print the value of "id" to see what is being passed as the argument
#         print(id)
#         try:
#             # Try to get the guild with the specified ID
#             guilds = kirakota.get_guild(id)
#         except Exception as e:
#             # If an exception is raised, print the exception message
#             print(e)
#         # Print out a list of guild members

        
#         member_list = "\n".join(
#             [f"{member.name} ({member.id})" for member in guild.members])
#         print(f"Guild members:\n{member_list}")

#         # Print out a list of roles
#         role_list = "\n".join(
#             [f"{role.name} ({role.id})" for role in guild.roles])
#         print(f"\nGuild roles:\n{role_list}")

#         # Print out a list of categories
#         category_list = "\n".join(
#             [f"{category.name} ({category.id})" for category in guild.categories])
#         print(f"\nGuild categories:\n{category_list}")

#         # Print out a list of channels
#         channel_list = "\n".join(
#             [f"{channel.name} ({channel.id})" for channel in guild.channels])
#         print(f"\nGuild channels:\n{channel_list}")


#     kirakota.run(settings.DISCORD_API_SECRET, root_logger=True)
# if __name__ == "__main__":
#     run()
