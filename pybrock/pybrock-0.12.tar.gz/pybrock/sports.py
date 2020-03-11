import pandas as pd
import json
import requests

def nhl_games(season=201920):
  # build the url for Nice time on Ice API
  URL = 'http://www.nicetimeonice.com/api/seasons/{}/games'
  url = URL.format(season)
  # get the games
  games = requests.get(url).json()
  # put into a dataframe
  df = pd.DataFrame(games)
  df.columns = df.columns.str.lower()
  # return
  return(df)


