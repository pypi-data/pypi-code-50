#!/usr/bin/env python

import argparse
import os
import sys
import select

import hiyapyco

from conans.client.cache import cache
from conans.client.output import ConanOutput
from conans.paths import get_conan_user_home
from conans.util.files import normalize


def bool_arg(parser, arg, default=None):
    parser.add_argument('--' + arg, dest=arg, action='store_true')
    parser.add_argument('--no-' + arg, dest=arg, action='store_false')
    parser.set_defaults(**{arg: default})


def get_stdin():
    return sys.stdin.read() \
        if select.select([sys.stdin, ], [], [], 0.0)[0] \
        else None


def default_settings():
    if hasattr(cache, 'default_settings_yml'):
        # pre conan 1.23
        return cache.default_settings_yml
    elif hasattr(cache, 'get_default_settings_yml'):
        # conan 1.23 an later
        return cache.get_default_settings_yml()
    else:
        raise Exception('Unsupported version of Conan. Please report to issue tracker, with details about the version.')


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Modify Conan settings.yml configuration')
    parser.add_argument('--merge-file', nargs='*', default=[], help='YAML config file to merge')
    parser.add_argument('--method', default='METHOD_MERGE')
    bool_arg(parser, 'mergelists', True)
    bool_arg(parser, 'interpolate', False)
    bool_arg(parser, 'castinterpolated', False)
    bool_arg(parser, 'usedefaultyamlloader', False)
    bool_arg(parser, 'failonmissingfiles', True)
    args = parser.parse_args()

    in_data = get_stdin() or ''
    in_data += "\n"  # newline is used to distinguish yaml from filename

    output = ConanOutput(sys.stdout, sys.stderr, True)
    conan_cache = cache.ClientCache(os.path.join(get_conan_user_home(), '.conan'), output)
    path = conan_cache.settings_path

    existing = cache.load(path) \
        if os.path.exists(path) \
        else default_settings()
    method = hiyapyco.METHODS[args.method]
    settings = hiyapyco.load(
        [existing, in_data],
        *args.merge_file,
        mergelists=args.mergelists,
        method=method,
        interpolate=args.interpolate,
        castinterpolated=args.castinterpolated,
        usedefaultyamlloader=args.usedefaultyamlloader,
        failonmissingfiles=args.failonmissingfiles)
    settings_yml = hiyapyco.dump(settings)
    cache.save(path, normalize(settings_yml), only_if_modified=True)


if __name__ == '__main__':
    main()
