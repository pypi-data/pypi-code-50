# -*- coding: utf-8 -*-
"""
Description: Searches a directory and puts all singleton files into
a directory of their namesake.
"""

import os
import shutil


class Folderizer:
    def __init__(self, directory, metadata_filename="metadata.json", verbose=False):
        self._directory = directory
        self._metadata_filename = metadata_filename
        self._verbose = verbose
        self._action_counter = 0

        if self._verbose:
            print("[CURRENT ACTION: MOVING SINGLETON FILES TO FOLDERS]\n")

    def _find_single_files(self, directory=None):
        """
        :param str directory: The directory to locate single files.
        :return list: A list of single files.

        Finds all the files without a folder within a given directory.
        """
        if directory is None:
            directory = self._directory

        # And find all the single files:
        if self._verbose:
            print(
                f"[{self._action_counter}] [DISCOVERING SINGLE FILES IN FOLDER: {directory}]\n"
            )
            self._action_counter += 1

        single_files = [
            f
            for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
        ]

        return single_files

    def _move_files_into_folders(
        self, directory=None, metadata_filename=None, filenames=[]
    ):
        """

        :param str directory: Directory of single files to move into folders.
        :param str metadata_filename: The metadata file to ignore when folderizing.
        :param list filenames: A list of files to folderize.
        :return: None

        Moves a group of files into their respective folders, given a list of filenames.
        Will create the folder if it does not already exist.
        """
        if directory is None:
            directory = self._directory

        if metadata_filename is None:
            metadata_filename = self._metadata_filename

        for filename in filenames:
            if filename != self._metadata_filename:
                old_filepath = os.path.join(directory, filename)
                stripped_filename, file_ext = os.path.splitext(
                    filename
                )  # Extract the filename from the extension
                new_filepath = os.path.join(directory, stripped_filename)

                if not os.path.exists(
                    new_filepath
                ):  # If the folder doesn't already exist:
                    os.mkdir(new_filepath)  # Then create it
                    if self._verbose:
                        print(f'[{self._action_counter}] [CREATED FOLDER] "{filename}"')
                        self._action_counter += 1

                shutil.move(old_filepath, new_filepath)
                if self._verbose:
                    print(
                        f'[{self._action_counter}] [MOVED FILE] "{filename}" -> [FOLDER] "{filename}"'
                    )
                    self._action_counter += 1

    def folderize(self, directory=None, metadata_filename=None):
        """

        :param str directory: Directory of single files to folderize.
        :param str metadata_filename: The metadata file to ignore when folderizing.
        :return: None

        Puts all singleton files from a directory into a folder of its namesake.
        """
        if directory is None:
            directory = self._directory

        if metadata_filename is None:
            metadata_filename = self._metadata_filename

        if self._verbose:
            print(
                f"[{self._action_counter}] [RUNNING FOLDERIZE ON SINGLE FILES IN FOLDER: {directory}]\n"
            )
            self._action_counter += 1

        filenames = self._find_single_files(
            directory=directory
        )  # Get all filenames in the given directory
        self._move_files_into_folders(
            directory=directory,
            metadata_filename=metadata_filename,
            filenames=filenames,
        )  # And move those into folders, based on the same names

    def unfolderize_all(self, directory=None):
        """
        Removes all files from every folder and places them into the main directory,
        then removes all the folders.
        """
        pass

    def unfolderize(self, directory=None, folder_name=None):
        """

        :param str directory: Directory of folderized files.
        :param str folder_name: Folder name to unfolderize.
        :return: None

        Removes all files from every folder named <folder_name> and places them into the
        current root directory, then removes the folder named <folder_name>.
        """
        if directory is None:
            directory = self._directory

        if self._verbose:
            print(
                f"[{self._action_counter}] [RUNNING UNFOLDERIZE ON SINGLE FILES IN FOLDER: {directory}]\n"
            )
            self._action_counter += 1

        for root, dirs, files in os.walk(directory):
            for folder in dirs:
                if folder.lower() == folder_name.lower():
                    for file in self._find_single_files(
                        directory=os.path.join(root, folder)
                    ):
                        old_filepath = os.path.join(root, folder, file)
                        new_filepath = os.path.join(root, file)
                        if self._verbose:
                            print(
                                f"[{self._action_counter}] [MOVING FILE] {old_filepath} -> [FOLDER] {new_filepath}\n"
                            )
                            self._action_counter += 1
                        shutil.move(old_filepath, new_filepath)
                    shutil.rmtree(os.path.join(root, folder))
                    if self._verbose:
                        print(
                            f"[{self._action_counter}] [FOLDER] {os.path.join(root, folder)} [REMOVED]\n"
                        )
                        self._action_counter += 1
