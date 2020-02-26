#!/usr/bin/python3
import os
import platform


class BookMarkLocation(object):
    def __init__(self):
        home_path = os.environ["HOME"]
        if(platform.system() == 'Linux'):
            self.firefox_bookmark_location = "{}/.mozilla/firefox/".format(
                home_path)
        elif(platform.system() == 'Darwin'):
            self.firefox_bookmark_location = "{}/Library/Application Support/Firefox".format(
                home_path)

    def get_bookmark_location(self):
        for root, dirs, files in os.walk(self.firefox_bookmark_location):
            for file in files:
                if file.endswith("places.sqlite"):
                    return os.path.join(root, file)
