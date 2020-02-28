import time
import sys
import string
from collections import OrderedDict
import json
import hashlib
import logging
import requests
import pygsheets.client
from django.utils.six.moves.urllib.parse import urlencode
from django.utils.timezone import now
from inputflow.models import Input
from . import models
from . import credentials


logger = logging.getLogger(__name__)
autoimportLogger = logging.getLogger('googlesheets.autoimport')


class Utils:
    @staticmethod
    def fetch_token_info(token):
        """
        update token user_id and username if the token belongs to the oauth client
        selected in the settings object.
        """
        settings = models.Settings.objects.filter(oauth_client=token.client).first()
        if settings is not None:
            url = "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={}"
            url = url.format(token.access_token)
            response = requests.get(url)
            if response.status_code == 200:
                info = response.json()
                token.user_id = info['user_id']
                token.username = info['email']

    @staticmethod
    def get_spreadsheet(spreadsheet_obj):
        creds = credentials.Credentials(spreadsheet_obj.access_token)
        client = pygsheets.client.Client(creds)
        return client.open_by_url(spreadsheet_obj.url)

    @classmethod
    def get_worksheet(cls, spreadsheet_obj):
        spreadsheet = cls.get_spreadsheet(spreadsheet_obj)
        return spreadsheet.worksheets()[spreadsheet_obj.sheet_index]

    @staticmethod
    def worksheet_row_to_dict(row):
        non_empty = [col for col in row if col != '']
        if len(non_empty) == 0:
            return None
        cols = ['COL${}'.format(letter) for letter in string.ascii_uppercase]
        encode = lambda value: value.encode('utf-8') if sys.version_info.major == 2 else value
        result = [(col, encode(value)) for col, value in zip(cols, row) if value != '']
        result = OrderedDict(result)
        content = json.dumps(result)
        sha1 = hashlib.sha1(content.encode('utf-8'))
        result['_content_hash'] = sha1.hexdigest()
        return result

    @staticmethod
    def save_worksheet_row_to_input(spreadsheet_obj, row):
        encoded_row = urlencode(row)
        input_row = Input()
        input_row.settings = spreadsheet_obj.input_settings
        input_row.internal_source = True
        input_row.format = 'form'
        input_row.raw_content = encoded_row
        input_row.save()
        spreadsheet_obj.last_imported_row = row['row']
        spreadsheet_obj.last_imported_date = now()
        spreadsheet_obj.save()
        input_row.notify()

    @classmethod
    def import_to_input_flow(cls, spreadsheet_obj, max_count=50, start_row=None):
        if spreadsheet_obj.input_settings is None:
            return
        row_index = start_row or spreadsheet_obj.get_next_row_number()
        worksheet = cls.get_worksheet(spreadsheet_obj)
        count = 0
        imported = True
        while imported:
            values = worksheet.get_values((row_index, 1), (row_index+max_count-1, worksheet.cols))
            imported = False
            for row in values:
                row = cls.worksheet_row_to_dict(row)
                if row is None:
                    break
                row['row'] = row_index
                cls.save_worksheet_row_to_input(spreadsheet_obj, row)
                row_index += 1
                count += 1
                imported = True
        return count

    @classmethod
    def start_import(cls, spreadsheet_obj, max_count=50):
        return cls.import_to_input_flow(spreadsheet_obj, max_count=max_count,
            start_row=spreadsheet_obj.get_start_row_number())

    @classmethod
    def continue_import(cls, spreadsheet_obj, max_count=50):
        return cls.import_to_input_flow(spreadsheet_obj, max_count=max_count,
            start_row=spreadsheet_obj.get_next_row_number())

    @classmethod
    def autoimport_iteration(cls):
        autoimportLogger.info("Started spreadsheets automatically import.")
        for spreadsheet in models.Spreadsheet.objects.filter(enabled=True, automatically_imported=True):
            count = cls.continue_import(spreadsheet)
            autoimportLogger.info("Finished importing spreadsheet '{}': {} rows imported".format(spreadsheet.pk, count))
        autoimportLogger.info("Finished spreadsheets automatically import.")

    @classmethod
    def autoimport_forever(cls):
        while True:
            settings = models.Settings.objects.first()
            delta = 30 if settings is None else settings.autoimport_sleep
            if delta == 0:
                autoimportLogger.info("Autoimport disabled.")
            else:
                cls.autoimport_iteration()
            autoimportLogger.info("Sleeping for %ss...", delta)
            time.sleep(delta)
