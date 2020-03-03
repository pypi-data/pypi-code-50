# -*- coding: utf-8 -*-
"""

Description: Reads the "metadata.json" file and downloads the subtitle for each title, given a language of preference.
"""

import hashlib
import json
import os

import requests


class SubtitleFinder:
    def __init__(
        self,
        directory=None,
        metadata_filename="metadata.json",
        language="en",
        verbose=False,
    ):
        self._directory = directory
        self._metadata_filename = metadata_filename
        self._language = language
        self._verbose = verbose
        self._action_counter = 0

        if self._verbose:
            print("[CURRENT ACTION: LOCATING MOVIE SUBTITLES]\n")

    def _is_movie_file(self, filename):
        """

        :param filename: The filename to assess.
        :return bool: Whether the given filename is a movie file or not.

        This method returns True if the given filename is a movie file and False if not.
        """
        if self._verbose:
            print(f'[{self._action_counter}] [PROCESSING FILE] "{filename}"\n')
            self._action_counter += 1

        movie_file_extensions = [".avi", ".mp4", ".mkv", ".mov"]
        filename, extension = os.path.splitext(filename)
        if extension in movie_file_extensions:
            if self._verbose:
                print(f'[INFO] "{filename}" [IS A] [MOVIE FILE]\n')
            return True
        else:
            if self._verbose:
                print(f'[INFO] "{filename}" [IS NOT A] [MOVIE FILE]\n')
            return False

    def _get_movie_file_paths(self, directory):
        """

        :param str directory: A directory containing movie files.
        :return list: A list of movie file paths.

        This method takes a directory that contains files and returns all files that are movie files.
        """
        movie_file_paths = []
        if os.path.exists(directory):
            for filename in os.listdir(directory):
                if self._is_movie_file(filename=filename):
                    movie_file_path = os.path.join(directory, filename)
                    movie_file_paths.append(movie_file_path)

        return movie_file_paths

    def _get_hash(self, filepath, size=64):
        """

        :param str filepath: The path to the file to be hashed.
        :param int size: The size (in KB) of the chunks to hash.
        :return str: The `md5` hash of the end chunks from the file at the given filepath.

        This hash function receives the name of the file and returns the `md5` hash of the beginning
        and end `size` KB sized chunks.

        i.e. If `size=64`, we will take a 64KB chunk from the beginning and end of the file and return
        the `md5` hash of those chunks.
        """
        if self._verbose:
            print(
                f'[{self._action_counter}] [PROCESSING FILE] [HASHING] [FILEPATH] "{filepath}"\n'
            )
            self._action_counter += 1

        readsize = size * 1024
        with open(filepath, "rb") as f:
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)

        file_hash = hashlib.md5(data).hexdigest()

        if self._verbose:
            if self._verbose:
                print(f'[INFO] "{filepath}": [HASH] "{file_hash}"\n')

        return file_hash

    def _download(self, url="http://api.thesubdb.com/", payload=None, headers=None):
        """

        :param str url: The SubDb API URL.
        :param dict headers: A dictionary containing custom headers. Default only contains the `User-Agent`.
        :return requests.Response: A `requests.Response` object containing the file being requested.

        This method performs a GET request on the given URL, using the given payload and headers (if desired).
        """
        if headers is None:
            headers = {
                "User-Agent": "SubDB/1.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11; https://github.com/blairg23/movie-file-fixer"
            }

        if self._verbose:
            print(f'[{self._action_counter}] [DOWNLOADING] [FILE] from [URL] "{url}"\n')
            self._action_counter += 1

        return requests.get(url=url, params=payload, headers=headers)

    def _search_subtitles(self, hashcode=None):
        """

        :param str hashcode: The `md5` hash of the file to use to search for available subtitles.
        :return str: A comma-separated list of available languages (two character language code).

        This method searches the SubDB API for the given subtitles by `hashcode` and returns all available languages
        the subtitle exists in.
        """
        if self._verbose:
            print(
                f'[{self._action_counter}] [SEARCHING] [SUBTITLE] for [HASHCODE] "{hashcode}"\n'
            )
            self._action_counter += 1

        payload = {"action": "search", "hash": hashcode}
        response = self._download(payload=payload)

        return response

    def _download_subtitles(self, language="en", hashcode=None):
        """

        :param str language: The language of the subtitle to download (as a two character language code, i.e., 'en' for English).
        :param str hashcode: The `md5` hash of the file to download the subtitle for.
        :return file: An `.srt` file containing the subtitle for the given file, named `<hashcode>.srt`.

        This method downloads subtitles from the SubDB API, given the specified `hashcode` and `language`.
        """
        if self._verbose:
            print(
                f'[{self._action_counter}] [DOWNLOADING] [SUBTITLE] for [HASHCODE] "{hashcode}"\n'
            )
            self._action_counter += 1

        payload = {"action": "download", "hash": hashcode, "language": language}
        response = self._download(payload=payload)

        return response

    def get_subtitles(self, directory=None, metadata_filename=None, language="en"):
        """

        :param str directory: The movie file directory to download subtitles for.
        :param str metadata_filename: The metadata filename.
        :param str language: The two character language code representing the language to download the subtitle in.
        :return None:
        """
        if directory is None:
            directory = self._directory

        if metadata_filename is None:
            metadata_filename = self._metadata_filename

        full_filepath = os.path.join(directory, metadata_filename)
        if os.path.exists(full_filepath):
            if self._verbose:
                print(f'[{self._action_counter}] [PROCESSING FILE] "{full_filepath}"\n')
                self._action_counter += 1

            # Open file for reading:
            with open(full_filepath, mode="rb") as infile:
                # Load existing data into titles index list:
                titles = json.load(infile)

            for title in titles.get("titles", []):
                title_filename = title.get("title")
                title_folder_path = os.path.join(directory, title_filename)
                subtitle_filename = f"{language}_subtitles.srt"
                subtitle_path = os.path.join(title_folder_path, subtitle_filename)
                movie_file_paths = self._get_movie_file_paths(
                    directory=title_folder_path
                )

                for movie_file_path in movie_file_paths:
                    if self._verbose:
                        print(f'[PROCESSING TITLE] "{title_filename}"\n')

                    if not os.path.exists(subtitle_path):
                        subtitles_available = None
                        hashcode = self._get_hash(filepath=movie_file_path)
                        response = self._search_subtitles(hashcode=hashcode)
                        if response.status_code == 200:
                            subtitles_available = response.text

                        if (
                            subtitles_available not in ["", None, " "]
                            and language in subtitles_available
                        ):
                            if self._verbose:
                                print(
                                    f'[ADDING SUBTITLE FILE] "{language}_subtitles.srt" at [FILEPATH] "{subtitle_path}"\n'
                                )

                            response = self._download_subtitles(
                                language=language, hashcode=hashcode
                            )
                            if response.status_code == 200:
                                subtitles = response.text

                                if self._verbose:
                                    print("[INFO] [DOWNLOAD COMPLETE]\n")
                                    print(
                                        f'[WRITING SUBTITLE FILE] "{language}_subtitles.srt" at [FILEPATH] "{subtitle_path}"\n'
                                    )

                                with open(
                                    subtitle_path, "w+", encoding="UTF-8"
                                ) as outfile:
                                    outfile.writelines(subtitles)
                                    if self._verbose:
                                        print("[WRITE COMPLETE]")
                            else:
                                print(
                                    f'[ERROR] [RESPONSE STATUS CODE] "{response.status_code}".\n'
                                    f'[SUBTITLE] for [MOVIE FILE] "{movie_file_path}" [MAY NOT EXIST]\n'
                                )
                        else:
                            if self._verbose:
                                print(
                                    f'[ERROR] No Subtitles Available for [LANGUAGE] "{language}".\n'
                                )
                    else:
                        print("[INFO] Subtitle already exists. Skipping...\n")

            print("[COMPLETE]")
