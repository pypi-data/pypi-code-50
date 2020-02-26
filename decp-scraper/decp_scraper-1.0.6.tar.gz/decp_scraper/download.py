#!/bin/python3
import argparse
import csv
import json
import os
import pathlib
import re
import signal
import sys
import threading
import time
import xml
from datetime import datetime
from os import mkdir
from os.path import isdir
from xml.dom import minidom

import requests as requests
import unidecode as unidecode

if __name__ == "__main__" and __package__ is None:
    __path__ = [str(pathlib.Path(os.path.dirname(__file__)).parent)]
from . import extractionAcheteurs
from .site_utils import get_all_platforms, get_base_url_from_site

XML_HEADER = '<?xml version="1.0" encoding="UTF-8"?>\n'
XML_MARKETS_HEADER = '<marches>\n'
XML_MARKETS_FOOTER = '</marches>\n'
BUYERS_DESCRIPTION_DIR = 'acheteurs'
ROOT_XML_DIR = 'xml'
BUYERS_XML_DIR = 'buyers'
STAT_FILE_PATH = 'disponibilite-donnees.csv'


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


def get_platform_xml_dir(platform):
    return os.path.join(ROOT_XML_DIR, platform)


def create_directory_structure(platform):
    xml_dir = get_platform_xml_dir(platform)
    if not isdir(xml_dir):
        mkdir(xml_dir)
    if not isdir(os.path.join(xml_dir, BUYERS_XML_DIR)):
        mkdir(os.path.join(xml_dir, BUYERS_XML_DIR))


def download_files(platform, years, force=False, delay=0.2):
    platform_xml_dir = get_platform_xml_dir(platform)
    base_url = get_base_url_from_site(platform)
    buyers_file = os.path.join(BUYERS_DESCRIPTION_DIR, platform + '.json')
    if years is None:
        years = get_all_years_available()
    buyers = json.loads(open(buyers_file, 'r').read())
    for buyer in buyers:
        current_thread = threading.current_thread()
        if isinstance(current_thread, StoppableThread) and current_thread.stopped():
            sys.exit('Thread requested to stop, exiting')
        buyer_name = re.sub("[ -./\\\\]+", ' ', unidecode.unidecode(buyer.get('name', None)).lower()).strip().replace(
            ' ', '_')
        buyer_id = buyer.get('id', None)
        if buyer_id is not None:
            time.sleep(delay)
            print('Platform: ' + platform + ' --- downloading buyer: ' + buyer_name)
            for year in years:
                url = base_url + '/app.php/api/v1/donnees-essentielles/contrat/xml-extraire-criteres/' + buyer_id + '/0/1/' + str(
                    year) + '/false/false/false/false/false/false/false/false/false'
                file_path = os.path.join(platform_xml_dir, BUYERS_XML_DIR,
                                         '_'.join([buyer_id, buyer_name, str(year)]) + '.xml')
                print(file_path)
                if not os.path.exists(file_path) or force:
                    pathlib.Path(file_path).touch()
                    with requests.get(url, verify=False) as response, open(file_path, 'wb') as out_file:
                        out_file.write(response.content)


def get_all_years_available():
    return [index + 2018 for index in range(datetime.now().year - 2018 + 1)]


def merge_files(platform, output_file=None):
    stat_file = open(STAT_FILE_PATH, 'a')
    writer_stats = csv.writer(stat_file, delimiter=',')
    date_as_str = datetime.strftime(datetime.now(), '%Y-%m-%dT%H:%M:%S')
    shall_add_footer = False
    if output_file is None:
        shall_add_footer = True
        output_file = open(os.path.join(get_platform_xml_dir(platform), platform + '.xml'), 'w')
        output_file.write(XML_HEADER)
        output_file.write(XML_MARKETS_HEADER)
    buyers_xml_dir = os.path.join(get_platform_xml_dir(platform), BUYERS_XML_DIR)
    for root, dirs, files in os.walk(buyers_xml_dir):
        for file in files:
            if file.split('.')[-1] == 'xml':
                name_components = '.'.join(file.split('.')[:-1]).split('_')
                buyer_id = name_components[0]
                buyer_name = '_'.join(name_components[1:-1])
                year_as_str = name_components[-1]
                row = [platform, buyer_name, year_as_str, 0, date_as_str]
                try:
                    dom = minidom.parse(os.path.join(root, file))
                    markets = dom.getElementsByTagName('marches')
                    nb_of_markets = 0
                    for market_group in markets:
                        nb_of_markets_in_current_group = len(market_group.getElementsByTagName('marche'))
                        if nb_of_markets_in_current_group > 0:
                            nb_of_markets += nb_of_markets_in_current_group
                            markets = market_group.getElementsByTagName('marche')
                            for market in markets:
                                output_file.writelines('  ' + market.toxml() + '\n')
                    row[3] = nb_of_markets
                except xml.parsers.expat.ExpatError:
                    row[3] = 'error'
                finally:
                    writer_stats.writerow(tuple(row))
    if shall_add_footer:
        output_file.write(XML_MARKETS_FOOTER)


def merge_all_files(platforms=None):
    if platforms is None:
        platforms = list(get_all_platforms().keys())
    open(os.path.join(ROOT_XML_DIR, 'multiple_platforms.xml'), 'w').close()
    open(STAT_FILE_PATH, 'w').close()
    output_file = open(os.path.join(ROOT_XML_DIR, 'multiple_platforms.xml'), 'a')
    output_file.write(XML_HEADER)
    output_file.write(XML_MARKETS_HEADER)
    for platform in platforms:
        merge_files(platform, output_file)
    output_file.write(XML_MARKETS_FOOTER)


def main(argv):
    force, platforms, years, thread_number, delay, should_initialize = parse_and_build_arguments(argv)
    collects_multiple_platforms_data(platforms, years, force, thread_number, delay, should_initialize)


def collects_multiple_platforms_data(platforms, years, force=False, thread_number=1, delay=0.2, should_initialize=False):
    if should_initialize:
        print('Initializing data')
        extractionAcheteurs.extract_buyer_information_for_multiple_platform(platforms)
    signal.signal(signal.SIGINT, signal_handler)
    thread_active_count = threading.active_count() - 1
    available_threads = max(0, thread_number - thread_active_count)
    for platform in platforms:
        while available_threads < 1:
            time.sleep(1)
            thread_active_count = threading.active_count() - 1
            available_threads = max(0, thread_number - thread_active_count)
        new_thread = StoppableThread(target=collect_platform_data, args=[platform, years, force, delay])
        new_thread.start()
        available_threads -= 1
    merge_all_files(platforms)


def collect_platform_data(platform, years, force=False, delay=0.2):
    print('Starting data capture for platform :' + platform)
    base_url = get_base_url_from_site(platform)
    if base_url is not None:
        print('Base URL found in config: ' + base_url)
        xml_dir = get_platform_xml_dir(platform)
        create_directory_structure(platform)
        download_files(platform, years, force, delay)
    merge_files(platform)


def parse_and_build_arguments(argv):
    possible_sites = list(get_all_platforms().keys())
    parser = argparse.ArgumentParser(
        description='Download DECP files from chosen ATEXO powered tender websites: '+str(possible_sites+['all']),
        epilog="Download with politeness (late schedule and low speed), those sites are public services. You download at your own risks and responsibility.")
    parser.add_argument('program', help='Default program argument in case files is called from Python executable')
    parser.add_argument('-s', '--site', nargs='+', required=True,
                        help='Specify the site you wish to download DECP from')
    parser.add_argument('-y', '--year', required=False, type=int,
                        help='Specify the year you wish to download the DECP for. Should be an int >=2018')
    parser.add_argument('-f', '--force_download', action='store_true',
                        help='Specify that you want to download the files even if you have them already to get fresh content, default is to no re-download')
    parser.add_argument('-d', '--delay', type=int, default=0.2,
                        help='Specify that you want to set some delay between calls, default to 0.2s')
    parser.add_argument('-t', '--thread_number', type=int, default=1,
                        help='Specify that you want to use a specific number of threads to speed up the process for multi-site capture, default is one thread')
    parser.add_argument('-i', '--init', action='store_true',
                        help='Specify that you want to initialize your local files, default is to not initialize')
    arguments = vars(parser.parse_args(argv))
    platforms = arguments.get('site', [])
    year_str = arguments.get('year', None)
    force = arguments.get('force_download')
    thread_number = arguments.get('thread_number', 1)
    delay = arguments.get('delay', 0.2)
    years = get_years_to_collect(year_str)
    should_initialize = arguments.get('init')
    base_url = None
    if platforms is not None:
        if 'all' in platforms:
            platforms = possible_sites
    return force, platforms, years, thread_number, delay, should_initialize


def get_years_to_collect(year_str):
    years = None
    if year_str is not None:
        year = int(year_str)
        try:
            assert year >= 2018
            years = [year]
        except AssertionError as e:
            exit('Stopping: Argument --year must be an integer year after or equal to 2018')
    return years


def signal_handler(sig, frame):
    print('You pressed Ctrl+C, killing all threads')
    threads = threading.enumerate()
    for thread in threads:
        if isinstance(thread, StoppableThread):
            thread.stop()
    sys.exit(0)


if __name__ == '__main__':
    main(sys.argv)
