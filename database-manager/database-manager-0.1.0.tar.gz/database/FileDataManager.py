import logging
import os


class FileDataManager:

    def __init__(self, tab_length=4):
        self.logger = logging.getLogger(__name__)
        self.file = None
        self.file_path = os.path.abspath(__file__)
        self.tab = ""
        for i in range(tab_length):
            self.tab += " "

    def open(self, file_path):
        self.file_path = os.path.join(self.file_path, file_path)
        self.logger.debug("Attempting to open file " + self.file_path)
        try:
            self.file = open(self.file_path, "w+")
        except OSError as e:
            self.logger.exception("Could not open file " + self.file_path)
            raise e
        else:
            self.logger.info("Opened file " + self.file_path)

    def write(self, text="", tabs=0, spaces=0):
        if tabs > 0:
            self.logger.debug("Writing " + str(tabs) + " tabs")
            for i in range(tabs):
                self.file.write(self.tab)
        if spaces > 0:
            self.logger.debug("Writing " + str(spaces) + " spaces")
            for i in range(spaces):
                self.file.write(" ")
        if len(text.split("\n", 1)[0]) > 0:
            self.logger.debug("Writing \"" + text.split("\n", 1)[0] + "\" to file.")
        else:
            self.logger.debug("Writing new line(s) to file.")
        self.file.write(text)
        if len(text.split("\n", 1)[0]) > 0:
            self.logger.info("Wrote \"" + text.split("\n", 1)[0] + "\" to file.")
        else:
            self.logger.info("Wrote new line(s) to file.")

    def write_line(self, text="", tabs=0, spaces=0, lines=1):
        self.logger.debug("Writing " + str(lines) + " lines")
        for i in range(lines):
            text += "\n"
        self.write(text, tabs, spaces)

    def close(self):
        self.logger.debug("Attempting to close file " + self.file_path)
        try:
            self.file.close()
        except OSError as e:
            self.logger.exception("Could not close file " + self.file_path)
            raise e
        else:
            self.logger.info("Closed file.")
