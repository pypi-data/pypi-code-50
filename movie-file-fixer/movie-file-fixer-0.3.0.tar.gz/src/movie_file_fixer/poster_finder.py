# -*- coding: utf-8 -*-
"""

Description: Reads the "titles" section of the `metadata.json` file and downloads the poster for each title.
"""

import json
import os

import requests


class PosterFinder:
    def __init__(
        self, directory=None, metadata_filename="metadata.json", verbose=False
    ):
        self._directory = directory
        self._metadata_filename = metadata_filename
        self._verbose = verbose
        self._action_counter = 0

        if self._verbose:
            print("[CURRENT ACTION: LOCATING MOVIE POSTERS]\n")

    def _download(self, url=None, headers=None):
        """

        :param str url: The URL of a file to download.
        :param dict headers: A dictionary containing custom headers. Default only contains the `User-Agent`.
        :return requests.Response: A `requests.Response` object containing the file being requested.
        """
        if headers is None:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            }

        if self._verbose:
            print(f'[{self._action_counter}] [DOWNLOADING] [FILE] from [URL] "{url}"\n')
            self._action_counter += 1

        return requests.get(url=url, headers=headers)

    def get_posters(self, directory=None, metadata_filename=None):
        """

        :param str directory: The directory containing the metadata file.
        :param str metadata_filename: The metadata filename.
        :return: None

        Downloads all posters specified in the metadata file `titles` section.
        """
        if directory is None:
            directory = self._directory

        if metadata_filename is None:
            metadata_filename = self._metadata_filename

        full_metadata_filepath = os.path.join(directory, metadata_filename)

        if self._verbose:
            print(
                f'[{self._action_counter}] [PROCESSING METADATA] from [FILE] "{full_metadata_filepath}"\n'
            )
            self._action_counter += 1

        # If the metadata file exists:
        if os.path.exists(full_metadata_filepath):
            # Open file for reading:
            with open(full_metadata_filepath, mode="rb") as infile:
                # Load existing data into titles index list:
                metadata_file = json.load(infile)

            # For each title in the metadata file,
            for title in metadata_file["titles"]:
                title_path = os.path.join(directory, title["title"])
                # If the title folder exists
                if os.path.exists(title_path):
                    poster_filepath = os.path.join(
                        directory, title["title"], "poster.jpg"
                    )

                    if self._verbose:
                        print(f'[PROCESSING TITLE] "{title}]"\n')

                    poster_url = title["poster"]

                    if poster_url not in ["", None, " ", "N/A"]:
                        if self._verbose:
                            print(
                                f'[{self._action_counter}] [DOWNLOADING] [POSTER URL] {poster_url}"\n'
                            )
                            self._action_counter += 1

                        response = self._download(url=poster_url)

                        if response.status_code == 200:
                            if self._verbose:
                                print("[DOWNLOAD COMPLETE]\n")
                                print(
                                    f'[{self._action_counter}] [WRITING FILE] -> "{poster_filepath}"\n'
                                )
                                self._action_counter += 1

                            with open(poster_filepath, "wb") as outfile:
                                outfile.write(response.content)
