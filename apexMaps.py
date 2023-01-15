import discord
from discord.ext import commands


class ActivityUpdate(commands.Cog):
    def __init__(self, kirakota):
        self.kirakota = kirakota
        self.activity_listening = False
        self.game_activity_map = {
        'VALORANT': 'Valorant',
        'APEX LEGENDS': 'Apex Legends',
        # add more game activities as needed
        }
        self.status_color_map = {
            'online': discord.Colour.green(),
            'offline': discord.Colour.dark_grey(),
            'dnd': discord.Colour.red(),
            'idle': discord.Colour.gold(),
            'streaming': discord.Colour.dark_purple(),
        }

    @commands.command()
    async def toggle_activity_listener(self, ctx):
        self.activity_listening = not self.activity_listening
        if self.activity_listening:
            await ctx.send("Activity update listener enabled.")
        else:
            await ctx.send("Activity update listener disabled.")
        
    @commands.Cog.listener()        
    async def on_presence_update(self, before, after):
        if self.activity_listening:
            color = self.status_color_map.get(after.status.name, discord.Colour.default())
            tellKeira = self.kirakota.get_user(317545559437344768)
            try:
                print(f'{after.activity} {after.activity.type} {discord.ActivityType.playing}')#debug
            except Exception as e:
                print(f'Error sending DM: {e}')
            if after.activity and after.activity.type == discord.ActivityType.playing:
                try:
                    activity_name = after.activity.name
                    if activity_name in self.game_activity_map:
                        activity_name = self.game_activity_map[activity_name]
                        # avatar = after.activity.assets.large_image.url
                        avatar = after.avatar
                        embed = discord.Embed(title='Activity Update', color=color)
                        embed.set_author(name=before.name, icon_url=after.avatar)
                        embed.set_thumbnail(url=avatar)
                        embed.add_field(name='Member Name', value=f'*{before.name}#{before.discriminator}*', inline=False)
                        embed.add_field(name='Old Activity', value=f'~~{before.activity}~~', inline=True)
                        embed.add_field(name='New Activity', value=activity_name, inline=True)
                        try:
                            await tellKeira.send(embed=embed)
                        except Exception as e:
                            print(f'Error sending DM: {e}')
                    else:
                        embed = discord.Embed(title='Activity Update', color=color)
                        embed.set_author(name=before.name, icon_url=after.avatar)
                        embed.add_field(name='Member Name', value=f'{before.name}#{before.discriminator}', inline=False)
                        embed.add_field(name='Old Activity', value=f'{before.activity}', inline=True)
                        embed.add_field(name='New Activity', value=activity_name, inline=True)
                        try:
                            await tellKeira.send(embed=embed)
                        except Exception as e:
                            print(f'Error sending DM: {e}')
                except Exception as e:
                    print(f'Error sending DM: {e}')
            else:
                    # if activity is not playing, do something else
                pass
        else:
                # if activity is not playing, do something else
            pass
    #         if before.activity != after.activity or before.status != after.status:
    #             if after.activity != None:
    #                 color = self.status_color_map.get(after.status.name, discord.Colour.default())
    #                 user = self.kirakota.get_user(317545559437344768)
    #                 if after.activity:
    #                     if after.activity.type == discord.ActivityType.streaming:
    #                         embed = discord.Embed(title='Stream Alert Update', color=color)
    #                         avatar = after.avatar
    #                         embed.set_thumbnail(url=avatar)
    #                         embed.set_author(name=after.name, icon_url=after.avatar)
    #                         embed.add_field(name='Member Name', value=f'*{before.name}#{before.discriminator}*', inline=True)
    #                         embed.add_field(name='Old Activity', value=f'~~~{before.activity}~~~', inline=True)
    #                         embed.add_field(name='New Activity', value=after.activity, inline=True)
    #                         try:
    #                             await user.send(embed=embed)
    #                         except Exception as e:
    #                             print(f'Error sending DM: {e}')
    #                     else:
    #                         color = discord.Colour.purple() 



    #             if before.activity != after.activity:
    #                 if after.activity:
    #                     # application = await after.activity.large_image_url
    #                     avatar = after.activity.large_image_url
    #                 else:
    #                     avatar = after.avatar
    #                 embed = discord.Embed(title='Activity Update', color=color)
    #                 # avatar = after.avatar
    #                 embed.set_thumbnail(url=avatar)
    #                 embed.set_author(name=before.name, icon_url=after.avatar)
    #                 embed.add_field(name='Member Name', value=f'*{before.name}#{before.discriminator}*', inline=False)
    #                 embed.add_field(name='Old Activity', value=f'~~~{before.activity}~~~', inline=True)
    #                 activity_name = before.activity.name if before.activity else None
    #                 if activity_name == "VALORANT":
    #                     activity_name = "Valorant"
    #                     embed.add_f