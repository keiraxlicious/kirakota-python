import discord
from discord.ext import commands
import random
apexMapNames = ["Kings Canyon", "Worlds Edge",
                "Olympus", "Storm Point", "Broken Moon", ]
apexKCDropSpots = ["Skull Town", "Artillery", ]
apexWEDropSpots = ["Sky Hook", "Sorting Factory", ]
apexOlympusDropSpots = ["Spot 1", "Spot 2", ]
apexSPDropSpots = ["Spot 1", "Spot 2", ]
apexBMDropSpots = ["Spot 1", "Spot 2", ]
apexCccChannelID = 1
apexFriendsChannelID = 2
apexRoom = ""
temporary_category = 123
setTempCategoryID = {}
# Apex Spots
for value in apexMapNames:
    if value == "Kings Canyon":
        print(f"KC: {random.choice(apexKCDropSpots)}")
    elif value == "Worlds Edge":
        print(f"WE: {random.choice(apexWEDropSpots)}")
    elif value == "Olympus":
        print(f"Olympus: {random.choice(apexOlympusDropSpots)}")
    elif value == "Storm Point":
        print(f"SP: {random.choice(apexSPDropSpots)}")
    elif value == "Broken Moon":
        print(f"BM: {random.choice(apexBMDropSpots)}")


class TemporaryVoice(commands.Cog):
    def __init__(self, kirakota):
        self.kirakota = kirakota

    async def createTempVC(self, member, after):
        if after.channel:
            if after.channel.id == apexFriendsChannelID:
                setTempChannel = await after.channel.clone(name=apexRoom)
                channelTemp = setTempChannel
                await member.move_to(channelTemp)
                self.temporary_channels.append(channelTemp.id)

    async def createTempVCnTextChannel(self, member, after, temporary_category):
        if after.channel.id == apexCccChannelID:
            await temporary_category.create_text_channel(name=f"{apexRoom} Chat")
            temp_VC = await temporary_category.create_voice_channel(name=f"{apexRoom}")
            VcTemp = temp_VC
            await member.move_to(VcTemp)
            self.temporary_channels.append(VcTemp.id)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        temporary_category = setTempCategoryID
        await self.createTempVCnTextChannel(member, after, temporary_category)
        await self.createTempVC(member, after)


async def setup(kirakota):
    await kirakota.add_cog(TemporaryVoice(kirakota))

# #####################
#     @commands.Cog.listener()
#     async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState)    :
#         if after.channel:
#             if after.channel.name == "temp": #"temp" is the name of the channel made.
#                 temp_channel = await after.channel.clone(name=apexTempRoom)
#                 await member.move_to(temp_channel)
#                 self.temporary_channels.append(temp_channel.id)

#                 # Check if the user moved to the '➕ Streaming' channel via .id instead of .name
#             if after.channel.id == apexFriendsChannelID or apexCccChannelID  : #'➕Apex🔴🟢':
#                  # Create a text channel and a voice channel for the stream
#                 temporary_category = setTempCategoryID
#                  # Move the user to the voice channel
#                 await temporary_category.create_text_channel(name=f"{stream_channel_name} Chat")
#                 # Add the voice channel to the list of temporary channels
#                 temp_channel = await temporary_category.create_voice_channel(name=f"{stream_channel_name}")
#                 # Move the user to the voice channel
#                 await member.move_to(temp_channel)
#                 # Add the voice channel to the list of temporary channels
#                 self.temporary_categories.append(temp_channel.id)


#     @commands.Cog.listener()
#     async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState)    :
#         if after.channel:
#             if after.channel.name == "temp": #"temp" is the name of the channel made.
#                 temp_channel = await after.channel.clone(name=apexTempRoom)
#                 await member.move_to(temp_channel)
#                 self.temporary_channels.append(temp_channel.id)


#             if after.channel.id == apexFriendsChannelID or apexCccChannelID  : #'➕Apex🔴 or ➕Apex🟢':
#                 temporary_category = setTempCategoryID
#                 await temporary_category.create_text_channel(name=f"{apexTempRoom} Chat")
#                 temp_channel = await temporary_category.create_voice_channel(name=f"{apexTempRoom}")
#                 await member.move_to(temp_channel)
#                 self.temporary_categories.append(temp_channel.id)

#             """
#             asdkjaskdjnakjnsd
#             """

#     async def createTempChannel(self, member, after):
#         if after.channel:
#             if after.channel.name == "temp":
#                 temp_channel = await after.channel.clone(name=apexTempRoom)
#                 await member.move_to(temp_channel)
#                 self.temporary_channels.append(temp_channel.id)

#     @commands.Cog.listener()
#     async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
#         await self.createTempChannel(member, after)


#             async def createTempChannel(self, member, after, temporary_category):
#         if after.channel.id == apexFriendsChannelID or apexCccChannelID:
#             await temporary_category.create_text_channel(name=f"{apexTempRoom} Chat")
#             temp_channel = await temporary_category.create_voice_channel(name=f"{apexTempRoom}")
#             await member.move_to(temp_channel)
#             self.temporary_channels.append(temp_channel.id)

#     @commands.Cog.listener()
#     async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
#         temporary_category = setTempCategoryID
#         await self.createTempChannel(member, after, temporary_category)
