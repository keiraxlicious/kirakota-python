from discord.ext import commands



@commands.group()
async def ping(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"No, {ctx.subcommand_passed} does not belong to simple")


@ping.command()
async def ping(ctx):
    await ctx.send("pong")


async def setup(kirakota):
    kirakota.add_command(ping)