#!/usr/bin/python
# -*- coding: utf-8 -*-

__copyright__ = """

    Copyright 2019 Samapriya Roy

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

"""
__license__ = "Apache 2.0"

import requests
import os
import csv
import sys
import getpass
import argparse, time
from prettytable import PrettyTable
from os.path import expanduser

x = PrettyTable()

main_url='https://zenodo.org'
sandbox_url='https://sandbox.zenodo.org'

# Save Zenodo Token Key
def zenpass():
    token = getpass.getpass("Enter Zenodo Access Token: ")
    with open(os.path.join(expanduser("~"), ".zkey"), "w") as apkey:
        apkey.write(token)
    apkey.close()


def zenpass_from_parser(args):
    zenpass()


# Print or export depositions you made
def deposits(outfile,title,mode):
    if mode is None:
        url=main_url
    elif mode=='sandbox':
        url=sandbox_url
    if outfile is not None:
        with open(outfile, "w") as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=[
                    "Item DOI",
                    "DOI url",
                    "Filename",
                    "Release version",
                    "Publication Date",
                    "Access Right",
                    "Download Link",
                    "Creator",
                    "Create Date",
                ],
                delimiter=",",
                lineterminator="\n",
            )
            writer.writeheader()
    i = 1  # Set records counter
    fname = os.path.join(os.path.expanduser("~"), ".zkey")
    if os.path.exists(fname):
        with open(fname, "r") as fp:
            ACCESS_TOKEN = fp.read().strip()
    headers = {"Content-Type": "application/json"}
    if title is not None:
        params={"q": title,"size": 200, "access_token": ACCESS_TOKEN}
    else:
        params={"q": [],"size": 200, "access_token": ACCESS_TOKEN}
    r = requests.get(
        url+'/api/deposit/depositions',
        params=params,
        json={},
        headers=headers,
    )
    if r.status_code == 200:
        for items in r.json():
            try:
                latest_url = items["links"]["latest"]
                resp = requests.get(
                    latest_url,
                    params={"access_token": ACCESS_TOKEN},
                    json={},
                    headers=headers,
                ).json()
                print('Getting Zenodo records : '+str(i),end='\r')
                badge = str(resp["links"]["badge"])
                doi = str(resp["doi"])
                doi_url = str(resp["links"]["doi"])
                filename = str(resp["files"][0]["key"]).split("/")[-1]
                version = str(resp["metadata"]["version"])
                pubdate = str(resp["metadata"]["publication_date"])
                right = str(resp["metadata"]["access_right"])
                download_url = str(resp["files"][0]["links"]["self"])
                creator = str(resp["metadata"]["creators"][0]["name"])
                created = str(resp["created"]).split("T")[0]
                updated = str(resp["updated"]).split("T")[0]
                if outfile is not None:
                    with open(outfile, "a") as csvfile:
                        writer = csv.writer(csvfile, delimiter=",", lineterminator="\n")
                        writer.writerow(
                            [
                                doi,
                                doi_url,
                                filename,
                                version,
                                pubdate,
                                right,
                                download_url,
                                creator,
                                created,
                            ]
                        )
                    csvfile.close()
                else:
                    x.field_names = [
                        "DOI",
                        "DOI link",
                        "filename",
                        "release version",
                        "created",
                    ]
                    x.add_row([doi, doi_url, filename, version, created])
                i = i + 1
            except Exception as e:
                print(e)
                print("")
        if outfile is None:
            print(x)
    elif mode is not None and r.status_code==401:
        print('Set Zen Token for Sandbox')
    else:
        print("Failed with response code: " + str(r.status_code))
        print(r.text)


def deposits_from_parser(args):
    deposits(title=args.title,outfile=args.file,mode=args.mode)


def main(args=None):
    parser = argparse.ArgumentParser(description="Ordersv2 Simple Client")
    subparsers = parser.add_subparsers()

    parser_zenpass = subparsers.add_parser(
        "zenpass", help="Setup and store your Zenodo Token"
    )
    parser_zenpass.set_defaults(func=zenpass_from_parser)

    parser_deposits = subparsers.add_parser(
        "deposits", help="Print or export all your Zenodo deposits"
    )
    optional_named = parser_deposits.add_argument_group("Optional named arguments")
    optional_named.add_argument(
        "--title", help="Search by title name", default=None
    )
    optional_named.add_argument(
        "--file", help="Output file to export Zenodo deposits records", default=None
    )
    optional_named.add_argument(
        "--mode", help="Choose sandbox if you want to work in Zenodo sandbox", default=None
    )
    parser_deposits.set_defaults(func=deposits_from_parser)
    args = parser.parse_args()

    try:
        func = args.func
    except AttributeError:
        parser.error("too few arguments")
    func(args)


if __name__ == "__main__":
    main()
