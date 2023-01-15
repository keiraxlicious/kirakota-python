# import os
# import discord 
# from discord.ext import commands
# import settings
# from settings import*
# import importlib
# import asyncio

# logger = settings.logging.getLogger("kirakota")
# loaded_cogs = []

# class ExtensionHandler:
#     def __init__(self, bot):
#         self.bot = bot

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # | | | - - - !loadall
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#     async def load_all_extensions(self, ctx):
#         loaded_cogs = []
#         success_embed = discord.Embed(title='Success', color=discord.Color.green())
#         fail_embed = discord.Embed(title='Failed', color=discord.Color.red())

#         # Iterate over the extension names and try to load them
#         for extension in os.listdir("cog_extensions"):
#             extension_name = extension.split('.')[-1]  # Get the extension name from the extension path
#             try:
#                 await self.bot.load_extension(f"cog_extensions.{extension_name}")
#                 cog = self.bot.get_cog(extension_name)  # Get the cog object
#                 success_embed.add_field(name=extension_name, value=cog.__cog_name__, inline=False)
#                 await loaded_cogs.append(cog.__qualified_name__) 
#             except Exception as e:
#                 fail_embed.add_field(name=extension_name, value=f'Error: {e}', inline=False)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # | | | - - - !unloadall
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#     async def unload_all_extensions(self, ctx):
#         loaded_cogs = []
#         success_embed = discord.Embed(title='Success', color=discord.Color.green())
#         fail_embed = discord.Embed(title='Failed', color=discord.Color.red())

#         # Iterate over the extension names and try to load them
#         for extension in os.listdir("cog_extensions"):
#             extension_name = extension.split('.')[-1]  # Get the extension name from the extension path
#             try:
#                 await self.bot.unload_extension(f"cog_extensions.{extension_name}")
#                 cog = self.bot.get_cog(extension_name)  # Get the cog object
#                 success_embed.add_field(name=extension_name, value=cog.__cog_name__, inline=False)
#                 await loaded_cogs.remove(cog.__qualified_name__) 
#             except Exception as e:
#                 fail_embed.add_field(name=extension_name, value=f'Error: {e}', inline=False)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # | | | - - - !reloadall
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#     async def reload_all_extensions(self, ctx):
#         loaded_cogs = []
#         success_embed = discord.Embed(title='Success', color=discord.Color.green())
#         fail_embed = discord.Embed(title='Failed', color=discord.Color.red())

#         # Iterate over the extension names and try to load them
#         for extension in os.listdir("cog_extensions"):
#             extension_name = extension.split('.')[-1]  # Get the extension name from the extension path
#             try:
#                 await self.bot.reload_extension(f"cog_extensions.{extension_name}")
#                 cog = self.bot.get_cog(extension_name)  # Get the cog object
#                 success_embed.add_field(name=extension_name, value=cog.__cog_name__, inline=False)
#                 await loaded_cogs.append(cog.__qualified_name__) 
#             except Exception as e:
#                 fail_embed.add_field(name=extension_name, value=f'Error: {e}', inline=False)

#         # Send the success and fail embeds
#         if success_embed.fields:
#             await ctx.send(embed=success_embed)
#         if fail_embed.fields:
#             await ctx.send(embed=fail_embed)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # | | | - - - !reload (ext)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#     async def reload_extension(self, ctx, extension_name):
#         loaded_cogs = []
#         success_embed = discord.Embed(title='Success', color=discord.Color.green())
#         fail_embed = discord.Embed(title='Failed', color=discord.Color.red())

#         # Reload the extension and get the cog object
#         try:
#             await self.bot.reload_extension(f"cog_extensions.{extension_name}")
#             cog = self.bot.get_cog(extension_name)
#             success_embed.add_field(name=extension_name, value=cog.__cog_name__, inline=False)
#             await loaded_cogs.append(cog.__qualified_name__) 
#         except Exception as e:
#             fail_embed.add_field(name=extension_name, value=f'Error: {e}', inline=False)

#         # Send the success and fail embeds
#         if success_embed.fields:
#             await ctx.send(embed=success_embed)
#         if fail_embed.fields:
#             await ctx.send(embed=fail_embed)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # | | | - - - !load (ext)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#     async def load_extension(self, ctx, extension_name):
#         loaded_cogs = []
#         success_embed = discord.Embed(title='Success', color=discord.Color.green())
#         fail_embed = discord.Embed(title='Failed', color=discord.Color.red())

#         # Reload the extension and get the cog object
#         try:
#             await self.bot.load_extension(f"cog_extensions.{extension_name}")
#             cog = self.bot.get_cog(extension_name)
#             success_embed.add_field(name=extension_name, value=cog.__cog_name__, inline=False)
#             await loaded_cogs.append(cog.__qualified_name__) 
#         except Exception as e:
#             fail_embed.add_field(name=extension_name, value=f'Error: {e}', inline=False)

#         # Send the success and fail embeds
#         if success_embed.fields:
#             await ctx.send(embed=success_embed)
#         if fail_embed.fields:
#             await ctx.send(embed=fail_embed)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # | | | - - - !unload (ext)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#     async def unload_extension(self, ctx, extension_name):
#         loaded_cogs = []
#         success_embed = discord.Embed(title='Success', color=discord.Color.green())
#         fail_embed = discord.Embed(title='Failed', color=discord.Color.red())

#         # Reload the extension and get the cog object
#         try:
#             await self.bot.unload_extension(f"cog_extensions.{extension_name}")
#             cog = self.bot.get_cog(extension_name)
#             success_embed.add_field(name=extension_name, value=cog.__cog_name__, inline=False)
#             await loaded_cogs.remove(cog.__qualified_name__) 

#         except Exception as e:
#             fail_embed.add_field(name=extension_name, value=f'Error: {e}', inline=False)

#         # Send the success and fail embeds
#         if success_embed.fields:
#             await ctx.send(embed=success_embed)
#         if fail_embed.fields:
#             await ctx.send(embed=fail_embed)


# # logger = settings.logging.getLogger("kirakota"){cog_extensions_path}.{module_name}"))
# class launchExtensions:
#     def __init__(self):
#         self.extension = "cog_extensions"

#     async def extensions(self, kirakota):
#         loaded_cogs = []
#         for subdir in os.listdir(self.extension):
#             for module in os.listdir(os.path.join(self.extension + "/" + subdir)):
#                 cog_extensions_path = os.path.abspath(f"{self.extension}/{subdir}")    
#                 if not module.endswith('.py') or module == '__pycache__':
#                     continue   
#                 module_name = module[:-3]
#                 extensionName =(os.path.join(f"{self.extension}.{subdir}.{module_name}"))
#                 imported_module = importlib.import_module(extensionName)
#                 try:
#                     setup_func = getattr(imported_module, "setup")
#                     module = setup_func(kirakota)
#                     await module.setup(kirakota)
#                 except AttributeError:
#                     print(f"{module_name} has no 'setup' function.")
#                 kirakota.load_extension(extensionName)
#                 loaded_cogs.append(extensionName)
#         for qualified_name in loaded_cogs:
#             print(f"Loaded extension {qualified_name}")

# # class launchExtensions:
# #     def __init__(self):
# #         self.extension = "cog_extensions"
# #     async def extensions(self, kirakota):
# #         loaded_cogs = []
# #         for subdir in os.listdir(self.extension):
# #                 for module in os.listdir(os.path.join(self.extension + "/" + subdir)):
# #                     cog_extensions_path = os.path.abspath(f"{self.extension}/{subdir}") 
# #                     # if any(f.endswith(".py") for f in os.listdir(os.path.join(self.extension, subdir))):   
# #                     if not module.endswith('.py') or module == '__pycache__':
# #                         continue   
# #                     module_name = module[:-3]
# #                     extensionName =(os.path.join(f"{cog_extensions_path}.{module_name}"))
# #                     # extensionName =(os.path.join(f"{self.extension}.{subdir}.{module_name}"))
# #                     imported_module = importlib.import_module(extensionName)
# #                     try:
# #                         setup_func = getattr(imported_module, "setup")
# #                         module = setup_func(kirakota)
# #                         await module.setup(kirakota)
# #                     except AttributeError:
# #                         print(f"{module_name} has no 'setup' function.")
# #                     await kirakota.load_extension(extensionName)
# #                     loaded_cogs.append(extensionName)
# #         for qualified_name in loaded_cogs:
# #             print(f"Loaded extension {qualified_name}")

#     # for subdir in os.listdir(self.extension):
#             # Process subdir as a cog
#         # else:
#             # Skip subdir

# # async def extensions(self, kirakota):
# #     loaded_cogs = []
# #     for subdir in os.listdir(self.extension):
# #         for module in os.listdir(os.path.join(self.extension + "/" + subdir)):
# #             cog_extensions_path = os.path.abspath(f"{self.extension}/{subdir}")    
# #             if not module.endswith('.py') or module == '__pycache__':
# #                 continue   
# #             module_name = module[:-3]
# #             extensionName =(os.path.join(f"{self.extension}.{subdir}.{module_name}"))
# #             imported_module = importlib.import_module(extensionName)
# #             # Check if the module is a directory or a file
# #             if not os.path.isfile(os.path.join(cog_extensions_path, module)):
# #                 # If it is a directory, skip it
# #                 continue
# #             # If the module has a setup function, call it
# #             if hasattr(imported_module, "setup"):
# #                 setup_func = getattr(imported_module, "setup")
# #                 module = setup_func(kirakota)
# #                 if asyncio.iscoroutine(module.setup):
# #                     await module.setup(kirakota)
# # class launchExtensions:
# #     def __init__(self):
# #         self.extension = "cog_extensions"

# #     async def extensions(self, kirakota):
# #         loaded_cogs = []
# #         for subdir in os.listdir(self.extension):
# #             for module in os.listdir(os.path.join(self.extension + "/" + subdir)):
# #                 cog_extensions_path = os.path.abspath(f"{self.extension}/{subdir}")    
# #                 if not module.endswith('.py') or module == '__pycache__':
# #                     continue   
# #                 module_name = module[:-3]
# #                 extensionName =(os.path.join(f"{self.extension}.{subdir}.{module_name}"))
# #                 imported_module = importlib.import_module(extensionName)
# #                 if hasattr(imported_module, "setup"):
# #                     setup_func = getattr(imported_module, "setup")
# #                     module = setup_func(kirakota)
# #                     if asyncio.iscoroutine(module.setup):
# #                         await module.setup(kirakota)
# #                 else:
# #                     print(f"{module_name} has no 'setup' function.")
# #                 kirakota.load_extension(extensionName)
# #                 loaded_cogs.append(extensionName)
# #         for qualified_name in loaded_cogs:
# #             print(f"Loaded extension {qualified_name}")

#     # async def extensions(self, kirakota):
#     #     loaded_cogs = []
#     #     for subdir in os.listdir(self.extension):
#     #         for module in os.listdir(os.path.join(self.extension + "/" + subdir)):
#     #             cog_extensions_path = os.path.abspath(f"{self.extension}/{subdir}")    
#     #             if not module.endswith('.py') or module == '__pycache__':
#     #                 continue   
#     #             module_name = module[:-3]
#     #             extensionName =(os.path.join(f"{self.extension}.{subdir}.{module_name}"))
#     #             imported_module = importlib.import_module(extensionName)
#     #             if hasattr(imported_module, "setup"):
#     #                 setup_func = getattr(imported_module, "setup")
#     #                 module = setup_func(kirakota)
#     #                 if asyncio.iscoroutine(module.setup):
#     #                     await module.setup(kirakota)
#     #                 else:
#     #                     module.setup(kirakota)
#     #             else:
#     #                 print(f"{module_name} has no 'setup' function.")
#     #             kirakota.load_extension(extensionName)
#     #             loaded_cogs.append(extensionName)
#     #     for qualified_name in loaded_cogs:
#     #         print(f"Loaded extension {qualified_name}")

#     # async def extensions(self, kirakota):
#     #     for subdir in os.listdir(self.extension):
#     #         for module in os.listdir(os.path.join(self.extension + "/" + subdir)):
#     #             cog_extensions_path = os.path.abspath(f"{self.extension}/{subdir}")    
#     #             if not module.endswith('.py') or module == '__pycache__':
#     #                 continue   
#     #             module_name = module[:-3]
#     #         extensionName =(os.path.join(f"{self.extension}.{subdir}.{module_name}"))
#     #         imported_module = importlib.import_module(extensionName)
#     #         module = imported_module(f"{cog_extensions_path}.{module_name}")
#     #         if hasattr(module, "setup"):
#     #             module.setup(kirakota)
#     #         print(imported_module)
#     #         setup_func = getattr(imported_module, "setup", None)
#     #         if setup_func is not None:
#     #             setup_func()
#     #         else:
#     #             print(f"{module_name} has no 'setup' function.")
#     #         for extension in extensionName:
#     #             self.bot.load_extension(extension)
#     #             print(f"{extensionName} Loaded")