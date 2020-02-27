"""
Contains class jsonnote - a simple interface for working with JSON files.
Properties:
    filename - name of the file without the extension (extention '.json' will be added automatically).
    location - location of the file. Once set, the file can be found and read from or write into.
    contents - JSON contents of the class instance.
Methods:
    full_path()
    file_exists()
    is_empty()      - returns True/False depending on whether the contents of the class instance are empty
    get_from_file() - reads contents from the JSON file
    save_to_file()  - saves contents in the JSON  file
    clear()         - empties the contents
    destroy()       - empties the contents and erases the file from the disc
    reset()         - empties the contents, destroys the file and sets 'filename' and 'location' to 'None'

    Example of use:

        x = jsondata()
        x.filename = <filename>
        x.location = <some directory>
        x.contents = <data in JSON format>
        x.save_to_file() # the JSON code is now saved in the file specified
        print(x.get_from_file()) # contents are read from file
        x.reset()
"""
import logging
import os
import json

logger = logging.getLogger(__name__)

class jsonnote():

    def __init__(self):
        self._f = None
        self._dir = None
        self._contents = {}
        self.mustsave = False
        self.mustdelete = False

    @property
    def filename(self):
        return self._f

    @filename.setter
    def filename(self, val):
        if val is not None:
            if not '.json' in val:
                val = val + '.json'
            self._f = val
        else:
            self._f = None

    @property
    def location(self):
        return self._dir

    @location.setter
    def location(self, val):
        self._dir = val

    def full_path(self):
        assert self.location != None, 'File location is not set.'
        return self.location + os.sep + self.filename

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, obj):
        self._contents = obj

    def file_exists(self):
        return os.path.exists(self.full_path())

    def is_empty(self):
        return self.contents == {}

    def get_from_file(self):
        with open(self.full_path(), 'r') as f:
            self.contents = json.load(f)

    def save_to_file(self):
        if self.mustsave:
            with open(self.full_path(), 'w') as f:
                json.dump(self.contents, f)

    def clear(self):
        self.contents = {}
        logger.debug('Contents cleared.')

    def destroy(self):
        self.clear()
        if self.mustdelete:
            self._file_delete()

    def reset(self):
        self.clear()
        self.destroy()
        self.filename = None
        self.location = None

    def _file_delete(self):
        try:
            os.remove(self.full_path())
            logger.debug(self.full_path() + ' deleted.')
        except FileNotFoundError:
            logger.debug(self.full_path() + ' not found (nothing to delete.)')
