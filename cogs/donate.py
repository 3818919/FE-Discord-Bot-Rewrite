import disnake
from disnake.ext import commands
import config
import time

######################
### DONATE COMMAND ###

class bcolours:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

class info:
  donate, thanks = config.donate()
  name, alias, game_client = config.Game()

class donate(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  bot = config.dbot()  
  @bot.slash_command(description=f"A way to help support {info.name} and further client development.")
  async def donate(inter):
    donate = disnake.Embed(title = f'Become An {info.alias} Supporter', url=info.donate, description = info.thanks, colour = disnake.Colour.green())
    donate.set_thumbnail(url="https://fallen-evolution.com/giftcash.png")
    await inter.response.send_message(embed=donate)
    time.sleep(2)


def setup(bot):
  bot.add_cog(donate(bot))
  print (bcolours.GREEN + 'Donate Command Loaded')