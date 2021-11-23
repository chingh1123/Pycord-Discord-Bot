import discord
import os

from discord.ext import commands

bot = commands.Bot(command_prefix=">")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

print('Bot is ready and it is online!')
bot.run(os.environ['token']) #or you can just write `bot.run('YOUR TOKEN HERE')`
