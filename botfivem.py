import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.command()
async def warn1(ctx, member:discord.Member, *, reason="Brak powodu"):
    await ctx.send(f" {member} Zostal zwarnowany za {reason} przez")

  

bot.run('NTUzNjM2MTgwMjMxNDU0NzM0.D2UcpA.gxmeSinTNGQhR2cUTMoDgLaHhyI')    

