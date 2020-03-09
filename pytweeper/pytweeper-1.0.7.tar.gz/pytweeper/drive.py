from pathlib import Path
from datetime import datetime
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

TOKEN_FILE = 'token.pkl'
DRIVE_SERVICE = 'drive'
DRIVE_SERVICE_VERSION = 'v3'

ROOT_FOLDER = Path(__file__).resolve().parent
TOKEN_PATH = Path.joinpath(ROOT_FOLDER, TOKEN_FILE)

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly', 'https://www.googleapis.com/auth/drive.file']

class Drive:
  def __init__(self, creds_path):
    self.creds = None
    self.service = None
    self.folder = []
    self.creds_path = creds_path
  
  def authenticate(self):
    if Path.exists(TOKEN_PATH):
      with open(TOKEN_PATH, 'rb') as token:
        self.creds = pickle.load(token)
    if not self.creds or not self.creds.valid:
      if self.creds and self.creds.expired and self.creds.refresh_token:
        self.creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
          self.creds_path, SCOPES
        )
        self.creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'wb') as token:
          pickle.dump(self.creds, token)
    self.build_service()
  
  def build_service(self):
    if self.creds:
      self.service = build(DRIVE_SERVICE, DRIVE_SERVICE_VERSION, credentials=self.creds)
  
  def get_files(self):
    result = self.service.files().list(
      pageSize=10, fields="nextPageToken, files(id, name)"
    ).execute()
    items = result.get('files', [])
    return items
  
  def upload_file(self, file_path, file_name):
    if self.folder:
      file_metadata = {
        "name": file_name,
        "parents": self.folder
      }
    else:
      file_metadata = {
        "name": file_name,
      }
    FILE_PATH = Path.absolute(file_path)
    media = MediaFileUpload(FILE_PATH, mimetype='image/jpeg')
    file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file

  def check_folder_if_exist(self, folder_name):
    check = self.service.files().list(
      q="name='%s' and mimeType='application/vnd.google-apps.folder'" % folder_name,
      spaces='drive'
    ).execute()
    folder_list = list(map(lambda f: f['id'], check.get('files')))
    return folder_list

  def create_folder(self, name, parents=None):
    if parents:
      file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': parents
      }
    else:
      file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder'
      }
    file = self.service.files().create(body=file_metadata, fields='id').execute()
    return file

  def select_folder(self, folder):
    self.folder = folder
    return self.folder

if __name__ == "__main__":
  '''Init Google Drive'''
  # d = Drive()
  # d.authenticate()

  '''Get files'''
  # files = d.get_files()
  # print("Files:", files)

  '''Upload file'''
  # TARGET_FOLDER = '1EJRFpb-EjgA0_xoCgRSWc6kopNzQNwMo'
  # today = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
  # folder_id = d.create_folder(today, [TARGET_FOLDER]).get('id')
  # d.select_folder([folder_id])
  # upload = d.upload_file('images/0natvLeMZEPC4Xz4.jpg', '0natvLeMZEPC4Xz4.jpg')
  
  '''Create folder'''
  # folder = d.create_folder('pytweeper')
  # print(folder)

  '''Check folder if exist'''
  # print(d.check_folder_if_exist('pytweepers'))
  
  print("Google Drive API Module")