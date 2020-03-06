import json


class Settings(object):
    def __init__(self, filename="settings.json"):
        self._filename = filename
        with open(filename, "r") as f:
            self._jsondata = json.load(f)

    def __str__(self):
        return json.dumps(self._jsondata, sort_keys=True, indent=4)

    def __repr__(self):
        return "Settings(filename='%s')" % self._filename

    def __getitem__(self, key):
        if isinstance(key, str):
            return self._jsondata[key]
        return NotImplemented
