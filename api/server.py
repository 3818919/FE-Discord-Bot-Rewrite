import config
from api import api
import socket
import disnake

###################
### PING SERVER ###

class server:
  ip, port, retry, timeout = config.Server()

class info:
  name, alias, game_client = config.Game()

#Ping game server
def ping():
  def isOpen(ip, port):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(server.timeout)
      try:
          s.connect((ip, int(port)))
          s.shutdown(socket.SHUT_RDWR)
          return True
      except:
          return False
      finally:
          s.close()

  def checkHost(ip, port):
      ipup = False
      for i in range(server.retry):
          if isOpen(ip, port):
              ipup = True
              break
          else:

              return
      return ipup
  if checkHost(server.ip, server.port):
    status = True
    return status
  else:
    status = False
    return status


#########################
### LOAD PLAYER COUNT ###

#Check Player Count of Game Server
def eo2():
  status = ping()
  if status == True:
    plist, pnum = api.players()
    if pnum ==1:
      game = disnake.Game(f'{info.alias} - {pnum} Player Online {plist}')
      return plist, pnum, game
    else:
      game = disnake.Game(f'{info.alias} - {pnum} Players Online {plist}')
      return plist, pnum, game
  else:
    game = disnake.Game('Nothing - Server Offline')
    return plist, pnum, game
    


