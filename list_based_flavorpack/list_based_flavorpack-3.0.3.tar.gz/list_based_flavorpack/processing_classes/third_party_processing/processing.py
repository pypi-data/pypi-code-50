import os
import linecache
import sqlite3
from list_based_flavorpack.processing_classes.third_party_processing import \
    rules
from list_based_flavorpack.models import ListBasedRegion
from list_based_flavorpack.processing_classes.third_party_processing.rules import \
    get_region_table


class ThirdPartyProcessingClass:
    '''
    An example of a processing  class for a list based pool/region.
    Returns UUIDs stored in memory.
    '''

    def __init__(self):
        '''
        Sets processing rules.
        '''
        self.pre_processing_rules = [rules.ValidNumberDirectory,
                                     rules.SufficientNumbersStorage]
        self.post_processing_rules = []

    def get_pre_processing_rules(self):
        '''
        Returns processing rules to be executed prior to the generator running.
        '''
        return self.pre_processing_rules

    def get_post_processing_rules(self):
        '''
        Returns processing rules to be executed after the generator has run.
        '''
        return self.post_processing_rules

    def get_items(self, region, size):
        '''
        Pull numbers from the file created/updated from rules previously executed.
        '''
        first = region.last_number_line
        max_line = first + size
        lines = []
        linecache.checkcache(filename=region.file_path)
        for lineno in range(first, max_line):
            item = linecache.getline(region.file_path, lineno).strip()
            if not item:
                raise ValueError(
                    "There are not enough numbers available for this iteration starting on line number: %s",
                    lineno)
            lines.append(item)
        region.last_number_line = max_line
        region.save()
        return lines


class DBProcessingClass(ThirdPartyProcessingClass):
    '''
    Uses a SQLite database instead of a flat file.  When numbers are used
    they are removed from the database.
    '''

    def __init__(self):
        '''
        Sets processing rules.
        '''
        self.pre_processing_rules = [rules.ValidNumberDirectory,
                                     rules.SufficientDBNumbers]
        self.post_processing_rules = []

    def get_items(self, region: ListBasedRegion, size):
        connection = sqlite3.connect(region.db_file_path)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT serial_number FROM %s WHERE used = 0 LIMIT ?" % get_region_table(region),
            (size,)
        )
        rows = cursor.fetchall()
        lines = []
        for row in rows:
            lines.append(row[0])
            cursor.execute('DELETE FROM %s WHERE serial_number = ?'
                           % get_region_table(region), (row[0],))
        connection.commit()
        if len(rows) < size:
            raise ValueError("There are not enough numbers to satisfy the "
                             "request.")
        return lines
