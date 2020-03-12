import httplib2
import pprint
import sys

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

class Sheets():
    def __init__(self, keyPath, spreadsheetId):
        """ 
        Classe: Sheets
        Descrição: Configura o acesso e recupera dados da API do Google Sheets
        
        param keyPath: Caminho e nome do arquivo que contém a chave de acesso para a API do Google Sheets
        param spreadsheetId: Id da planilha que será consultada
        """
        
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            keyPath,
            scopes='https://www.googleapis.com/auth/spreadsheets.readonly')
        
        http = httplib2.Http()
        http = credentials.authorize(http)

        self.service = build('sheets', 'v4', credentials=credentials, cache_discovery=False)
        self.spreadsheetId = spreadsheetId

    def getRangeData(self, range):
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.spreadsheetId,
                                    range=range).execute()
        values = result.get('values', [])

        return values