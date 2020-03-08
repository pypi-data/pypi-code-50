#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains Drive tracking class for Artella projects
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging
import urllib2
import traceback

import gspread
from oauth2client.service_account import ServiceAccountCredentials
# from artellapipe.libs.drive.externals.oauth2client.service_account import ServiceAccountCredentials

from tpDcc.libs.python import decorators, python

import artellapipe.register
from artellapipe.managers import tracking
import artellapipe.libs.drive as drive_lib

LOGGER = logging.getLogger()


@decorators.Singleton
class DriveTrackingManager(tracking.TrackingManager, object):

    def __init__(self):
        tracking.TrackingManager.__init__(self)
        self._client = None
        self._spreadsheets = list()
        self._worksheets = dict()

    @property
    def spreadsheets(self):
        return self._spreadsheets

    @property
    def worksheets(self):
        return self._worksheets

    def update_tracking_info(self):

        python.clear_list(self._spreadsheets)
        self._worksheets.clear()

        try:
            valid_login = self.login()
            if not valid_login and self._client:
                LOGGER.error("Production Tracking was not loaded successfully!")
                return False

            worksheets = drive_lib.config.data.get('worksheets', None)
            if not worksheets:
                LOGGER.warning('Drive Production Tracking Configuration File does not specifies any worksheet!')
                return False

            found_worksheets = dict()
            for sheet in self._spreadsheets:
                for worksheet_name, worksheet_data in worksheets.items():
                    found_worksheets[worksheet_name] = list()
                    try:
                        worksheet = sheet.worksheet(worksheet_name)
                        found_worksheets[worksheet_name].append(worksheet)
                    except gspread.models.WorksheetNotFound as exc:
                        LOGGER.warning(
                            'Production Tracking Worksheet: "{}" does not exists in sheet: "{}"!'.format(
                                worksheet_name, sheet))
                        continue

            for worksheet_name, worksheets_list in found_worksheets.items():
                if not worksheets_list:
                    LOGGER.warning('No worksheets with name "{}" found in registered spreadsheets: {}'.format(
                        worksheet_name, self._spreadsheets))
                    continue
                if len(worksheets_list) > 1:
                    LOGGER.warning(
                        'Multiple worksheets found name "{}" in registered spreadsheets: {}. '
                        'Only first one will be used'.format(worksheet_name, worksheets_list))
                self._worksheets[worksheet_name] = worksheets_list[0]
        except Exception as exc:
            LOGGER.error('Error while getting information from Drive: {} | {}'.format(exc, traceback.format_exc()))

        self._updated = True

        return True

    def is_tracking_available(self):

        self.check_update()

        if not self._client:
            LOGGER.warning("Production Tracking Client is not initialized yet!")
            return False

        if not self._spreadsheets:
            LOGGER.warning("No Production Tracking Spreadsheets loaded!")
            return False

        if not self._worksheets:
            LOGGER.warning("Production Tracking has no loaded data!")
            return False

        return True

    def login(self, *args, **kwargs):

        credentials = drive_lib.config.data.get('credentials', None)
        scope = drive_lib.config.data.get('scope', list())
        if not credentials:
            LOGGER.warning("Non-valid Drive credentials found ...")
            return False

        creds = ServiceAccountCredentials._from_parsed_json_keyfile(dict(credentials), scope)
        try:
            self._client = gspread.authorize(creds)
        except Exception(RuntimeError, ValueError) as exc:
            LOGGER.error('Error while logging into Drive Production Tracking ...')
            raise(exc)

        spreadsheets = drive_lib.config.data.get('spreadsheets', None)
        if not spreadsheets:
            LOGGER.warning('No spreadsheets to open defined in Drive Production Tracking Configuration File!')
            return False

        for spreadsheet_name in spreadsheets:
            try:
                open_sheet = self._client.open(spreadsheet_name)
                self._spreadsheets.append(open_sheet)
            except gspread.client.SpreadsheetNotFound as exc:
                LOGGER.warning('Production Tracking Sheet Document: "{}" does not exists!'.format(spreadsheet_name))
                continue

        if not self._spreadsheets:
            LOGGER.warning(
                'Any of the spreadsheets defined in Drive Production Tracking Configuration File were valid!')
            return False

        return True

    def all_project_assets(self):

        self.check_update()

        assets_data = list()

        if not self.is_tracking_available():
            return None

        assets_worksheet_name = drive_lib.config.data.get('assets_worksheet_name', 'Assets')
        assets_worksheet = self._worksheets.get(assets_worksheet_name, None)
        if not assets_worksheet:
            LOGGER.warning('No Assets Worksheet with name "{}" found in Drive Production Tracking Data!'.format(
                assets_worksheet_name
            ))
            return None

        worksheets_data = drive_lib.config.data.get('worksheets', {}).get(assets_worksheet_name, None)
        if not worksheets_data:
            LOGGER.warning(
                'No worksheet data defined for worksheet "{}" in Drive Production Tracking '
                'Configuration File!'.format(assets_worksheet))
            return None

        table_fields_row = worksheets_data.get('fields_row', 1)

        data = assets_worksheet.get_all_records(head=table_fields_row)
        if not data:
            LOGGER.warning('No data retrieved from worksheet "{}" in Drive Production Tracking Spreadsheet!'.format(
                assets_worksheet))

        for item_dict in data:
            valid_item = False
            for k in item_dict.values():
                if k:
                    valid_item = True
            if not valid_item:
                continue
            # Make sure all keys are lower case
            item_dict = {k.lower(): v for k, v in item_dict.items()}
            assets_data.append(item_dict)

        return assets_data

    def download_preview_file_thumbnail(self, preview_id, file_path):

        filedata = urllib2.urlopen(preview_id)
        datatowrite = filedata.read()

        with open(file_path, 'wb') as f:
            f.write(datatowrite)


artellapipe.register.register_class('Tracker', DriveTrackingManager)
