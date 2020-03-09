from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from progress.bar import ChargingBar
import tweepy
import pickle
import os
from datetime import datetime
from pathlib import Path

from .twitter import *
from .operation import *

TIMELINE_FILE = 'timeline.pkl'
KEY_FILE = 'key.pkl'
CREDS_FILE = 'credentials.pkl'
G_DRIVE_NAME = 'gd_creds'

ROOT_FOLDER = Path(__file__).resolve().parent
KEY_PATH = Path.joinpath(ROOT_FOLDER, KEY_FILE)
CREDS_PATH = Path.joinpath(ROOT_FOLDER, CREDS_FILE)
TIMELINE_PATH = Path.joinpath(ROOT_FOLDER, TIMELINE_FILE)

def pickle_dump(x, name):
  with open(name, 'wb') as f:
    pickle.dump([status._json for status in x], f)

def save_key(key):
  with open(KEY_PATH, 'wb') as f:
    pickle.dump(key, f)

def load_key():
  try:
    with open(KEY_PATH, 'rb') as f:
      return pickle.load(f)
  except FileNotFoundError:
    return {}

def save_credentials(key, path):
  creds = load_credentials()
  creds[key] = Path(path)
  with open(CREDS_PATH, 'wb') as f:
    pickle.dump(creds, f)
  return creds

def load_credentials():
  try:
    with open(CREDS_PATH, 'rb') as f:
      return pickle.load(f)
  except FileNotFoundError:
    return {}

def remove_access_token():
  try:
    with open(KEY_PATH, 'rb') as f:
      key = pickle.load(f)
    del key['access_token']
    del key['access_secret']
    del key['name']
    del key['id']
    del key['error']
    with open(KEY_PATH, 'wb') as f:
      pickle.dump(key, f)
    return True
  except FileNotFoundError:
    return False

def check_key(obj, key):
  try:
    if obj[key]:
      return True
  except KeyError:
    return False

class Tweeper:
  def __init__(self):
    self.files = {
      'timeline': TIMELINE_FILE
    }
    self.authorize = False
    self.twitter_auth = TwitterAuth()
  
  def logout(self):
    if remove_access_token():
      self.authorize = False

  def initialize_api(self):
    key = load_key()
    if check_key(key, 'consumer_key') and check_key(key, 'consumer_secret'):
      self.twitter_auth.set_comsumer_keys(key['consumer_key'], key['consumer_secret'])
      if not(check_key(key, 'access_token') or check_key(key, 'access_secret')): # Already has keys
        key = self.twitter_auth.auth()
      if not key['error']:
        save_key(key)
        auth = tweepy.OAuthHandler(key['consumer_key'], key['consumer_secret'])
        auth.set_access_token(key['access_token'], key['access_secret'])
        self.api = tweepy.API(auth, wait_on_rate_limit=True)
        self.authorize = True
    else:
      print("Unauthorize please set consumer keys by run 'pytweeper init'")
  
  def set_file(self, name, file):
    self.files[name] = file
  
  def get_me(self):
    return self.api.me()
  
  def get_home_timeline(self, end_page=1):
    timeline = []
    bar = ChargingBar('Crawling', max=end_page)
    for page in range(1, end_page+1):
      timeline += self.api.home_timeline(page=page, count=200)
      pickle_dump(timeline, self.files['timeline'])
      bar.next()
    bar.finish()
    return timeline
