import json
import itertools
import requests
import shutil
import os
import pickle
from progress.bar import ChargingBar
from pathlib import Path

from .drive import Drive

def read(file):
  with open(file, 'rb') as f:
    return pickle.load(f)

def make_dir(path):
  if not os.path.exists(path):
      os.makedirs(path)

def download_image(url, image_path):
  response = requests.get(url, stream=True)
  with open(image_path, 'wb+') as out_file:
      shutil.copyfileobj(response.raw, out_file)
  del response


def mapper(d):
  has_image = False
  has_extended_image = False
  image = list()
  extended_image = list()
  try:
    image = list(map(lambda x: x['media_url_https'], d['entities']['media']))
    has_image = True
    extended_image = list(map(lambda x: x['media_url_https'], d['extended_entities']['media']))
    has_extended_image = True
    return image+extended_image
  except KeyError:
    if has_image:
      return image
    else:
      return ''

def extract_data(file):
  data = read(file)
  mapped = list(map(mapper, data))
  merged = list(itertools.chain(*mapped))
  return merged

def list_files(path):
  onlyfiles = [f for f in Path.iterdir(path) if Path.is_file(Path.joinpath(path, f))]
  return onlyfiles

def read_and_download(file, path):
  merged = extract_data(file)

  make_dir(path)
  bar = ChargingBar('Downloading', max=len(merged))
  for i, image in enumerate(merged):
    download_image(image, os.path.join(path, image.split('/')[-1]))
    bar.next()
  bar.finish()

def read_and_upload(creds_path, source, folder_name=None):
  d = Drive(creds_path=creds_path)
  d.authenticate()
  if type(source) == str:
    source = Path(source)
  files = list_files(source)
  source_folder = source.parts[-1]

  # Select folder section
  if (folder_name):
    folder = d.check_folder_if_exist(folder_name)
    if folder:
      folder_id = d.create_folder(source_folder, folder).get('id')
      d.select_folder([folder_id])
    else:
      new_folder = d.create_folder(folder_name).get('id')
      folder_id = d.create_folder(source_folder, [new_folder]).get('id')
      d.select_folder([folder_id])
  else:
    folder_id = d.create_folder(source_folder).get('id')
    d.select_folder([folder_id])
  
  # Upload section
  bar = ChargingBar('Uploading', max=len(files))
  for f in files:
    file_name = f.parts[-1]
    upload = d.upload_file(f, file_name)
    bar.next()
  bar.finish()

if __name__ == '__main__':
  print('Operation file!')