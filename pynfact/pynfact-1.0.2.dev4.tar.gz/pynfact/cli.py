#!/usr/bin/env python3
# vim: set ft=python fileencoding=utf-8 tw=72 fdm=indent nowrap:
"""
    pynfact.cli
    ~~~~~~~~~~~

    Command line interface.

    :copyright: (c) 2012-2020, J. A. Corbal
    :license: MIT
"""
from pynfact.builder import Builder
from pynfact.server import Server
from pynfact.yamler import Yamler
import os
import shutil
import sys


try:
    import colored_traceback.auto
    colored_traceback.add_hook(always=True)
except ImportError:
    pass


def main():
    default_post_ext = '.md'  # .mkdn, .markdown,...

    if len(sys.argv) >= 2:
        action = sys.argv[1]
    else:
        action = "help"

    if action == "init" or action == "new":
        real_path = os.path.dirname(os.path.realpath(__file__))
        src = os.path.join(real_path, 'initnew')
        dst = 'pynfact_blog' if len(sys.argv) < 3 else sys.argv[2]

        # create new blog structure with the default values
        try:
            shutil.copytree(src, dst)
        except OSError as exc:
            sys.exit("pynfact.cli.main: cannot make blog structure")

    elif action == "help":
        print("  $ pynfact init [<site>]. Creates new empty site")
        print("  $ pynfact build......... Builds site")
        print("  $ pynfact serve......... Testing server")
        print("  $ pynfact help.......... Displays this awesome help")

    elif action == "serve":
        port = 4000 if len(sys.argv) < 3 else int(sys.argv[2])
        server = Server(port=port, verbose=True)
        server.serve()

    elif action == "build":
        config_file = 'config.yml' if len(sys.argv) < 3 else sys.argv[2]
        config = Yamler(config_file)

        # Get config
        site_config = {
            'uri': {
                'base': config.retrieve('base_uri', '').strip('/'),
                'canonical': config.retrieve('canonical_uri', '').rstrip('/'),
            },
            'wlocale': {
                'encoding': config.retrieve('encoding', 'utf-8'),
                'locale': config.retrieve('locale', 'en_US.UTF-8'),
                'language': config.retrieve('site_language', 'en'),
            },
            'date_format': {
                'entry': config.retrieve('datefmt_entry', "%c"),
                'home': config.retrieve('datefmt_home', "%b %_d, %Y"),
                'list': config.retrieve('datefmt_list', "%Y-%m-%d"),
            },
            'info': {
                'author': config.retrieve('author', "Nameless"),
                'email': config.retrieve('author_email', ''),
                'copyright': config.retrieve('site_copyright'),
                'site_name': config.retrieve('site_name', "My Blog"),
                'site_description': config.retrieve('site_description'),
            },
            'presentation': {
                'comments': config.retrieve('comments').lower() == "yes",
                'default_category':
                    config.retrieve('default_category', "Miscellaneous"),
                'feed_format': config.retrieve('feed_format', "atom"),
                'max_entries': config.retrieve('max_entries', 10),
            },
            'dirs': {
                'deploy': "_build",
                'extra': config.retrieve('extra_dirs')
            }
        }

        # Prepare builder
        template_values = { 'blog': {
            'author': site_config['info']['author'],
            'base_uri': site_config['uri']['base'],
            'encoding': site_config['wlocale']['encoding'],
            'feed_format': site_config['presentation']['feed_format'],
            'lang': site_config['wlocale']['language'],
            'site_name': site_config['info']['site_name'],
        } }

        # Build
        b = Builder(site_config, template_values,
                infile_ext=default_post_ext, verbose=True)
        b.gen_site()


## Main entry
if __name__ == "__main__":
    main()

