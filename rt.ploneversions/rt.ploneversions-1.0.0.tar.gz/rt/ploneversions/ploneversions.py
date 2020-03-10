# -*- coding: utf-8 -*-
import argparse
import sys
from configparser import RawConfigParser, NoOptionError, NoSectionError
from urllib.error import HTTPError
from urllib.request import urlopen

VERSION_URL_TEMPLATE = "https://dist.plone.org/release/%s/versions.cfg"

parser = argparse.ArgumentParser(description='Plone version pinning')


def merge_versions(v1, v2):
    ''' Merge the versions from v1 with the ones from v2
    '''
    v1 = dict(v1)
    v2 = dict(v2)
    v2.update(v1)
    return [(x, y) for x, y in v2.items()]


def sort_versions(v):
    ''' Return the versions sorted
    '''
    v.sort(key=lambda x: x[0])
    return v


class CFGParser(RawConfigParser):

    ''' Parse a URL
    '''
    _url = ''
    _version = ''

    optionxform = str

    def __init__(self, url):
        ''' Initialize our object

        :param version: a string like 4.3.1
        '''
        RawConfigParser.__init__(self)
        self._url = url
        self.urlfp = urlopen(self._url)
        self.read_string(self.urlfp.read().decode())

    def get_extends_urls(self):
        ''' Get the extends from the buildout
        '''
        try:
            option = self.get('buildout', 'extends').strip()
        except (NoOptionError, NoSectionError):
            return []
        base_url = self._url.rpartition("/")[0]
        urls = []
        for line in option.splitlines():
            line = line.strip()
            if not "://" in line and not line.startswith("file:"):
                line = "/".join((base_url, line.strip()))
            urls.append(line)
        return list(reversed(urls))

    def get_versions(self):
        ''' Get's the versions from this file
        '''
        return self.items('versions')

    def get_merged_versions(self):
        ''' Get's the versions merged according to the extends
        '''
        urls = self.get_extends_urls()
        composed = [(self._url, self.get_versions())]
        for url in urls:
            cfg = CFGParser(url)
            composed.extend(cfg.get_merged_versions())
        return composed

    def __call__(self):
        ''' Calling This will output versions to the stdout
        '''
        merged_versions = self.get_merged_versions()
        merged_versions.reverse()
        for url, versions in merged_versions:
            print(f"## {url}")
            for key, value in versions:
                print(f"{key} = {value}")
            print()


class PloneCFGParser(CFGParser):

    ''' Parse a URL from dist.plone.org
    '''
    _version = ''

    def __init__(self, version):
        ''' Initialize our object

        :param version: a string like 4.3.1
        '''
        self._version = version
        CFGParser.__init__(self, VERSION_URL_TEMPLATE % version)


def main(return_tagdir=False):
    """ This will try to fetch versions from dist.plone.org
    """
    try:
        version = sys.argv[1]
    except IndexError:
        print("""
Usage: ploneversions X.Y.X

Check available Plone versions at:
 - https://dist.plone.org/release
""")
        return
    try:
        return PloneCFGParser(sys.argv[1])()
    except HTTPError:
        print(f"ERROR: Cannot resolve Plone version {sys.argv[1]}")
        sys.exit(1)
