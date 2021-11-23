import discord

from discord.ui import Button, View

from discord.ext import commands

bot = commands.Bot(command_prefix=">")

@bot.command()
async def ping(ctx):
    button = Button(label='CLick me!', style=discord.ButtonStyle.primary, emoji='😁')
    # more button style view here: https://docs.pycord.dev/en/master/api.html?highlight=buttonstyle#discord.ButtonStyle
    # button emoji can be put emoji id too
    view = View()
    view.add_item(button)
    await ctx.send("Here is the button", view=view)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

from config import token
bot.run(token)
