"""Analysis-related classes and enumerations."""

import copy
import datetime
import gzip
import os
import pathlib
import re
import sys
import typing

from . import decorate, exceptions
from .trace import trace


class File:
    # pylint: disable=missing-class-docstring
    def __init__(self, name: str, size: int, date: datetime.datetime):
        self.name = name
        self.size = size
        self.date = date


class Analysis:
    """Access XRA-31 capture files."""
    def __init__(self, xra31):
        self.xra31 = xra31

        self._files = {}

    def __add_folder(self, path: str, contents: dict):
        strip = len("/mnt/data/captures")
        relative_path = path[strip:].strip('/')
        if relative_path not in self._files:
            self._files[relative_path] = []
            for file_folder in contents:
                if "isFolder" in file_folder and file_folder["isFolder"]:
                    self.__add_folder(file_folder["path"],
                                      file_folder["contents"])
                else:
                    self._files[relative_path].append(
                        File(
                            file_folder["name"], file_folder["size"],
                            datetime.datetime.strptime(
                                file_folder["date"], "%Y-%m-%dT%H:%M:%S.%fZ")))

    def __update(self):
        response = self.xra31.session.get(self.xra31.url_api +
                                          "/analyse/files",
                                          timeout=self.xra31.timeout)
        response.raise_for_status()
        response_json = response.json()

        self._files.clear()
        self.__add_folder(response_json["path"], response_json["contents"])

    def __get_files(self,
                    directory: str,
                    filename: str,
                    rolling: bool,
                    output: str = ""
                    ) -> typing.Tuple[str, typing.List[File], str]:
        if not filename:
            directory = self.xra31.capture.output.directory
            filename = self.xra31.capture.filename
        elif not directory:
            directory = ""
        directory = directory.strip('/')

        # strip file extension if present
        filename = re.sub("(.pcap)?$", "", filename)
        # strip rolling file numbering
        filename_base = re.sub("(_[0-9]+)?$", "", filename)
        # matching pattern
        filename_pattern = re.compile("^{}_[0-9]+.pcap$".format(
            filename_base)) if rolling else re.compile(
                "^{}.pcap$".format(filename))

        self.__update()
        all_files = copy.deepcopy(self._files)

        if directory not in all_files:
            raise exceptions.Xra31FileNotFoundException(
                "Could not find directory " + directory)

        files = []
        files = sorted((file for file in all_files[directory]
                        if filename_pattern.match(file.name)),
                       key=lambda file: file.date.timestamp())
        if not files:
            raise exceptions.Xra31FileNotFoundException(
                "Could not find file " + directory + "/" +
                filename_pattern.pattern.strip("^$"))

        if not output:
            output = (filename_base if rolling else filename)
        output = re.sub("(.pcap)?(.gz)?$", "", output)

        return (directory, files, output)

    @decorate.translate_requests
    @trace
    def delete(self,
               directory: str = None,
               filename: str = None,
               *,
               rolling: bool = False,
               verbose: bool = False):
        """Remove a capture file or rolling file capture from the XRA-31.
        If no filename is given, remove the latest capture.
        In case of a rolling file capture (``rolling`` is ``True``), the full
        collection of files will be removed.

        :param directory: Directory on the XRA-31.
        :type directory: str, optional
        :param filename: Filename on the XRA-31.
        :type filename: str, optional
        :param rolling: Remove all files related to a rolling file capture.
        :type rolling: bool, optional
        :param verbose: Show progress.
        :type verbose: bool, optional
        """
        directory, files, _ = self.__get_files(directory, filename, rolling)

        for file in files:
            path = "/mnt/data/captures/" + directory + '/' + file.name
            if verbose:
                sys.stdout.write("Deleting {}/{}{}".format(
                    directory, file.name, os.linesep))
            response = self.xra31.session.delete(self.xra31.url_api +
                                                 "/analyse/file",
                                                 params={"path": path},
                                                 timeout=self.xra31.timeout)
        response.raise_for_status()

    @decorate.translate_requests
    @trace
    def download(self,
                 directory: str = None,
                 filename: str = None,
                 output: str = None,
                 *,
                 rolling: bool = False,
                 append: bool = False,
                 compress: bool = False,
                 verbose: bool = False) -> None:
        """Download a capture file or rolling file capture from the XRA-31.
        If no filename is given, download the latest capture.
        In case of rolling file capture (``rolling`` is ``True``), the full
        collection of files is downloaded and
        concatenated to a single capture file.

        :param directory: Directory on the XRA-31.
        :type directory: str, optional
        :param filename: Filename on the XRA-31.
        :type filename: str, optional
        :param output: Filename for local storage,
                       defaults to the filename on the XRA-31.
        :type output: str, optional

        :param rolling: Indicate whether the full collection of files in a
                        rolling file capture should be downloaded and
                        concatenated.
        :type rolling: bool, optional
        :param append: Append to an existing file.
        :type append: bool, optional
        :param compress: Compress the file(s) locally (gzip).
        :type compress: bool, optional
        :param verbose: Show progress.
        :type verbose: bool, optional
        """

        CHUNK_SIZE = 10485760  # pylint: disable=invalid-name

        mode = 'wb' if not append else 'ab'

        directory, files, output = self.__get_files(directory, filename,
                                                    rolling, output)

        if compress:
            output = output + ".pcap.gz"
        else:
            output = output + ".pcap"
        local_path = pathlib.Path(output)
        if append and not local_path.is_file():
            append = False

        with (open(str(local_path), mode) if not compress else gzip.open(
                str(local_path), mode, compresslevel=5)) as pcap_file:
            skip_header = append
            for file in files:
                path = "/mnt/data/captures/" + directory + '/' + file.name
                response = self.xra31.session.get(self.xra31.url_api +
                                                  "/analyse/file",
                                                  params={"path": path},
                                                  stream=True,
                                                  timeout=self.xra31.timeout)
                response.raise_for_status()

                if verbose:
                    sys.stdout.write("Downloading {} to {}: ".format(
                        file.name, local_path))

                size = 0
                done = 0
                if verbose:
                    if "content-length" in response.headers:
                        size = int(response.headers["content-length"])
                    else:
                        size = file.size

                    if size:
                        sys.stdout.write("{: 3}%".format(0))
                    else:
                        sys.stdout.write("-")

                first_chunk = True
                for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                    if skip_header and first_chunk:
                        pcap_file.write(chunk[24:])
                    else:
                        pcap_file.write(chunk)
                    if verbose:
                        if size:
                            done += len(chunk)
                            sys.stdout.write("\b\b\b\b{: 3}%".format(
                                round(100. * done / size)))
                        else:
                            done += 1
                            sys.stdout.write('\b' + "-\\|/" [done % 4])
                        sys.stdout.flush()
                    first_chunk = False
                if verbose:
                    sys.stdout.write(os.linesep)
                skip_header = True
