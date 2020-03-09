import os
import sys


class IniFile(object):
    def __init__(self, filename=None):
        self.data = {}
        if filename is not None:
            self.filename = filename
            basename = filename.split("/")[-1]
            self.filename = filename
            self.root_dir = self.filename[0:len(filename)-len(basename)]
            if os.path.isfile(filename):
                self.load()

    def load(self):
        f = open(self.filename, 'r')
        for line in f:
            line = line.strip()
            whitespace = False
            comment = False
            header = False
            key = False
            if line == "":
                whitespace = True
            elif line.find("#") == 0:
                comment = True
            elif line.startswith("[") and line.endswith("]"):
                header = True
            elif line.find("=") > -1:
                key = True

            if whitespace or comment:
                continue
            elif header:
                # a new header
                current_header = {}
                header_key = line.strip("[]")
                if self.data.get(header_key) is None:
                    # saves against multiple declarations of the header
                    self.data[header_key] = {}
            elif key:
                key_name, value = line.split("=", 1)
                self.data[header_key][key_name] = value
        f.close()

    def save(self):
        f = open(self.filename, 'w')
        for header_key in self.get_headers():
            line = "[" + header_key + "]"
            f.write(line)
            f.write("\n")
            for value_key in self.get_header_keys(header_key):
                value = self.get(header_key, value_key)
                if value is None:
                    value = ""
                line = "{}={}".format(value_key, value)
                f.write(line)
                f.write("\n")
            f.write("\n")
        f.close()

    def get(self, header, key, default_value=None):
        keys = self.data.get(header) or {}
        return keys.get(key) or default_value

    def set(self, header, key, value):
        keys = self.data.get(header) or {}
        self.data[header] = keys
        keys[key] = str(value)

    def get_headers(self):
        return self.data.keys()

    def get_header_keys(self, header):
        entry = self.data.get(header) or {}
        return entry.keys()

    def get_root_dir(self):
        return self.root_dir

