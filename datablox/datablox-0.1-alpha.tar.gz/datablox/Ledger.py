import json
import os

class Ledger:
    def __init__(self, parent_directory = None):
        self.index = {}

        self.parent_directory = "."
        if parent_directory:
            self.parent_directory = parent_directory

    def directory(self):
        return self.parent_directory + "/ledger"

    def write(self):
        if not os.path.exists(self.directory()):
            os.mkdir(self.directory())
            