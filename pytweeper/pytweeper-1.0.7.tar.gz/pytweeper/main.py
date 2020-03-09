from pathlib import Path
from .tweeper import *
from .operation import *

KEY_FILE = 'key.pkl'
APP_NAME = 'pytweeper'
G_DRIVE_NAME = 'gd_creds'

ROOT_FOLDER = Path(__file__).resolve().parent
KEY_PATH = Path.joinpath(ROOT_FOLDER, KEY_FILE)

def main():
  import argparse
  parser = argparse.ArgumentParser(description='PyTweeper (Twitter crawler)')
  parser.add_argument('command', nargs='?', help='command or mode')
  parser.add_argument('-p', type=int, help='page count for crawler')
  parser.add_argument('-o', type=str, help='output destination')
  parser.add_argument('--logout', action='store_true', help='output destination')
  parser.add_argument('--drive', action='store_true', help='Upload to Google Drive')
  parser.add_argument('--gd_creds', type=str, help='Path to Google Drive Credentials')

  today = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
  args = vars(parser.parse_args())
  command = args['command']
  page = args['p'] or 10
  output = Path.joinpath(Path(args['o'] or Path.cwd()).resolve(), APP_NAME, today)
  logout = args['logout']
  drive = args['drive']
  gd_creds = args['gd_creds']

  consumer_key = None
  consumer_secret = None
  gd_creds_path = None

  client = Tweeper()
  if logout:
    client.logout()
  elif command == 'init':
    consumer_key = input("Consumer key: ")
    consumer_secret = input("Consumer secret: ")
    with open(KEY_PATH, 'wb') as f:
      pickle.dump({ "consumer_key": consumer_key, "consumer_secret": consumer_secret }, f)
  else:
    if drive:
      if gd_creds:
        saved = save_credentials(G_DRIVE_NAME, gd_creds)
        gd_creds_path = saved[G_DRIVE_NAME]
      else:
        load_creds = load_credentials()
        if not load_creds:
          print('Please provide Google Drive Credentials file')
          quit()
        else:
          gd_creds_path = load_creds[G_DRIVE_NAME]
    client.initialize_api()
    if client.authorize:
      client.set_file('timeline', TIMELINE_PATH)
      client.get_home_timeline(page)
      read_and_download(TIMELINE_PATH, output)
      if drive:
        read_and_upload(gd_creds_path, output, APP_NAME)

if __name__ == "__main__":
  # main()
  pass
