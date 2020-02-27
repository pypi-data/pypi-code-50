import re
import os
import time
import warnings
import pathlib
from typing import Union, List, Pattern, Match


class Watcher(object):
    def __init__(self,
                 path: Union[str, pathlib.Path],
                 watchfor: Union[str, Pattern] = '',
                 includesubfolders: bool = True,
                 subdirectory: str = None,
                 watch_type: str = 'file',
                 exclude_subfolders: List[str] = None,
                 match_exact: bool = False,
                 ignore_case: bool = True,
                 ):
        """
        Watches a folder for file changes.

        :param path: The folder path to watch for changes
        :param watchfor: Watch for this item. This can be a full filename, or an extension (denoted by *., e.g. "*.ext")
        :param bool includesubfolders: wehther to search subfolders
        :param str subdirectory: specified subdirectory
        :param str watch_type: The type of item to watch for ('file' or 'folder')
        :param exclude_subfolders: specific sub folders to exclude when looking for files. These subfolders will be
            globally excluded.
        :param match_exact: whether the watcher should only look for exact matches of the provided pattern
        :param ignore_case: case sensitivity for matches
        """
        # protected attributes for properties
        self._path = None
        self._subdir = None
        self._watchfor = None
        self._ignore_case: bool = True

        self.match_exact: bool = match_exact
        self.path = path
        self.includesubfolders = includesubfolders
        self.watchfor = watchfor
        self.ignore_case = ignore_case
        self.watch_type = watch_type
        if exclude_subfolders is None:
            exclude_subfolders = []
        self.exclude_subfolders = exclude_subfolders
        self.subdirectory = subdirectory

    def __repr__(self):
        return f'{self.__class__.__name__}({len(self.contents)} {self.watchfor})'

    def __str__(self):
        return f'{self.__class__.__name__} with {len(self.contents)} matches of {self.watchfor}'

    def __len__(self):
        return len(self.contents)

    def __iter__(self):
        for file in self.contents:
            yield file

    @property
    def path(self) -> pathlib.Path:
        """path to watch"""
        return self._path

    @path.setter
    def path(self, newpath: Union[str, pathlib.Path]):
        if isinstance(newpath, pathlib.Path) is False:
            newpath = pathlib.Path(newpath)
        if not os.path.isdir(newpath):
            raise ValueError(f'The specified path\n{newpath}\ndoes not exist.')
        self._path = newpath

    @property
    def subdirectory(self) -> str:
        """specific subdirectory to watch within the path"""
        return self._subdir

    @subdirectory.setter
    def subdirectory(self, newdir: str):
        if newdir is None:
            del self.subdirectory
            return
        if os.path.isdir(self.path / newdir) is False:
            raise ValueError(f'The subdirectory {newdir} does not exist in the path {self.path}.')
        if newdir in self.exclude_subfolders:
            raise ValueError(f'The subdirectory {newdir} is specifically excluded in the exclude_subfolders attribute.')
        self._subdir = newdir

    @subdirectory.deleter
    def subdirectory(self):
        self._subdir = None

    @property
    def full_path(self) -> pathlib.Path:
        """full watch path (including subdirectory)"""
        if self.subdirectory is not None:
            return self.path / self.subdirectory
        return self.path

    @property
    def watchfor(self) -> Pattern:
        """the pattern to watch for in the directory"""
        return self._watchfor

    @watchfor.setter
    def watchfor(self, value: Union[str, Pattern]):
        if value is None:
            value = ''
        if type(value) is str and value.startswith('*'):
            warnings.warn(f'the value "{value}" is an invalid regex pattern, please remove the "*"')
            value = '.' + value
        if isinstance(value, Pattern) is False:
            value = re.compile(
                value,
                flags=re.IGNORECASE if self.ignore_case else 0
            )
        self._watchfor = value

    @watchfor.deleter
    def watchfor(self):
        self.watchfor = ''

    @property
    def ignore_case(self) -> bool:
        """whether instance will be case sensitive"""
        return self._ignore_case

    @ignore_case.setter
    def ignore_case(self, value: bool):
        if value != self._ignore_case:
            self._ignore_case = value
            # regenerate pattern
            self.watchfor = self.watchfor.pattern

    @property
    def contents(self) -> list:
        """Finds all instances of the watchfor item in the path"""
        # todo make this less arduous for large directories
        path = self.full_path
        contents = []

        if self.includesubfolders is True:
            for root, dirs, files in os.walk(path):  # walk through specified path
                dirs[:] = [d for d in dirs if d not in self.exclude_subfolders]
                if self.watch_type == 'file':
                    for filename in files:  # check each file
                        if self._condition_match(filename) is not None:  # search for pattern match
                            file_path = os.path.join(root, filename)
                            if os.path.isfile(file_path) is True:  # ensure file
                                contents.append(file_path)
                elif self.watch_type == 'folder':
                    for directory in dirs:
                        if self._condition_match(directory) is not None:
                            dir_path = os.path.join(root, directory)
                            if os.path.isdir(dir_path) is True:  # ensure directory
                                contents.append(dir_path)
        else:
            for file in os.listdir(path):
                if self._condition_match(file) is not None:
                    file_path = os.path.join(path, file)
                    if self.watch_type == 'file' and os.path.isfile(file_path):
                        contents.append(file_path)
                    elif self.watch_type == 'folder' and os.path.isdir(file_path):
                        contents.append(file_path)
        return contents

    def _condition_match(self, string: str) -> Match:
        """
        Performs the condition match on the provided string

        :param string: string to perform match/search against
        :return: match or none
        """
        if self.match_exact is True:
            return self.watchfor.match(string)
        else:
            return self.watchfor.search(string)

    def check_path_for_files(self):
        """Finds all instances of the watchfor item in the path"""
        warnings.warn('The check_path_for_files method has be depreciated, access .contents directly',
                      DeprecationWarning)
        return self.contents

    def find_subfolder(self):
        """returns the subdirectory path within the full path where the target file is"""
        path = self.full_path
        contents = []
        for root, dirs, files in os.walk(path):  # walk through specified path
            for filename in files:  # check each file
                if self._condition_match(filename) is not None:
                    # todo catch file/folder?
                    contents.append(root)
        return contents

    def wait_for_presence(self, waittime=1.):
        """waits for a specified match to appear in the watched path"""
        while len(self.contents) == 0:
            time.sleep(waittime)
        return True

    def oldest_instance(self, wait=False, **kwargs):
        """
        Retrieves the first instance of the watched files.

        :param wait: if there are no instances, whether to wait for one to appear
        :return: path to first instance (None if there are no files present)
        """
        if len(self.contents) == 0:  # if there are no files
            if wait is True:  # if waiting is specified
                self.wait_for_presence(**kwargs)
            else:  # if no wait and no files present, return None
                return None
        if len(self.contents) == 1:  # if there is only one file
            return os.path.join(self._path, self.contents[0])
        else:  # if multiple items in list
            return os.path.join(  # return path to oldest (last modified) file in directory
                self._path,
                min(
                    zip(
                        self.contents,  # files in directory
                        [  # last modifiation time for files in directory
                            os.path.getmtime(
                                os.path.join(self._path, filename)
                            ) for filename in self.contents
                        ]
                    ),
                    key=lambda x: x[1]
                )[0]
            )

    def newest_instance(self):
        """
        Retrieves the newest instance of the watched files.

        :return: path to newest instance
        :rtype: str
        """
        if len(self.contents) == 0:  # if there are no files
            # if wait is True:  # if waiting is specified
            #     self.wait_for_presence(**kwargs)
            # else:  # if no wait and no files present, return None
            return None
        if len(self.contents) == 1:  # if there is only one file
            return os.path.join(self._path, self.contents[0])
        else:  # if multiple items in list
            return os.path.join(  # return path to oldest (last modified) file in directory
                self._path,
                max(
                    zip(
                        self.contents,  # files in directory
                        [os.path.getmtime(  # last modifiation time for files in directory
                            os.path.join(self._path, filename)
                        ) for filename in self.contents]
                    ),
                    key=lambda x: x[1]
                )[0]
            )
