# import os
# import discord 
# from discord.ext import commands
# import settings
# from settings import*
# from extHndlr import*

# # logger = settings.logging.getLogger("kirakota"){extension}.{subdir}.{module_name}"))
            
# def run():
#     intents = discord.Intents.all()
#     kirakota = commands.Bot(command_prefix="!", intents=intents)
#     # @kirakota.command()
#     # async def loadall(ctx):
#     #     extension_handler = ExtensionHandler(kirakota)
#     #     await extension_handler.load_all_extensions(ctx)
#     # @kirakota.command()
#     # async def unloadall(ctx):
#     #     extension_handler = ExtensionHandler(kirakota)
#     #     await extension_handler.unload_all_extensions(ctx)
#     # @kirakota.command()
#     # async def reloadall(ctx):
#     #     extension_handler = ExtensionHandler(kirakota)
#     #     await extension_handler.reload_all_extensions(ctx)
#     # @kirakota.command()
#     # async def reload(self, ctx, extension_name):
#     #     extension_handler = ExtensionHandler(kirakota)
#     #     await extension_handler.reload_extension(ctx, extension_name)
#     # @kirakota.command()
#     # async def unload(self, ctx, extension_name):
#     #     extension_handler = ExtensionHandler(kirakota)
#     #     await extension_handler.unload_extension(ctx, extension_name)
#     # @kirakota.command()
#     # async def load(self, ctx, extension_name):
#     #     extension_handler = ExtensionHandler(kirakota)
#     #     await extension_handler.load_extension(ctx, extension_name)
#     # @kirakota.event 
#     # async def on_ready():
#     #     launcher = launchExtensions()
#     #     await launcher.extensions(kirakota)
# # run()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # | | | - - - old way fail/safe
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#     # @kirakota.event()
#     # async def on_ready():
#     #     logger.info(f"User: {kirakota.user} (ID: {kirakota.user.id})")
#     #     for cog_file in settings.COGS_DIR.glob("*.py"):
#     #         if cog_file != "__init__.py":
#     #             await kirakota.load_extension(f"cogs.{cog_file.name[:-3:]}")
#     #     for cmd_file in settings.CMDS_DIR.glob("*.py"):
#     #         if cmd_file.name != "__init__.py":
#     #             await kirakota.load_extension(f"cmds.{cmd_file.name[:-3]}")
#     # # @kirakota.command()
#     # # async def load(ctx, extension):
#     # #     await kirakota
#     # @kirakota.command()
#     # async def load(ctx, extension):
#     #     await kirakota.load_extension(f'cogs.{extension}')
#     #     await ctx.send(f'{extension} loaded.')
#     # @kirakota.command()
#     # async def unload(ctx, extension):
#     #     await kirakota.unload_extension(f'cogs.{extension}')
#     #     await ctx.send(f'{extension} unloaded.')
#     # @kirakota.command()
#     # async def reload(ctx, extension):
#     #     await kirakota.reload_extension(f'cogs.{extension}')
#     #     await ctx.send(f'{extension} reloaded.')
#     # async def load_extensions():
#     #     for filename in os.listdir("./cogs"):
#     #         if filename.endswith(".py"):
#     #             # cut off the .py from the file name
#     #             await kirakota.load_extension(f"cogs.{filename[:-3]}")



#     kirakota.run(settings.DISCORD_API_SECRET, root_logger=True)
# run()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # | | | - - - old way fail/safe
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



# class launchExtensions():
#     def __init__(self):
#         self.extension = "cog_extensions"

#     async def extensions(kirakota, self.extension):
#         for subdir in os.listdir("cog_extensions"):
#             for module in os.listdir(os.path.join("cog_extensions/"+subdir)):
#                 cog_extensions_path = os.path.abspath(f"cog_extensions/{subdir}")    
#                 if not module.endswith('.py') or module == '__pycache__':
#                     continue   
#                 module_name = module[:-3]
#             extensionName =(os.path.join(f"cog_extensions.{subdir}.{module_name}"))

# def run():
#     intents = discord.Intents.all()
#     kirakota = commands.Bot(command_prefix="!", intents=intents)
#     dataName=()

#     @kirakota.event 
#     async def on_ready():
#         await kirakota.load_extension(extensionName)
        

    # def createEmbed(self, data):
    #     embed = discord.Embed(title=f"{dataName}")
    #     for item in data:
    #         embed.add_field(name=item['label'], value=item[''], inline=False)
    #     return embed



    # async def dataLoad():
    #     for subdir in os.listdir("cog_extensions"):
    #         for module in os.listdir(os.path.join("cog_extensions/"+subdir)):           
    #             if not module.endswith('.py') or module == '__pycache__':
    #                 continue
    #             module_name = module[:-3]
    #             extensionData = (os.path.join(f"cog_extensions.{subdir}.{module_name}"))
    #             for each in extensionData:
    #                 embed = discord.Embed(title=f"{dataName}")
    #                 embed.add_field(name=each.qualified_name, value=each.qualified_value, inline=True)
    #                 print (extensionData.qualified_name)




    # @kirakota.event 
    # async def on_ready():
    #     await kirakota.load_extension(extensionName)     
    #     logger.info(f"User: {kirakota.user} (ID: {kirakota.user.id})")
    #     print(f"Guild Intents: {kirakota.intents.guilds}")
    #     print(f"Message Intents: {kirakota.intents.messages}")    
    #     print(f"User: {kirakota.user} (ID: {kirakota.user.id})")
    #     #for each sub directory in>> directory folder name
    #     for subdir in os.listdir("cog_extensions"):
    #         # then for each cmd/cog module in>> directory subdirectories
    #         for module in os.listdir(os.path.join("cog_extensions/"+subdir)):
    #             #cog extensions path will ==>> extension folder/subdir data   
    #             cog_extensions_path = os.path.abspath(f"cog_extensions/{subdir}")
    #             #then prints the cog extensions path `E:\!python\Bot Python Template\cog_extensions\cogs`
    #             print(cog_extensions_path)  
    #             #if the module doesn't end w/ .py or it doesn't equal __pycache__, it will continue      
    #             if not module.endswith('.py') or module == '__pycache__':
    #                 continue   
    #             #rename module(file) to module_name and remove the last 3 characters aka ".py"
    #             module_name = module[:-3]
    #             #then you want to load unload or reload the extensions. 
    #             #this takes the raw data. `(os.path.join(f"cog_extensions.{subdir}.{module_name}"))`
    #             #
    #             await kirakota.load_extension(os.path.join(f"cog_extensions.{subdir}.{module_name}"))
    #             print(f"\n[{module_name.qualified_name}]( now loaded.)")


    # @kirakota.command()
    # async def load(ctx):
    #     await ctx.send("```md\n[Extensions]( are now loading.)```")
    #     for subdir in os.listdir("cog_extensions"):
    #         for module in os.listdir(os.path.join("cog_extensions/"+subdir)):           
    #             if not module.endswith('.py') or module == '__pycache__':
    #                 continue
    #             module_name = module[:-3]
    #             await kirakota.load_extension(os.path.join(f"cog_extensions.{subdir}.{module_name}"))
    #             await ctx.send(f"```md\n[{module_name}]( now loaded.)```")
        
    # @kirakota.command()
    # async def unload(ctx):
    #     await ctx.send("`md\n[Extensions]( are now unloading.)`")
    #     for subdir in os.listdir("cog_extensions"):
    #         for module in os.listdir(os.path.join("cog_extensions/"+subdir)):           
    #             if not module.endswith('.py') or module == '__pycache__':
    #                 continue
    #             module_name = module[:-3]
    #             await kirakota.unload_extension(os.path.join(f"cog_extensions.{subdir}.{module_name}"))
    #             await ctx.send(f"```md\n[{module_name}]( now unloaded.)```")
        
    # @kirakota.command()
    # async def reload(ctx):
    #     await ctx.send("```md\n[Extensions]( are now reloading.)```")
    #     for subdir in os.listdir("cog_extensions"):
    #         for module in os.listdir(os.path.join("cog_extensions/"+subdir)):           
    #             if not module.endswith('.py') or module == '__pycache__':
    #                 continue
    #             module_name = module[:-3]
    #             try:
    #                 await kirakota.reload_extension(os.path.join(f"cog_extensions.{subdir}.{module_name}"))
    #                 await ctx.send(f"```md\n[{module_name}]( now reloaded.)```")
    #             except Exception as e:
    #                 print(f"Error occurred while reloading {module_name}: {e}")
    #                 await ctx.send(f"```md\n[Error]( occurred while reloading )[{module_name}:]( {e})```")



    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# old way
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import os
import discord 
from discord.ext import commands
import settings
from settings import*

logger = settings.logging.getLogger("kirakota")



def run():
    intents = discord.Intents.all()
    kirakota = commands.Bot(command_prefix="!", intents=intents)
    # dataName=()
    # def createEmbed(self, data):
    #     embed = discord.Embed(title=f"{dataName}")
    #     for item in data:
    #         embed.add_field(name=item['label'], value=item[''], inline=False)
    #     return embed



    # async def dataLoad():
    #     for subdir in os.listdir("cog_extensions"):
    #         for module in os.listdir(os.path.join("cog_extensions/"+subdir)):           
    #             if not module.endswith('.py') or module == '__pycache__':
    #                 continue
    #             module_name = module[:-3]
    #             extensionData = (os.path.join(f"cog_extensions.{subdir}.{module_name}"))
    #             for each in extensionData:
    #                 embed = discord.Embed(title=f"{dataName}")
    #                 embed.add_field(name=each.qualified_name, value=each.qualified_value, inline=True)
    #                 print (extensionData.qualified_name)




    @kirakota.event 
    async def on_ready():
        logger.info(f"User: {kirakota.user} (ID: {kirakota.user.id})")
        print(f"Guild Intents: {kirakota.intents.guilds}")
        print(f"Message Intents: {kirakota.intents.messages}")    
        print(f"User: {kirakota.user} (ID: {kirakota.user.id})")
        #for each sub directory in>> directory folder name
        for subdir in os.listdir("cog_extensions"):
            # then for each cmd/cog module in>> directory subdirectories
            for module in os.listdir(os.path.join("cog_extensions/"+subdir)):
                #cog extensions path will ==>> extension folder/subdir data   
                cog_extensions_path = os.path.abspath(f"cog_extensions/{subdir}")
                #then prints the cog extensions path `E:\!python\Bot Python Template\cog_extensions\cogs`
                print(cog_extensions_path)  
                #if the module doesn't end w/ .py or it doesn't equal __pycache__, it will continue      
                if not module.endswith('.py') or module == '__pycache__':
                    continue   
                #rename module(file) to module_name and remove the last 3 characters aka ".py"
                module_name = module[:-3]
                #then you want to load unload or reload the extensions. 
                #this takes the raw data. `(os.path.join(f"cog_extensions.{subdir}.{module_name}"))`
                #
                await kirakota.load_extension(os.path.join(f"cog_extensions.{subdir}.{module_name}"))
                print(f"\n[{module_name}]( now loaded.)")


    @kirakota.command()
    async def load(ctx):
        await ctx.send("```md\n[Extensions]( are now loading.)```")
        for subdir in os.listdir("cog_extensions"):
            for module in os.listdir(os.path.join("cog_extensions/"+subdir)):           
                if not module.endswith('.py') or module == '__pycache__':
                    continue
                module_name = module[:-3]
                await kirakota.load_extension(os.path.join(f"cog_extensions.{subdir}.{module_name}"))
                await ctx.send(f"```md\n[{module_name}]( now loaded.)```")
        
    @kirakota.command()
    async def unload(ctx):
        await ctx.send("`md\n[Extensions]( are now unloading.)`")
        for subdir in os.listdir("cog_extensions"):
            for module in os.listdir(os.path.join("cog_extensions/"+subdir)):           
                if not module.endswith('.py') or module == '__pycache__':
                    continue
                module_name = module[:-3]
                await kirakota.unload_extension(os.path.join(f"cog_extensions.{subdir}.{module_name}"))
                await ctx.send(f"```md\n[{module_name}]( now unloaded.)```")
        
    @kirakota.command()
    async def reload(ctx):
        await ctx.send("```md\n[Extensions]( are now reloading.)```")
        for subdir in os.listdir("cog_extensions"):
            for module in os.listdir(os.path.join("cog_extensions/"+subdir)):           
                if not module.endswith('.py') or module == '__pycache__':
                    continue
                module_name = module[:-3]
                try:
                    await kirakota.reload_extension(os.path.join(f"cog_extensions.{subdir}.{module_name}"))
                    await ctx.send(f"```md\n[{module_name}]( now reloaded.)```")
                except Exception as e:
                    print(f"Error occurred while reloading {module_name}: {e}")
                    await ctx.send(f"```md\n[Error]( occurred while reloading )[{module_name}:]( {e})```")

    kirakota.run(settings.DISCORD_API_SECRET, root_logger=True)
run()




























    
# # # # # # # # # # # # # # # # # # # # 
# # On Ready Script to read cmds and cogs folder.
#import os
# import settings
# import discord
# from discord.ext import commands
# logger = settings.logging.getLogger("kirakota")

# def run():
#     intents = discord.Intents.all()
#     kirakota = discord.Client(intents=intents)
#     kirakota = commands.Bot(command_prefix="!", intents=intents)
#     logger.info(f"User: {bot.user} (ID: {bot.user.id})")

#     # Print the value of "id" to see what is being passed as the argument
#     print(id)
#     try:
#         # Try to get the guild with the specified ID
#         guilds = kirakota.get_guild(id)
#     except Exception as e:
#         # If an exception is raised, print the exception message
#         print(e)

#     @kirakota.event()
#     async def on_ready():
#         logger.info(f"User: {kirakota.user} (ID: {kirakota.user.id})")
#         print(guilds)

#         for cog_file in settings.COGS_DIR.glob("*.py"):
#             if cog_file != "__init__.py":
#                 await kirakota.load_extension(f"cogs.{cog_file.name[:-3:]}")

#         for cmd_file in settings.CMDS_DIR.glob("*.py"):
#             if cmd_file.name != "__init__.py":
#                 await kirakota.load_extension(f"cmds.{cmd_file.name[:-3]}")
#     @kirakota.command()
#     async def load(ctx, extension):
#         await kirakota
#     @kirakota.command()
#     async def load(ctx, extension):
#         await kirakota.load_extension(f'cogs.{extension}')
#         await ctx.send(f'{extension} loaded.')

#     @kirakota.command()
#     async def unload(ctx, extension):
#         await kirakota.unload_extension(f'cogs.{extension}')
#         await ctx.send(f'{extension} unloaded.')

#     @kirakota.command()
#     async def reload(ctx, extension):
#         await kirakota.reload_extension(f'cogs.{extension}')
#         await ctx.send(f'{extension} reloaded.')

#     async def load_extensions():
#         for filename in os.listdir("./cogs"):
#             if filename.endswith(".py"):
#                 # cut off the .py from the file name
#                 await kirakota.load_extension(f"cogs.{filename[:-3]}")

#     kirakota.run(settings.DISCORD_API_SECRET, root_logger=True)
# if __name__ == "__main__":
#     run()
# # # # # # # # # # # # # # # # # # # #     