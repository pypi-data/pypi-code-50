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
    RemoteProgress.COUNTING: "COUNTING",
    RemoteProgress.COMPRESSING: "COMPRESSING",
    RemoteProgress.RECEIVING: "RECEIVING",
    RemoteProgress.RESOLVING: "RESOLVING",
    RemoteProgress.FINDING_SOURCES: "FINDING_SOURCES",
    RemoteProgress.WRITING: "WRITING",
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

    def test_config(self) -> None:
        files = self.match_files()
        # replace absolute path with path relative to home
        files = list(map(lambda x: x.replace(self.home, '~'), files))
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
        # initialize some abspath
        self.home = os.path.expanduser('~')
        self.repo_dir = os.path.expandvars(self.conf['dotez_data_dir'])
        self.repo_dir = os.path.expanduser(self.repo_dir)

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
        # setup remotes
        self.setup_remotes()

    def wildcard_match(self, pattern: str, input_: str) -> bool:
        pattern = os.path.join(self.home, pattern)
        return PurePath(input_).match(pattern)

    def match_files(self) -> List[str]:
        files: List[str] = []
        includes: List[str] = []
        # match includes
        for f in self.conf['includes']:
            includes += glob.glob(os.path.join(self.home, f))

        # check whether files are ignored, if so, override include rules
        for f in includes:
            # ~ is expanded, but we are undoing it to get shorter names of links
            f = str(PurePath(f).relative_to(self.home))
            ignored = False
            for p in self.conf['ignores']:
                if self.wildcard_match(p, f):
                    ignored = True
                    break
            if ignored:
                continue
            link_name = os.path.join(self.repo_dir, f.replace('/', '%'))
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

    def git_commit(self, files: List[str]) -> bool:
        # git commit if dirty
        index = self.repo.index
        index.add(files)
        if self.repo.is_dirty():
            # replace absolute path with path relative to home
            files = list(map(lambda x: x.replace(self.home, '~'), files))
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
