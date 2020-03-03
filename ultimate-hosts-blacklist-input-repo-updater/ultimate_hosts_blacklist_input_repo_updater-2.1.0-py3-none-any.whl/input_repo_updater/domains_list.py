"""
The tool to update the input repositories of the Ultimate-Hosts-Blacklist project.

Gets, formats and saves the upstream source.
It basically construct the `domains.list´ file.

License:
::


    MIT License

    Copyright (c) 2019, 2020  Ultimate-Hosts-Blacklist
    Copyright (c) 2019, 2020  Nissar Chababy
    Copyright (c) 2019, 2020  Mitchell Krog

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""
import logging

import PyFunceble

from ultimate_hosts_blacklist.helpers import Download, File

from .config import Outputs
from .exceptions import CouldNotDownload


class DomainsList:
    """
    Get, format and save the upstream source into `domains.list`.
    """

    raw_link = None

    @classmethod
    def __init__(cls, raw_link):
        cls.raw_link = raw_link

    @classmethod
    def get_subject(cls, line):
        """
        Provides the subject to test from the given line.
        """

        return PyFunceble.converter.File(line).get_converted()

    def format_for_engine(self, file, data):
        """
        For the given data into something our infrastructure understand.
        """

        file.write("", overwrite=True)

        for line in data.splitlines():
            line = line.strip()

            if not line:
                continue

            file.write(f"{self.get_subject(line)}\n")

    def generate(self):
        """
        Get the upstream version.
        """

        logging.info("Starting the generation of %s", Outputs.input_destination)

        file = File(Outputs.input_destination)

        if self.raw_link and not Download(self.raw_link, file.file).text():
            raise CouldNotDownload(self.raw_link)

        if file.exists():
            self.format_for_engine(file, file.read())

        logging.info("Finished the generation of %s", Outputs.input_destination)
