# -*- coding: utf-8 -*-
"""

Description: Removes any files with unwanted extensions like ".txt" or ".dat".
"""

import os


class FileRemover:
    def __init__(
        self,
        directory,
        file_extensions=[
            ".txt",
            ".dat",
            ".nfo",
            ".bmp",
            ".gif",
            ".jpg",
            ".png",
            ".exe",
        ],
        verbose=False,
    ):
        self._directory = directory
        self._file_extensions = file_extensions
        self._verbose = verbose
        self._action_counter = 0

        if self._verbose:
            print("[CURRENT ACTION: REMOVING UNWANTED FILES]\n")

    def remove_files(self, directory=None, file_extensions=None):
        """

        :param str directory: Directory to remove files from.
        :param list file_extensions: A list of file extensions to remove.
        :return: None
        """
        if directory is None:
            directory = self._directory

        if file_extensions is None:
            file_extensions = self._file_extensions

        for root, dirs, files in os.walk(directory):
            for current_file in files:
                if self._verbose:
                    print(f"[{self._action_counter}] [PROCESSING FILE: {current_file}]")
                    self._action_counter += 1

                filename, extension = os.path.splitext(current_file)

                if extension in file_extensions:
                    os.remove(os.path.join(os.getcwd(), root, current_file))
                    if self._verbose:
                        print("[RESULT: REMOVED]\n")
                else:
                    if self._verbose:
                        print("[RESULT: NOT REMOVED]\n")
