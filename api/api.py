import config
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
from api.advertising import settings
import numpy as np

################
### LOAD VARIABLES ###

class config:
  domain, ranks = config.API()
  ip, port, retry, timeout = config.Server()
  download = config.download()
  name, alias, game_client = config.Game()

class info:
  name = config.name
  alias = config.alias

################
### WEBSCRAPE FOR LEADER BOARDS ###
  
def topPlayers():
  topplayers = pd.read_html(config.ranks)[0]
  topplayers.index += 1
  Lists = topplayers.head(100)
  Players = Lists[0]
  Level = Lists[1]
  Names = Players.values
  Levels = Level.values
  return Names, Levels

###################################
### WEBSCRAPE FOR DOWNLOAD LINK ###
  
def download():
#  Scrapes website for download
#  download = config.download
#  req = Request(download, headers={'User-Agent': 'Mozilla/5.0'})
#  parser = 'lxml'  
#  resp = urllib.request.urlopen(req)
#  soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
#  for link in soup.find_all('a', href=True):
#    client = link['href']
#    if client.endswith('msi'):
  client = config.download()
  return client


##################################
### WEBSCRAPE FOR PLAYER COUNT ###

def players():
  try:
    Players = pd.read_html('https://eosource.net/characters.php?ip=game.fallen-evolution.com&port=8078')[0]
    Players.index += 1
    Lists = Players.head(100) #Only show x Items
    People = Lists.Name
    People = sorted(People)
    print (People)
    Names = People.values
    plist = '\n '.join(Names) #List of Players
    pnum = len(Names) #Count of players
    return plist, pnum
  except:
    Table = pd.read_html('http://www.apollo-games.com/SLN/sln.php/onlinelist?server=host:server1.fallen-evolution.com:8078')[0]
    Table.index += 1
    List2 = Table.head(100) #Only show x Items
    People_Names = List2.Name
    Names = People_Names.values
    plist = '\n '.join(Names) #List of Players
    pnum = len(Names) #Count of players
    return plist, pnum

####################
### LINK ADVERTS ###

def Adverts():
  advert = settings.Ads()
  return advert