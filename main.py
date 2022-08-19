import os
import config
from api import server, api
import asyncio
import disnake
from disnake.ext import tasks, commands

#########################
#### FE Discord Bot ####
#########################
### BOT > DISCORD API ###

class bcolours:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

#Debug channel for feature testing
class DEBUG:
  testchannel = config.DEBUG()

class info:
  name, alias, game_client = config.Game()
  
TOKEN = os.environ['TOKEN']
intents = disnake.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=disnake.ext.commands.when_mentioned, intents=intents)
bot.remove_command('help')
Server = ".:Fallen Evolution:."
print (bcolours.GREEN + Server)
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
  else:
    pass

###############################
#### END BOT > DISCORD API ####


#######################
### STATUS BOT TASK ###

class status:
  plist, pnum, game = server.eo2()

@tasks.loop(seconds=30)
async def status_swap(): 
  await bot.change_presence(status=disnake.Status.online, activity=status.game)
  await asyncio.sleep(2)

#########################
### AUTO MSG BOT TASK ###

class post:
  active = config.Advertising()
  ServerID, channel = config.Discord()
  advert = api.Adverts()

@tasks.loop(minutes=180)
async def send():
  await asyncio.sleep(200)
  channel = bot.get_channel(post.channel)
  
  try:
    if post.active == True:
      await channel.send(post.advert, delete_after = 1800)
      await asyncio.sleep(2)
      return
    else:
      print (bcolours.RED + 'Advertising is disabled')
      await asyncio.sleep(2)
  except:
    return

@send.before_loop
async def before():
    await bot.wait_until_ready()

################
### LOAD BOT ###

@bot.event
async def on_ready():
  if not status_swap.is_running():
    print('Status Updater Loaded')
    status_swap.start()
  if not send.is_running():
    print('Adverts Loaded')
    send.start()
  print(bcolours.YELLOW + 'I have logged in to the FE Discord as {0.user}'.format(bot))

#######################
### WELCOME MESSAGE ###

@bot.event
async def on_member_join(member):
  
  #Welcome Message General Chat
  channel = bot.get_channel(post.channel)
  welcome = config.Welcome(member)
  await channel.send(welcome)
  print (f'{member} has joined the discord [SENDING DM]..')

  #Welcome Message DM
  welcome = disnake.Embed(title = f'Welcome to the {info.alias} Discord', url= "https://discord.com/channels/192691686156140545/809355290545094686", description = f'If you need help recovering your account, check out the #support channel on the {info.alias} discord.', colour = disnake.Colour.green())
  welcome.add_field(name="New client now avaliable!", value=f"Client is still in beta and any feedback or bug reports are appreciated!\n\n Currently {status.pnum} players online!", inline=False)
  welcome.set_thumbnail(url="https://fallen-evolution.com/image33.png")
  await member.send(embed=welcome)
  await asyncio.sleep(2)

########################
### TRACK PLAYER MSG ###
  
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot:
        return
      
    await bot.process_commands(message)
    await asyncio.sleep(2)

#################
### START BOT ###

#TOKEN = config.TOKEN() #Uncomment to enable config.ini token functionality
bot.run(TOKEN)