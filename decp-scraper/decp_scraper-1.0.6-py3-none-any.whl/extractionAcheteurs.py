import argparse
import json
import os
import pathlib
import sys

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__" and __package__ is None:
    __path__ = [str(pathlib.Path(os.path.dirname(__file__)).parent)]
from .site_utils import get_all_platforms, get_base_url_from_site

HTML_PAGE_PER_PLATFORM = {}
JSON_BUYER_LIST_PER_PLATFORM = {}


def get_html_file_url(platform):
    return get_base_url_from_site(platform) + '/?page=entreprise.EntrepriseRechercherListeMarches'


def get_json_path(platform):
    return 'acheteurs/' + platform + '.json'


def extract_buyers(platform):
    global HTML_PAGE_PER_PLATFORM
    if os.path.exists(get_html_file_path(platform)):
        html_file = open(get_html_file_path(platform), 'rb')
        html_text = html_file.read()
        HTML_PAGE_PER_PLATFORM[platform] = html_text
    else:
        html_text = HTML_PAGE_PER_PLATFORM[platform]
    soup = BeautifulSoup(html_text, 'html.parser')
    drop_down = soup.find_all('select', id='ctl0_CONTENU_PAGE_organismeAcronyme')
    options = drop_down[0].find_all('option')
    buyers = []
    for option in options[1:]:
        id = option.get('value')
        name = str(option.string).strip()
        buyers.append({'id': id, 'name': name})
    return buyers


def main(argv):
    arguments = parse_args(argv)
    site = arguments.get('site')
    platforms = None
    if site is not None:
        platforms = [site]
    extract_buyer_information_for_multiple_platform(platforms)


def extract_buyer_information_for_multiple_platform(platforms):
    if platforms is not None:
        if 'all' in platforms:
            platforms = list(get_all_platforms().keys())
        for platform in platforms:
            extract_buyer_information(platform)
    else:
        print("ID de plateforme $plateforme introuvable.")


def extract_buyer_information(platform):
    global HTML_PAGE_PER_PLATFORM, JSON_BUYER_LIST_PER_PLATFORM
    if not os.path.exists(get_json_path(platform)):
        print('Starting buyer extraction :' + platform)
        base_url = get_base_url_from_site(platform)
        if base_url is not None:
            print('Base URL found in config: ' + base_url)
            html_file_url = get_html_file_url(platform)
            html_file_path = get_html_file_path(platform)
            if not os.path.exists(html_file_path):
                print('Downloading HTML file')
                with requests.get(html_file_url, verify=False) as response, open(html_file_path, 'wb') as out_file:
                    HTML_PAGE_PER_PLATFORM[platform] = response.content
                    out_file.write(response.content)
            buyers = extract_buyers(platform)
            JSON_BUYER_LIST_PER_PLATFORM[platform] = buyers
            with open(get_json_path(platform), 'w', encoding='utf-8') as json_file:
                json.dump(buyers, json_file, ensure_ascii=False, indent=2)


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description='Download buyers and corresponding code from chosen ATEXO powered tender websites',
        epilog="Now, let's have fun !")
    parser.add_argument('program', help='Default program argument in case files is called from Python executable')
    parser.add_argument('--site', required=True)
    arguments = vars(parser.parse_args(argv))
    return arguments


def get_html_file_path(platform):
    file_path = 'html/' + platform + '.html'
    return file_path


if __name__ == '__main__':
    main(sys.argv)
