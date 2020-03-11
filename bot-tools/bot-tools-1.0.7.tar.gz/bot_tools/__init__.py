__version__ = "1.0.7"
import os
import json
import time
import shutil
import io
from pathlib import Path
from colorama import Fore

BT_LOG_LEVEL = 1


class BotTools:

    @staticmethod
    def write_json(path, content):
        # write json to a plain text file
        while True:
            try:
                with io.open(path, 'w', encoding='utf8') as f:
                    try:
                        json.dump(content, f)
                        return True
                    except Exception as e:
                        print(e)
                        return False
            except Exception as e:
                print("ERROR unable to save json details: " + content)

    @staticmethod
    def read_json(path):
        # read json from a plain text file
        with open(path) as json_file:
            data = json.load(json_file)
        return data

    @staticmethod
    def add_line(file, line):
        # add a line to a text file
        try:
            with open(file, "a", encoding='utf8') as f:
                f.write(line + "\n")
            return True
        except Exception as e:
            print(e)
            print('error writing line to ' + file)
            return False

    @staticmethod
    def remove_line(file, remove_line):
        # remove a line from a text file
        with open(file, 'r+') as f:
            t = f.read()
            f.seek(0)
            for line in t.split('\n'):
                if line != remove_line:
                    f.write(line + '\n')
            f.truncate()

    @staticmethod
    def write_text(path, content):
        # write text to plain text file, note this will delete anything in the file if not empty.
        try:
            newfile = open(path, 'w')
            newfile.write(str(content))
            newfile.close()
            return True
        except Exception as e:
            print("ERROR unable to write_text(): " + str(e))
        return False

    @staticmethod
    def read_text(path):
        # read text from a plain text file
        file = open(path, 'r')
        return file.read()

    @staticmethod
    def read_lines(path):
        # read lines to an array from a text file
        while True:
            try:
                with open(path) as f:
                    the_list = f.readlines()
                    the_list = [x.strip() for x in the_list]
                return the_list
            except Exception as e:
                print("enable to open file for read_lines()")

    @staticmethod
    def move_file(source, destination):
        # move a file
        tries = 0
        while True:
            try:
                shutil.move(source, destination)
                break
            except Exception as e:
                print("unable to move: " + source)
                print(e)

                time.sleep(5)
                tries += 1

                if tries > 5:
                    print("unable to move (fatal): " + source)
                    break

    @staticmethod
    def print_json(json_text):
        # pretty dump for json
        print(json.dumps(json_text, indent=4, sort_keys=True))

    @staticmethod
    def list_files(path, file_type):
        # get all files in a folder and sub folders based on type
        return list(Path(path).rglob("*."+file_type))

    @staticmethod
    def log(message, log_level=1, log_type='NOTICE', color=Fore.CYAN):
        if log_level >= BT_LOG_LEVEL:
            if log_level == 1:
                print(Fore.GREEN + '[NOTICE] ' + str(message) + Fore.RESET)
            if log_level == 2:
                print(Fore.YELLOW + '[WARNING] ' + str(message) + Fore.RESET)
            if log_level == 3:
                print(Fore.RED + '[ERROR] ' + str(message) + Fore.RESET)
            if log_level == 4:
                print(color + '[' + log_type + '] ' + str(message) + Fore.RESET)

    @staticmethod
    def check_folder(folder):
        # create the target folder
        try:
            if not os.path.isdir(folder):
                try:
                    os.makedirs(folder, exist_ok=True)
                    return True
                except OSError as e:
                    BotTools.log('Unable to create folder', 4)
                    BotTools.log(e, 4)
            return False
        except Exception as e:
            BotTools.log('Unable to create folder', 4)
            BotTools.log(e, 4)
            return False

