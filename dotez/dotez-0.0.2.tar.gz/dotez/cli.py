#!/usr/bin/env python3
from dotez import config
from dotez.core import DotEZ
import argparse


def main():
    parser = argparse.ArgumentParser(description='dotez: manage dotfiles with ease')
    parser.add_argument('--use-conf', type=str, default=None, metavar='conffile',
                        help='Path to a custom file to load configurations from')
    parser.add_argument('--no-push', action='store_true', default=False,
                        help='Do NOT automatically push to remote')
    parser.add_argument('--test', action='store_true', default=False,
                        help='Only print out dotfiles being managed, useful for testing your configurations')
    args = parser.parse_args()
    # load custom conf file if specified
    config.logger.info("Loading configs")
    if args.use_conf is not None:
        dotez = DotEZ([args.use_conf])
    else:
        dotez = DotEZ(config.CONFIG_LOCS)

    # load or init git repo
    config.logger.info("Loading git repo")
    dotez.init_dotez_repo()

    # get files matching the rules
    config.logger.info("Getting a list of dotfiles")
    files = dotez.match_files()

    if args.test:
        dotez.test_config()
        exit(0)

    # commit files if dirty
    config.logger.info("Committing files")
    dirty = dotez.git_commit(files)
    if not dirty:
        config.logger.info("No changed files")

    # push to remote(s)
    if not args.no_push:
        config.logger.info("Pushing to remote(s)")
        dotez.push_remotes()


if __name__ == "__main__":
    main()
