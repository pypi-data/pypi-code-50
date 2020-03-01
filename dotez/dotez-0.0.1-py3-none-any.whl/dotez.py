#!/usr/bin/env python3
from dotez import config
from typing import List
import json
import os
from git import Repo

globals = {}


def read_config(config_locs: List[str]) -> dict:
    found = False
    # default config here
    conf = config.DEFAULT_CONFIG
    for config_loc in config_locs:
        if os.path.isfile(config_loc):
            found = True
            try:
                with open(config_loc) as f:
                    conf.update(json.load(f))
            except Exception as e:
                exit("Cannot parse configuration file at: " + config_loc + ".\nError message: " + str(e))

    if not found:
        config.logger.warning("Cannot find a configuration file")
    return conf


def init_dotez_repo(conf: dict) -> Repo or None:
    repo_dir: str = os.path.expanduser(conf['dotez_data_dir'])
    globals['repo_dir'] = repo_dir
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
    try:
        globals['homedir'] = homedir = os.path.join(repo_dir, 'homedir')
        if not os.path.exists(homedir):
            os.symlink(os.path.expanduser('~'), homedir)
    except OSError as e:
        config.logger.error("Cannot create symlink in dotez data directory. Erro message: {0}".format(e.args[0]))
    return repo


def wildcard_match(pattern: str, input_: str) -> bool:
    pattern = pattern.replace('.', r'\.')
    pattern = pattern.replace('*', r'[^\s]*')
    import re
    return bool(re.search(pattern, input_))


def git_add(conf: dict, repo: Repo) -> None:
    files: List[str] = []
    for f in conf['includes']:
        # TODO: check whether files are included
        # check whether files are ignored, if so, override include rules
        ignored = False
        for p in conf['ignores']:
            if wildcard_match(p, f):
                ignored = True
                break
        if ignored:
            continue
        f = os.path.join(globals['homedir'], f)
        files.append(os.path.expanduser(f))
    index = repo.index
    index.add(files)
    # replace absolute path with path relative to home
    files = list(map(lambda x: x.replace(globals['homedir'], '~'), files))
    commit_msg = "Update {0} files\n\n".format(len(files)) + "File list: {0}".format(str(files))
    index.commit(message=commit_msg)


def main():
    conf = read_config(config.CONFIG_LOCS)
    repo = init_dotez_repo(conf)
    git_add(conf, repo)


if __name__ == "__main__":
    main()
