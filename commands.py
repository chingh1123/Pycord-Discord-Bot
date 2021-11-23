import discord

from discord.ext import commands

bot = commands.Bot(command_prefix=">")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

from config import token
bot.run(token)
