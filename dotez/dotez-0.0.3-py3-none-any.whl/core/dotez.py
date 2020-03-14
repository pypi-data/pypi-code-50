from dotez import config
from typing import List, Optional, Dict
import json
import os
import shutil
from git import Repo, Remote
from pathlib import PurePath
import glob
from git.remote import RemoteProgress

__all__ = ['DotEZ']

GIT_PUSH_OP_ID = {
    RemoteProgress.COUNTING: "Counting",
    RemoteProgress.COMPRESSING: "Compressing",
    RemoteProgress.RECEIVING: "Receiving",
    RemoteProgress.RESOLVING: "Resolving",
    RemoteProgress.FINDING_SOURCES: "Finding Sources",
    RemoteProgress.WRITING: "Writing",
}


class DotEZ:
    def __init__(self, config_locs: List[str]):
        self.repo_dir: str = ''
        self.home: str = ''
        # initialize with default config first
        self.conf: dict = config.DEFAULT_CONFIG
        self.repo: Optional[Repo] = None
        self.remotes: Dict[str, Remote] = {}
        # load configs, may override some things defined above
        self.read_config(config_locs)
        self.home = os.path.expanduser('~')
        self.repo_dir = os.path.expandvars(self.conf['dotez_data_dir'])
        self.repo_dir = os.path.expanduser(self.repo_dir)
        config.logger.info("Home: {}; Repo: {}".format(self.home, self.repo_dir))

    def test_config(self) -> None:
        files = self.index_files()
        # replace absolute path with path relative to `self.repo_dir`
        files = [os.path.relpath(f, self.repo_dir) for f in files]
        # replace % with /
        files = list(map(lambda x: x.replace('%', '/'), files))
        config.logger.info('Files to be added: {}'.format(files))

    def read_config(self, config_locs: List[str]) -> None:
        found = False
        for config_loc in config_locs:
            config_loc = os.path.expandvars(config_loc)
            config_loc = os.path.expanduser(config_loc)
            if os.path.isfile(config_loc):
                found = True
                try:
                    with open(config_loc) as f:
                        self.conf.update(json.load(f))
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

    def init_dotez_repo(self) -> None:
        # init or load the repo
        if not os.path.isdir(self.repo_dir):
            config.logger.info("No existing dotez data directory, creating a new one...")
            try:
                os.mkdir(self.repo_dir)
                self.repo = Repo.init(self.repo_dir)
            except Exception as e:
                config.logger.error("Cannot create git repo at: '" + self.repo_dir + "'. Error message: {0}".format(e))
                exit(1)
        else:
            if os.path.exists(os.path.join(self.repo_dir, '.git')):
                self.repo = Repo(self.repo_dir)
            else:
                self.repo = Repo.init(self.repo_dir)

    def wildcard_match(self, pattern: str, input_: str) -> bool:
        pattern = os.path.join(self.home, pattern)
        return PurePath(input_).match(pattern)

    def link_files_or_dirs(self, src: str) -> List[str]:
        """
        Create links in `self.repo_dir` to real dotfiles
        :param src: relative path to `self.home`
        :return: list of strings containing the created links
        """
        ret = []
        # make sure that `src` is abs, `rel_src` is relative to `self.home`
        if self.home not in src:
            rel_src = src
            src = os.path.join(self.home, src)
        else:
            rel_src = os.path.relpath(src, self.home)

        # TODO: escape '%' if it's already in the filename
        # TODO: allow users to specify custom replacement for '/' other than '%'
        # replace '/' with '%'
        link_name = os.path.join(self.repo_dir, rel_src.replace('/', '%'))
        src = os.path.expanduser(os.path.join('~', src))
        if os.path.exists(link_name):
            # if a directory in data_dir already exists, delete and recreate files under it, in case the user
            # might have deleted some of the files in the dir
            if os.path.isdir(link_name):
                shutil.rmtree(link_name)
            else:
                os.remove(link_name)

        # if dir, recursively link all the files/dirs under it
        if os.path.isdir(src):
            # FIXME: detect and follow symlinks?
            files = os.scandir(src)
            for f in files:
                ret += self.link_files_or_dirs(os.path.join(src, f))
        else:
            # print(link_name)
            os.link(src, link_name)  # hard link
            ret.append(link_name)
        return ret

    def clean_repo(self) -> None:
        for f in os.scandir(self.repo_dir):
            f = f.name
            # FIXME: missing something?
            # PREVENT deleting git files, or repo_dir
            if f in ['.git', '.gitignore', '.gitconfig', '.gitmodules', '.gitattributes', 'dotez']:
                continue
            # PREVENT deleting self.repo_dir
            f = os.path.join(self.repo_dir, f)
            if os.path.samefile(f, self.repo_dir):
                continue
            # PREVENT deleting non-existing files, but exception for invalid hard links
            if not os.path.islink(f) and not os.path.exists(f):
                continue
            # remove dirs or files
            if os.path.isdir(f):
                shutil.rmtree(f)
            elif os.path.islink(f) or os.path.isfile(f):
                os.remove(f)

    def index_files(self) -> List[str]:
        self.clean_repo()
        files: List[str] = []
        includes: List[str] = []
        # match includes
        for f in self.conf['includes']:
            includes += glob.glob(os.path.join(self.home, f))

        # ~ is expanded, but we are undoing it to get shorter names of links
        includes = [os.path.relpath(i, self.home) for i in includes]

        # check whether files are ignored, if so, override include rules
        for f in set(includes):
            ignored = False
            for p in self.conf['ignores']:
                if self.wildcard_match(p, f):
                    ignored = True
                    break
            if ignored:
                continue
            link_names = self.link_files_or_dirs(f)
            files += link_names
        return files

    def git_commit(self, files: List[str]) -> bool:
        # git commit if dirty
        index = self.repo.index
        index.add(files)
        if self.repo.is_dirty():
            # replace absolute path with path relative to `self.repo_dir`
            files = [os.path.relpath(f, self.repo_dir) for f in files]
            # replace % with /
            files = list(map(lambda x: x.replace('%', '/'), files))
            # TODO: only show dirty files, instead of listing all files
            commit_msg = "Update {0} files\n\n".format(len(files)) + "File list: {0}".format(str(files))
            index.commit(message=commit_msg)
            return True
        else:
            return False

    def setup_remotes(self) -> None:
        # get existing remotes
        existing_remotes = self.repo.remotes
        existing_remote_names = list(map(lambda r: r.name, existing_remotes))
        conf_remote_names = list(map(lambda r: r['name'], self.conf['remotes']))

        config.logger.info("Using remotes: {}".format(self.conf['remotes']))

        # check whether an existing remote needs to be deleted
        for ern in existing_remote_names:
            if ern not in conf_remote_names:
                self.repo.delete_remote(ern)
            else:
                # FIXME: optimize this process?
                self.remotes[ern] = self.repo.remote(ern)

        # create new remotes
        for remote in self.conf['remotes']:
            rn = remote['name']
            # if remote already exists, skip
            if rn in existing_remote_names:
                # TODO: check whether a remote needs update, such as url being changed
                continue
            origin = self.repo.create_remote(rn, remote['url'])
            assert origin.exists()
            # set local "master" to track remote "master
            try:
                self.repo.create_head('master', origin.refs.master)
            except OSError:
                # If a Reference with the same name but different contents already exists.
                pass
            self.repo.heads.master.set_tracking_branch(origin.refs.master).checkout()
            self.remotes[rn] = origin

    @staticmethod
    def push_process_callback(op_code, cur_count, max_count=None, message=''):
        stage_id = op_code & RemoteProgress.STAGE_MASK
        op_id = op_code & RemoteProgress.OP_MASK
        op = GIT_PUSH_OP_ID[op_id]

        if message == '':
            msg = "{0}: {1}/{2}".format(op, cur_count, max_count)
        else:
            msg = "{0}: {1}/{2} {3}".format(op, cur_count, max_count, message)
        if stage_id & RemoteProgress.END:
            print(msg)
        else:
            print(msg, end='\r')

    def push_remotes(self):
        # setup remotes
        self.setup_remotes()
        remote_configs = self.conf['remotes']
        for rc in remote_configs:
            push = rc['push']
            if not push:
                continue
            name = rc['name']
            self.remotes[name].push(refspec='refs/heads/master:refs/heads/master',
                                    progress=DotEZ.push_process_callback)
            # FIXME:
            print('\n')
