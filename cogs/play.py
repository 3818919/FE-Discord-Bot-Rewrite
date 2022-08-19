import disnake
from disnake.ext import commands
import config
from api import api, server
import time

####################
### PLAY COMMAND ###

class bcolours:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

class info:
  plist, pnum, game = server.eo2()
  name, alias, game_client = config.Game()

class play(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  bot = config.dbot()  
  @bot.slash_command(description=f"A quick way to download {info.alias}.")
  async def play(inter):
    download = disnake.Embed(title = f'Play {info.alias} Today!', url=info.game_client, description = f'Currently {info.pnum} players online!', colour = disnake.Colour.green())
    download.set_thumbnail(url="https://fallen-evolution.com/image33.png")
    await inter.response.send_message(embed=download)
    time.sleep(2)


def setup(bot):
  bot.add_cog(play(bot))
  print (bcolours.GREEN + 'Play Command Loaded')