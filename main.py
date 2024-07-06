import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!krak_", intents = intents)

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")
    guilds = client.guilds
    channel = discord.utils.get(guilds[0].text_channels, name="krakounet")
    
    if channel is None:
        channel = discord.utils.get(guilds[1].text_channels, name="krakounet")
    
    await channel.send("Hardi moussaillons, vla le Krakounet. !krak_command to activate me")
    
    channel = discord.utils.get(guilds[0].text_channels, name="shitpost")
    
    if channel is None:
        channel = discord.utils.get(guilds[1].text_channels, name="shitpost")
    
    await channel.send("Hardi moussaillons, vla le Krakounet. !krak_command to activate me")
    
@client.command()
async def fdp(ctx):
    await ctx.send("Vous êtes tous des fils de putes")

@client.command()    
async def server(ctx, server_name):
    channel = discord.utils.get(ctx.guild.channels, name = server_name)
    if channel is not None:
        await channel.send("J'ai trouver ton canal grosse merde")
    
client.run("MTI1ODkzMTM5ODcyNzk2MjcwNA.GdGBq8.3yIuA9eSttifwjlzNjVWAbRjfsgCsTmqOBrF7A")
