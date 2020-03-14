#!/usr/bin/env python3
from dotez import config
from typing import List
import json
import os
import shutil
from git import Repo
import argparse
from pathlib import PurePath
import glob

globals = {
    'repo_dir': '',
    'home': '',
}


def read_config(config_locs: List[str]) -> dict:
    found = False
    # default config here
    conf = config.DEFAULT_CONFIG
    for config_loc in config_locs:
        config_loc = os.path.expandvars(config_loc)
        config_loc = os.path.expanduser(config_loc)
        if os.path.isfile(config_loc):
            found = True
            try:
                with open(config_loc) as f:
                    conf.update(json.load(f))
                    config.logger.info("Using {} as configuration".format(config_loc))
                    break
            except Exception as e:
                config.logger.warn(
                    "Invalid configuration file at: {}\n\tError message: {}\n\tTrying the next one".format(
                        config_loc, str(e)))
        else:
            config.logger.info("Configuration not found at {}".format(config_loc))
    if not found:
        config.logger.error("Cannot find a valid configuration file")
        exit(1)
    return conf


def init_dotez_repo(conf: dict) -> Repo or None:
    # initialize some abspath
    home = os.path.expanduser('~')
    repo_dir = os.path.expandvars(conf['dotez_data_dir'])
    repo_dir = os.path.expanduser(repo_dir)
    globals['repo_dir'] = repo_dir
    globals['home'] = home

    # init or load the repo
    repo = None
    if not os.path.isdir(repo_dir):
        config.logger.info("No existing dotez data directory, creating a new one...")
        try:
            os.mkdir(repo_dir)
            repo = Repo.init(repo_dir)
        except Exception as e:
            config.logger.error("Cannot create git repo at: '" + repo_dir + "'. Error message: {0}".format(e))
            exit(1)
    else:
        if os.path.exists(os.path.join(repo_dir, '.git')):
            repo = Repo(repo_dir)
        else:
            repo = Repo.init(repo_dir)
    return repo


def wildcard_match(pattern: str, input_: str) -> bool:
    pattern = os.path.join(globals['home'], pattern)
    return PurePath(input_).match(pattern)


def match_files(conf: dict, repo: Repo) -> List[str]:
    files: List[str] = []
    includes: List[str] = []
    # match includes
    for f in conf['includes']:
        includes += glob.glob(os.path.join(globals['home'], f))

    # check whether files are ignored, if so, override include rules
    for f in includes:
        # ~ is expanded, but we are undoing it to get shorter names of links
        f = str(PurePath(f).relative_to(globals['home']))
        ignored = False
        for p in conf['ignores']:
            if wildcard_match(p, f):
                ignored = True
                break
        if ignored:
            continue
        link_name = os.path.join(globals['repo_dir'], f.replace('/', '%'))
        if os.path.exists(link_name):
            if os.path.isdir(link_name):
                shutil.rmtree(link_name)
            else:
                os.remove(link_name)
        f = os.path.expanduser(os.path.join('~', f))
        if os.path.isdir(f):
            shutil.copytree(f, link_name, copy_function=os.link)  # copy a dir using hard links for individual files
        else:
            os.link(f, link_name)  # hard link
        files.append(link_name)
    return files


def git_add(files: List[str], repo: Repo) -> bool:
    # git commit if dirty
    index = repo.index
    index.add(files)
    if repo.is_dirty():
        # replace absolute path with path relative to home
        files = list(map(lambda x: x.replace(globals['home'], '~'), files))
        # replace % with /
        files = list(map(lambda x: x.replace('%', '/'), files))
        commit_msg = "Update {0} files\n\n".format(len(files)) + "File list: {0}".format(str(files))
        index.commit(message=commit_msg)
        return True
    else:
        return False


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
        conf = read_config([args.use_conf])
    else:
        conf = read_config(config.CONFIG_LOCS)

    # load or init git repo
    config.logger.info("Loading git repo")
    repo = init_dotez_repo(conf)

    # get files matching the rules
    config.logger.info("Getting a list of dotfiles")
    files = match_files(conf, repo)

    if args.test:
        # replace absolute path with path relative to home
        files = list(map(lambda x: x.replace(globals['home'], '~'), files))
        # replace % with /
        files = list(map(lambda x: x.replace('%', '/'), files))
        print('Files to be added: ', files)
        exit(0)

    # commit files if dirty
    config.logger.info("Committing files")
    dirty = git_add(files, repo)
    if dirty:
        if not args.no_push:
            # TODO: push to remote
            config.logger.info("Pushing to remote")
    else:
        config.logger.info("No changed files")


if __name__ == "__main__":
    main()
