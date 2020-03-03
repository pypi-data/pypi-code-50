# -*- coding: utf-8 -*-
"""
Description:

Executes a five part movie folder formatting workflow for a given directory.

The workflow actions are as follows:

1. [Folderizer] Searches a directory and puts all singleton files into a directory of their namesake.

2. [FileRemover] Removes any files with unwanted extensions like ".txt" or ".dat".

3. [Formatter] Formats all the files and folders in a given directory based on their movie title
and creates a title directory called "contents.json", which also contains poster information.

4. [PosterFinder] Reads that "contents.json" file and downloads the poster for each title.

5. [SubtitleFinder] Reads the "contents.json" file and downloads the subtitle for each title.

"""

import argparse
import json
import os
import sys

from movie_file_fixer.file_remover import FileRemover
from movie_file_fixer.folderizer import Folderizer
from movie_file_fixer.formatter import Formatter
from movie_file_fixer.poster_finder import PosterFinder
from movie_file_fixer.subtitle_finder import SubtitleFinder


def main():
    args = parse_args(sys.argv[1:])

    utils = args.utils
    if utils:
        movie_file_fixer = MovieFileFixer(directory=args.directory, util="title_fixer")
        movie_file_fixer.run()
    else:
        movie_file_fixer = MovieFileFixer(
            directory=args.directory,
            file_extensions=args.file_extensions,
            metadata_filename=args.metadata_filename,
            language=args.language,
            result_type=args.result_type,
            verbose=args.verbose,
        )
        movie_file_fixer.folderize()
        movie_file_fixer.cleanup()
        movie_file_fixer.format()
        movie_file_fixer.get_posters()
        movie_file_fixer.get_subtitles()


def parse_args(args):
    """

    :param list args: The list of arguments to parse.
    :return argparse.Namespace: An object which contains all parsed arguments as attributes.

    Convert argument strings to objects and assign them as attributes of the namespace.
    Return the populated namespace.
    """
    parser = argparse.ArgumentParser(
        description="A command line utility to help create a rich multimedia library out of your backup movie collection."
    )
    parser.add_argument(
        "--directory",
        "-d",
        type=str,
        help="A directory containing raw movie files and folders.",
    )
    parser.add_argument(
        "--file_extensions",
        "-e",
        action="append",
        default=[".idx", ".sub", ".nfo", ".dat", ".jpg", ".png", ".txt", ".exe"],
        help="A directory containing raw movie files and folders.",
    )
    parser.add_argument(
        "--metadata_filename",
        "-f",
        type=str,
        default="metadata.json",
        help="To specify a pre-built or custom metadata filename.",
    )
    parser.add_argument(
        "--language",
        "-l",
        type=str,
        default="en",
        help="To specify a two-character language encoding for subtitles.",
    )
    parser.add_argument(
        "--result_type",
        "-r",
        type=str,
        default="movie",
        choices=["movie", "series", "episode"],
        help="To specify a type of IMDb object result to return metadata and poster information for.",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        default=False,
        help="Set this flag to enable verbose print statements.",
    )
    parser.add_argument(
        "--utils",
        "-u",
        action="store_true",
        default=False,
        help="Set this flag to use a utility function.",
    )
    parser.add_argument(
        "--util_name",
        "-n",
        type=str,
        default="title_fixer",
        choices=["title_fixer"],
        help="Choose a stand-alone utility to run",
    )
    return parser.parse_args(args)


class MovieFileFixer:
    def __init__(
        self,
        directory,
        file_extensions=[
            ".idx",
            ".sub",
            ".nfo",
            ".dat",
            ".jpg",
            ".png",
            ".txt",
            ".exe",
        ],
        metadata_filename="metadata.json",
        language="en",
        result_type="movie",
        util="title_fixer",
        verbose=False,
    ):
        default_file_extensions = [
            ".idx",
            ".sub",
            ".nfo",
            ".dat",
            ".jpg",
            ".png",
            ".txt",
            ".exe",
        ]
        self._directory = directory
        self._file_extensions = (
            file_extensions if file_extensions else default_file_extensions
        )
        self._metadata_filename = metadata_filename
        self._language = language
        self._result_type = result_type
        self._util = util
        self._verbose = verbose

    def folderize(
        self, directory=None, metadata_filename=None, folder_name="subs", verbose=None
    ):
        """

        :param str directory: The directory of single files to folderize.
        :param str metadata_filename: The metadata file to ignore when folderizing.
        :param str folder_name: Folder to unfolderize files from.
        :param bool verbose: Whether or not to activate verbose mode.
        :return: None

        1. Place all single files in folders of the same name.
            a. Pull all subtitle files out of folders if they are in them.
        """
        if directory is None:
            directory = self._directory

        if metadata_filename is None:
            metadata_filename = self._metadata_filename

        if verbose is None:
            verbose = self._verbose

        folderizer = Folderizer(
            directory=directory, metadata_filename=metadata_filename, verbose=verbose
        )
        folderizer.folderize()
        folderizer.unfolderize(folder_name=folder_name)

    def cleanup(self, directory=None, file_extensions=None, verbose=None):
        """

        :param str directory: The directory of movie folders to clean.
        :param list file_extensions: A list of file extensions to remove.
        :param bool verbose: Whether or not to activate verbose mode.
        :return: None

        2. Remove all non-movie files, based on a list of "bad" extensions (i.e., .nfo, .txt, etc)
        """
        if directory is None:
            directory = self._directory

        if file_extensions is None:
            file_extensions = self._file_extensions

        if verbose is None:
            verbose = self._verbose

        file_remover = FileRemover(
            directory=directory, file_extensions=file_extensions, verbose=verbose
        )
        file_remover.remove_files()

    def format(self, directory=None, result_type=None, verbose=None):
        """

        :param str directory: The directory of movie folders to format.
        :param str result_type: What type of IMDb object you want returned. Valid Options: [`movie`, `series`, `episode`]
        :param bool verbose: Whether or not to activate verbose mode.
        :return: None

        3. Pull the names of all folders and decide what the title is, based on movie titles in OMDb API.
            a. Rename the movie file and folders (i.e., <movie_title> [<year_of_release>])
        """
        if directory is None:
            directory = self._directory

        if verbose is None:
            verbose = self._verbose

        if result_type is None:
            result_type = self._result_type

        formatter = Formatter(
            directory=directory, result_type=result_type, verbose=verbose
        )
        formatter.format()

    def get_posters(self, directory=None, metadata_filename=None, verbose=None):
        """

        :param str directory: The directory of movie folders to get posters for.
        :param str metadata_filename: The metadata file to get the poster URL from.
        :param bool verbose: Whether or not to activate verbose mode.
        :return: None

        4. Download the movie poster and name the file poster.<extension>
        (where <extension> is the original extension of the poster file)
        """
        if directory is None:
            directory = self._directory

        if metadata_filename is None:
            metadata_filename = self._metadata_filename

        if verbose is None:
            verbose = self._verbose

        poster_finder = PosterFinder(
            directory=directory, metadata_filename=metadata_filename, verbose=verbose
        )
        poster_finder.get_posters()

    def get_subtitles(
        self, directory=None, metadata_filename=None, language=None, verbose=None
    ):
        """

        :param str directory: The directory of movie folders to get subtitles for.
        :param str metadata_filename: The metadata file to get movie paths from.
        :param str language: The two-character language code for the subtitle language to retrieve.
        :param bool verbose: Whether or not to activate verbose mode.
        :return: None

        5. Download the movie subtitles and name the file <language>_subtitles.srt
        """
        if directory is None:
            directory = self._directory

        if metadata_filename is None:
            metadata_filename = self._metadata_filename

        if language is None:
            language = self._language

        if verbose is None:
            verbose = self._verbose

        subtitle_finder = SubtitleFinder(
            directory=directory,
            metadata_filename=metadata_filename,
            language=language,
            verbose=verbose,
        )
        subtitle_finder.get_subtitles()

    def title_fixer(self, directory=None, metadata_filename=None, verbose=None):
        """

        :param str directory: The directory of movie folders to fix titles in.
        :param str metadata_filename: The metadata file to get `titles` metadata from.
        :param bool verbose: Whether or not to activate verbose mode.
        :return None:

        Given a directory and metadata file, will use the `original_filename` and `imdb_id`
        to determine the correct title information for the files/folders in the directory.
        """
        if directory is None:
            directory = self._directory

        if metadata_filename is None:
            metadata_filename = self._metadata_filename

        if verbose is None:
            verbose = self._verbose

        formatter = Formatter(directory=directory, verbose=verbose)

        metadata = formatter.initialize_metadata_file(
            directory=directory, metadata_filename=metadata_filename
        )

        all_folders = [
            folder_name
            for folder_name in os.listdir(directory)
            if folder_name != metadata_filename
        ]

        titles = metadata.get("titles")
        while len(all_folders) > 0:
            for title_index in range(len(titles)):
                title_data = titles[title_index]
                # See if the file is in the given directory:
                original_filename = title_data.get("original_filename")
                # formatted_title = title_data.get('title')

                # If a file hasn't been formatted OR it has already been formatted, such as
                if original_filename in all_folders:
                    # Use the IMDb ID to find the IMDb object metadata:
                    imdb_id = title_data.get("imdb_id")
                    imdb_object = formatter.get_imdb_object(
                        search_query="", imdb_id=imdb_id
                    )
                    metadata["metadata"].append(imdb_object)

                    # Gather the important bits of metadata:
                    title = imdb_object.get("Title")
                    poster = imdb_object.get("Poster")
                    release_year = imdb_object.get("Year")
                    formatted_title = title + " [" + release_year + "]"
                    # If it is, rename the folder and its contents:
                    formatter.rename_folder_and_contents(
                        original_name=original_filename,
                        new_name=formatted_title,
                        directory=directory,
                    )
                    # mark that folder complete:
                    all_folders.remove(original_filename)
                    print(f"{original_filename} removed!")
                    print(f"All Folders:{all_folders}\n")

                    # set the potentially incorrect or missing metadata:
                    title_data["title"] = formatted_title
                    title_data["poster"] = poster

        # Finally, write the updated metadata to the metadata file:
        metadata_filepath = os.path.join(directory, metadata_filename)
        with open(metadata_filepath, "w+") as outfile:
            json.dump(metadata, outfile, indent=4)

    def run(self, directory=None, metadata_filename=None, util=None, verbose=None):

        """
        :param str directory: The directory of movie folders to run the given `util` on.
        :param str metadata_filename: The metadata file to get metadata from.
        :param str util: The name of the utility function to run.
        :param bool verbose: Whether or not to activate verbose mode.
        :return None:

        Runs stand-alone utility functions.

        Utility Functions Available:

        `title_fixer`: Fixes titles (folders, directories, and subtitles files) based on
        given metadata file `titles.original_filename` and `titles.imdb_id` values.
        """
        if directory is None:
            directory = self._directory

        if metadata_filename is None:
            metadata_filename = self._metadata_filename

        if verbose is None:
            verbose = self._verbose

        if util is None:
            util = self._util

        if util == "title_fixer":
            self.title_fixer(
                directory=directory,
                metadata_filename=metadata_filename,
                verbose=verbose,
            )
