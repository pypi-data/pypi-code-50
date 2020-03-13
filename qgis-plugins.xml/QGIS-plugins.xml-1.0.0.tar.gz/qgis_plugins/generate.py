# -*- coding: utf-8 -*-

# Copyright (c) 2011-2014, Camptocamp SA
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies,
# either expressed or implied, of the FreeBSD Project.


import argparse
import os
import re
import sys
from datetime import datetime
from glob import glob
from configparser import RawConfigParser
from jinja2 import Environment

TEMPLATE_STRING = u"""<?xml version = '1.0' encoding = 'UTF-8'?>
<!--?xml-stylesheet type="text/xsl" href="http://qgis.camptocamp.net/plugins/plugins.xsl" ?-->
<plugins>
{% for metadata in metadatas %}
    <pyqgis_plugin name="{{ metadata["name"] }}" version="{{ metadata["version"] }}">
        <description><![CDATA[{{ metadata["description"] }}]]></description>
        <about><![CDATA[{{ metadata["about"] }}]]></about>
        <version>{{ metadata["version"] }}</version>
        <qgis_minimum_version>{{ metadata["qgisminimumversion"] }}</qgis_minimum_version>
        <qgis_maximum_version>{{ metadata["qgismaximumversion"] }}</qgis_maximum_version>
        <homepage><![CDATA[{{ metadata["homepage"] }}]]></homepage>
        <file_name>{{ metadata["filename"] }}</file_name>
        <icon>{{ metadata["icon"] }}</icon>
        <author_name><![CDATA[{{ metadata["author"] }}]]></author_name>
        <download_url>{{ metadata["download_url"] }}</download_url>
        <uploaded_by><![CDATA[{{ metadata["uploaded_by"] }}]]></uploaded_by>
        <create_date>{{ metadata["create_date"] | datetimeformat }}</create_date>
        <update_date>{{ metadata["update_date"] | datetimeformat }}</update_date>
        <experimental>{{ metadata["experimental"] }}</experimental>
        <deprecated>{{ metadata["deprecated"] }}</deprecated>
        <tracker><![CDATA[{{ metadata["tracker"] }}]]></tracker>
        <repository><![CDATA[{{ metadata["repository"] }}]]></repository>
        <tags><![CDATA[{{ metadata["tags"] }}]]></tags>
        <downloads></downloads>
        <average_vote></average_vote>
        <rating_votes></rating_votes>
   </pyqgis_plugin>
{% endfor %}
</plugins>
"""


def datetimeformat(item):
    return "" if item is None else item.isoformat()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to folder or .zip file")
    parser.add_argument("url", help="Url of the QGIS plugin repository")
    args = parser.parse_args()
    path = args.path
    url = args.url

    # Initialize Jinja2 environment
    environment = Environment()
    environment.filters['datetimeformat'] = datetimeformat
    template = environment.from_string(TEMPLATE_STRING)

    if not os.path.exists(path):
        raise Exception("{} does not exists.".format(path))

    if os.path.isdir(path):
        metadatas = []
        for dirpath, dirnames, filenames in os.walk(path):
            visitor(dirpath, metadatas, url)
        output_folder = path

    if os.path.isfile(path):
        plugin_file = path
        metadata_file = os.path.join(os.path.dirname(path), "metadata.txt")
        metadatas = [plugin_metadata(metadata_file, plugin_file, url)]
        output_folder = os.path.dirname(plugin_file)

    result = template.render(metadatas=metadatas)

    with open(os.path.join(output_folder, "plugins.xml"), "wt") as file_open:
        file_open.write(result)


def visitor(directory, metadatas, url):
    for metadata_file in glob("%s/*.txt" % directory):
        split_file = metadata_file.split(".")
        split_file[-1] = "zip"
        plugin_path = ".".join(split_file)
        metadatas.append(plugin_metadata(metadata_file, plugin_path, url))


def plugin_metadata(metadata_file, plugin_path, url):
    # Create dictionary with some default values
    metadata = {
        "qgismaximumversion": "",
        "about": "",
        "changelog": "",
        "experimental": False,
        "deprecated": False,
        "tags": "",
        "homepage": "",
        "repository": "",
        "tracker": "",
        "icon": "",
        "category": "",
        "uploaded_by": "",
        "create_date": None,
        "average_vote": "",
        "rating_votes": "",
    }

    # Read metadata from the plugin
    parser = RawConfigParser()
    parser.read(metadata_file)

    for key, value in parser.items("general"):
        metadata[key] = value

    qgisminimumversion = metadata["qgisminimumversion"].split(".")
    while len(qgisminimumversion) < 3:
        qgisminimumversion.append("0")
    metadata["qgisminimumversion"] = ".".join(qgisminimumversion)

    qgismaximumversion = metadata.get(
        "qgismaximumversion",
        "{}.99".format(qgisminimumversion[0])).split(".")
    while len(qgismaximumversion) < 3:
        qgismaximumversion.append("0")
    metadata["qgismaximumversion"] = ".".join(qgismaximumversion)

    # Set update_date to archive modification date
    metadata["update_date"] = datetime.fromtimestamp(
        os.path.getmtime(plugin_path)
    )

    metadata["download_url"] = os.path.join(url, os.path.basename(plugin_path))

    metadata["filename"] =  os.path.basename(plugin_path)

    return metadata
