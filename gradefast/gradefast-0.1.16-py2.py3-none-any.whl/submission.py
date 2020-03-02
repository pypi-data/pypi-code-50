"""
Contains :class:`Submission` and :class:`SubmissionGroup` classes that represent `submission` 
of a single `team` (or student) and `many teams` (or many students), respectively.

:class:`LoadSubmissions` is a utility class to quickly populate a :class:`SubmissionGroup` from
sources like `web portal`, `filesystem` or `databases`.
"""

import os
import re
import json
import logging
import fnmatch
from os import listdir
from datetime import datetime, timedelta
from abc import ABC, ABCMeta, abstractmethod

from pathlib import Path
from typing import Union
from os.path import isfile, join
import urllib.request as urllib2
from urllib.response import addinfourl

import requests
from slugify import slugify
from bs4 import BeautifulSoup

from gradefast import utils
from gradefast import logconfig
from gradefast.exceptions import *


logger = logconfig.configure_and_get_logger(__name__)

class Submission(object):
    """
    Represents a team (or student) submission information

    A :class:`Submission` contains information about a team's uploaded task items like images, 
    text files or zips, on the web, filesystem or databases. Gradefast uses this information 
    in utility classes like :class:`~gradefast.utils.Download` to download files locally. It 
    also uses it to search and provide files to a :class:`~gradefast.test.GFTest` when executed 
    from within an :class:`~gradefast.test.Evaluate` 
    
    Parameters
    ----------
    team_id : int
        Identifier of a team (or student)

    items : dict
        Dictionary of uploaded items. ``e.g. {'zip': {'url': 'https://e-yantra.org/some.zip'}, 
        'png': {'url': 'https://e-yantra.org/some.zip'}}``

    Attributes
    ----------
    team_id : int
        Identifier of a team (or student)
        
    items : dict
        Dictionary of uploaded items. ``e.g. {'zip': {'url': 'https://e-yantra.org/some.zip'}, 
        'png': {'url': 'https://e-yantra.org/some.zip'}}``
    
    Examples
    --------
    .. doctest::

        >>> team_id = 75
        >>> items =  {'png': {'url': 'http://eyntra.org/test.png', 'path': 'path/to/png.png'},
        ... 'zoo': {'url': 'http://eyntra.org/zoo.txt', 'path': 'path/to/zoo.txt'}}
        >>> Submission(team_id, items)
        Submission({'team_id': 75, 'items': {'png': {'url': 'http://eyntra.org/test.png', 'path':
        'path/to/png.png'}, 'zoo': {'url': 'http://eyntra.org/zoo.txt', 'path': 'path/to/zoo.txt'}}})

    """
    def __init__(self, team_id: int, items: dict):
        # Identified by team id. Should be a number
        if isinstance(team_id, int): 
            self.team_id = team_id
        elif isinstance(team_id, str) and utils.is_string_number(team_id):
            self.team_id = int(team_id)
        else:
            # Dictionary of items uploaded and their metadata like path on filesystems
            raise TypeError("team_id should be a number")
        self.items = items
    
    def __repr__(self):
        return "Submission(" + self.__dict__.__str__()[1:-1] + ")"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, value):
        return utils.object_equality(self, value)

    def __ne__(self, value):
        return not self.__eq__(value)

    def to_dict(self):
        """
        Converts from :class:`Submission` to a :class:`dict`

        Returns
        -------
        dict

        Examples
        --------
        .. doctest::

            >>> team_id = 75
            >>> items =  {'png': {'url': 'http://eyntra.org/test.png', 'path': 'path/to/png.png'},
            ... 'zoo': {'url': 'http://eyntra.org/zoo.txt', 'path': 'path/to/zoo.txt'}}
            >>> submission = Submission(team_id, items)
            >>> submission.to_dict()
            {'team_id': 75, 'items': {'png': {'url': 'http://eyntra.org/test.png', 'path':
            'path/to/png.png'}, 'zoo': {'url': 'http://eyntra.org/zoo.txt', 'path': 'path/to/zoo.txt'}}}
        
        """
        return self.__dict__

    @staticmethod
    def from_dict(submission_dict: dict):
        """
        Creates a :class:`Submission` from a :class:`dict`.

        Parameters
        ----------
        submission_dict: dict
            Should contain `keys` `team_id`, and `items`.

        Returns
        -------
        :class:`Submission`
            A :class:`Submission` built from the submission dictionary

        Examples
        --------
        .. doctest::

            >>> submission_dict = {'team_id': 75, 'items': {'png': {'url': 'http://eyntra.org/
            ... test.png', 'path': 'path/to/png.png'}, 'zoo': {'url': 'http://eyntra.org/zoo.txt', 
            ... 'path': 'path/to/zoo.txt'}}}
            >>> Submission.from_dict(submission_dict)
            Submission({'team_id': 75, 'items': {'png': {'url': 'http://eyntra.org/test.png',
            'path': 'path/to/png.png'}, 'zoo': {'url': 'http://eyntra.org/zoo.txt', 'path':
            'path/to/zoo.txt'}}})
        """
        return Submission(submission_dict['team_id'], submission_dict['items'])

class SubmissionGroup:
    """
    Groups many :class:`Submission` together

    A :class:`SubmissionGroup` clubs multiple :class:`Submission` together and includes 
    additional information like ``task_name`` and ``theme_name``. 

    Parameters
    ----------
    task_name: str

    theme_name: str

    submissions: list, dict
        List or dictionary of submissions. If dictionary, key should be a team_id 
        and value should be a :class:`Submission`

    Attributes
    ----------
    task_name: str

    theme_name: str

    dict_of_submissions: dict
        A dictionary of submissions where `key` is a team_id and `value` is a :class:`Submission`

    Warnings
    ---------    
    :class:`SubmisisonGroup` is an iterator. Try not to mutate it and expect it to work fabulously thereafter.
    
    Examples
    --------
    .. doctest::

        >>> team_id1 = 75
        >>> items1 = {'png': {'url': 'someurl', 'downloaded': True}, 'py': {'url': 'hello', 'latest': True}}
        >>> submission1 = Submission(team_id1, items1)

        >>> team_id2 = 987
        >>> items2 = {'ipynb': {'url': 'pqwdm', 'downloaded': False}, 'png': {'url': 'uuhsnad'}}
        >>> submission2 = Submission(team_id2, items2)

        >>> team_id3 = 453
        >>> items3 = {'py': {'url': 'gnlkj', 'downloaded': False}, 'ipynb': {}}
        >>> submission3 = Submission(team_id3, items3)

        >>> SubmissionGroup('Task0', 'Homecoming', {submission.team_id: submission
        ... for submission in [submission1, submission2, submission3]})
        SubmissionGroup(task_name: Task0, theme_name: Homecoming, dict_of_submissions: {75:
        Submission({'team_id': 75, 'items': {'png': {'url': 'someurl', 'downloaded': True},
        'py': {'url': 'hello', 'latest': True}}}), 987: Submission({'team_id': 987, 'items':
        {'ipynb': {'url': 'pqwdm', 'downloaded': False}, 'png': {'url': 'uuhsnad'}}}), 453:
        Submission({'team_id': 453, 'items': {'py': {'url': 'gnlkj', 'downloaded': False},
        'ipynb': {}}})})

    """
    def __init__(self, task_name: str, theme_name: str, submissions: Union[list, dict]):
        self.task_name = task_name
        self.theme_name = theme_name
        if type(submissions) == list:
            submissions = {int(submission.team_id) if type(submission.team_id) == str 
            else submission.team_id: submission for submission in submissions}
        self.dict_of_submissions = submissions
        self._iter = iter(self.dict_of_submissions)

    def __iter__(self):
        return self
    
    def __len__(self):
        return len(self.dict_of_submissions)

    def __next__(self):
        try:
            self._curr_idx = next(self._iter)
            idx = self._curr_idx
            return self.dict_of_submissions[self._curr_idx]
        except StopIteration:
            self._iter = iter(self.dict_of_submissions)
            raise StopIteration
    
    def __getitem__(self, team_id: int) -> Submission:
        try:
            if isinstance(team_id, slice):
                dict_of_submissions = {}
                for ii in range(*team_id.indices(team_id.stop)):
                    if self[ii] != None:
                        dict_of_submissions[ii] = self[ii]
                return SubmissionGroup(self.task_name, self.theme_name, dict_of_submissions)
            elif type(team_id) == str:
                if self.dict_of_submissions.get(team_id) != None:
                    return self.dict_of_submissions[team_id]
                elif self.dict_of_submissions.get(int(team_id)) != None:
                    return self.dict_of_submissions[int(team_id)]
            elif type(team_id) == int:
                if self.dict_of_submissions.get(team_id) != None:
                    return self.dict_of_submissions[team_id]
                elif self.dict_of_submissions.get(str(team_id)) != None:
                    return self.dict_of_submissions[str(team_id)]
        except KeyError:
            return None

    def __eq__(self, value) -> bool:
        return utils.object_equality(self, value)

    def __ne__(self, value):
        return not self.__eq__(value)

    def __repr__(self):
        return "SubmissionGroup(task_name: {}, theme_name: {}, dict_of_submissions: {})".format(self.task_name, self.theme_name, self.dict_of_submissions)

    def __str__(self):
        return self.__repr__()

    # TODO: need to safely remove this
    def find_by_id(self, team_id):
        # find submission quickly by exploiting the fact that submissions are stored in sorted order
        try:
            return self.dict_of_submissions[team_id]
        except KeyError:
            return None

    @staticmethod
    def from_dict(group_dict):
        """
        Creates a :class:`SubmissionGroup` from a :class:`dict`

        Parameters
        ----------
        group_dict: dict

        Returns
        -------
        :class:`SubmissionGroup`

        Examples
        --------
        .. doctest::

            >>> submission_group_dict = {'task_name': 'Task0', 'theme_name': 'Homecoming',
            ... 'dict_of_submissions': {75: {'team_id': 75, 'items': {'png': {'url': 'someurl',
            ... 'downloaded': True}, 'py': {'url': 'hello', 'latest': True}}}, 987: {'team_id': 987,
            ... 'items': {'ipynb': {'url': 'pqwdm', 'downloaded': False}, 'png': {'url': 'uuhsnad'}}},
            ... 453: {'team_id': 453, 'items': {'py': {'url': 'gnlkj', 'downloaded': False}, 'ipynb':
            ... {}}}}}
            >>> SubmissionGroup.from_dict(submission_group_dict)
            SubmissionGroup(task_name: Task0, theme_name: Homecoming, dict_of_submissions: {75:
            Submission({'team_id': 75, 'items': {'png': {'url': 'someurl', 'downloaded': True},
            'py': {'url': 'hello', 'latest': True}}}), 987: Submission({'team_id': 987, 'items':
            {'ipynb': {'url': 'pqwdm', 'downloaded': False}, 'png': {'url': 'uuhsnad'}}}), 453:
            Submission({'team_id': 453, 'items': {'py': {'url': 'gnlkj', 'downloaded': False},
            'ipynb': {}}})})
        """
        dict_of_submissions = {}
        for team_id, submission in group_dict['dict_of_submissions'].items():
            if type(team_id) == str:
                dict_of_submissions[int(team_id)] = Submission.from_dict(submission)
            else:
                dict_of_submissions[team_id] = Submission.from_dict(submission)
        return SubmissionGroup(group_dict['task_name'], group_dict['theme_name'], dict_of_submissions)

    def to_dict(self):
        """
        Converts from :class:`SubmissionGroup` to a :class:`dict`
        
        Returns
        -------
        dict

        Examples
        --------
        .. doctest::

            >>> submission_group.to_dict()
            {'task_name': 'Task0', 'theme_name': 'Homecoming', 'dict_of_submissions': {75:
            {'team_id': 75, 'items': {'png': {'url': 'someurl', 'downloaded': True}, 'py':
            {'url': 'hello', 'latest': True}}}, 987: {'team_id': 987, 'items': {'ipynb':
            {'url': 'pqwdm', 'downloaded': False}, 'png': {'url': 'uuhsnad'}}}, 453: {'team_id':
            453, 'items': {'py': {'url': 'gnlkj', 'downloaded': False}, 'ipynb': {}}}}}

        """
        group_dict = {}
        group_dict['task_name'] = self.task_name
        group_dict['theme_name'] = self.theme_name
        group_dict['dict_of_submissions'] = {}
        # print(self.dict_of_submissions)
        for team_id, submission in self.dict_of_submissions.items():
            group_dict['dict_of_submissions'][team_id] = submission.__dict__

        return group_dict

    @staticmethod
    def from_json(file_path):
        """
        Create a :class:`SubmissionGroup` from a json file

        Parameters
        ----------
        file_path: str
            Path to json file

        Returns
        -------
        :class:`SubmissionGroup`

        Examples
        --------
        .. doctest::

            >>> SubmissionGroup.from_json('path/to/json/file')
            SubmissionGroup(task_name: Task0, theme_name: Homecoming, dict_of_submissions: {75:
            Submission({'team_id': 75, 'items': {'png': {'url': 'someurl', 'downloaded': True},
            'py': {'url': 'hello', 'latest': True}}}), 987: Submission({'team_id': 987, 'items':
            {'ipynb': {'url': 'pqwdm', 'downloaded': False}, 'png': {'url': 'uuhsnad'}}}), 453:
            Submission({'team_id': 453, 'items': {'py': {'url': 'gnlkj', 'downloaded': False},
            'ipynb': {}}})})
        """
        if os.path.isdir(file_path):
            file_path = os.path.join(file_path, 'submission.json')
        # print(file_path)
        with open(file_path, 'r') as json_file:
            group_dict = json.load(json_file)
            return SubmissionGroup.from_dict(group_dict)

    def to_json(self, save_path):
        """
        Save a :class:`SubmissionGroup` object to json file

        Parameters
        ----------
        save_path: str
            Path to json file or directory

        Returns
        -------
        None

        Examples
        --------
        .. doctest::

            >>> submission_group.to_json('path/to/json/file')
        """
        if os.path.isdir(save_path):
            save_path = os.path.join(save_path, 'submission.json')
        with open(save_path, 'w+') as json_file:
            group_dict = self.to_dict()
            json.dump(group_dict, json_file)

class LoadSubmissions:
    """
    A utility class to load submission information from web portal, filesystem or databases

    Use this class to populate information about submission from web page or filesystem. Unless 
    you want to create only a few :class:`Submission` objects for testing, :attr:`~LoadSubmissions.get_submissions()`
    of this class should be the preferred way to load and create a :class:`SubmissionGroup`.

    .. note::

        :class:`LoadSubmissions` is never instantiated directly. Use either :attr:`LoadSubmissions.from_url`
        or :attr:`LoadSubmissions.from_fs` 

    Parameters
    ----------
    cookie: str, optional
        HTTP cookie obtained from the logged in session on the web portal.
    task_url: str, optional
        Url of the web page showing information to download files. 
        ``e.g. 'http://old.e-yantra.org/admin/grade/task0'``
    task_name: str, optional
    theme_name: str, optional
    fs_location: str, optional
        Filesystem location where the downloaded files were stored. You can use this option for 
        testing by creating the directory structure according to downloading conventions
    types: list, optional
        List of items to download from all the items available. ``e.g. ['zip', 
        'png2', 'txt1']``. Default is ['zip']
    after_date: Union[str, datetime], optional
        If specified, submissions uploaded only at or after provided datetime or date string will
        be considered in submission_group
    before_date: Union[str, datetime], optional
        If specified, submissions uploaded only at or before provided datetime or date string will
        be considered in submission_group
    scraper: str, :class:`Scraper`, optional
        If 'default', then use :class:`DefaultScraper`, else use provided :class:`Scraper`

    Attributes
    ----------
    cookie: str
        HTTP cookie obtained from the logged in session on the web portal
    task_url: str
        Url of the web page showing information to download files. 
        ``e.g. 'http://old.e-yantra.org/admin/grade/task0'``
    task_name: str
    theme_name: str
    fs_location: str
        Filesystem location where the downloaded files were stored. You can use this option for 
        testing by creating the directory structure according to downloading conventions
    types: list
        List of items to download from all the items available. ``e.g. ['zip', 'png2', 'txt1']``
    after_date: Union[str, datetime]
        If specified, submissions uploaded only at or after provided datetime or date string will
        be considered in submission_group
    before_date: Union[str, datetime]
        If specified, submissions uploaded only at or before provided datetime or date string will
        be considered in submission_group
    scraper: str, :class:`Scraper`
        If 'default', then use :class:`DefaultScraper`, else use provided :class:`Scraper`

    """
    def __init__(self, cookie: str = '', task_url: str = '', task_name: str = '', 
    theme_name: str = '', fs_location: str = '', types: list = ['zip'], after_date = '',
    before_date = '', scraper: Union[str, object] = 'default2019'):
        # Top level LoadSubmissions
        # Not supposed to be used directly
        # Use either LoadSubmissions.from_fs or LoadSubmissions.from_url
        self.cookie = cookie
        self.task_url = task_url
        self.task_name = task_name
        self.theme_name = theme_name
        self.fs_location = fs_location
        # file types to download
        self.types = types
        self.after_date = after_date
        self.before_date = before_date
        self.scraper = scraper

    @staticmethod    
    def from_url(task_url: str, cookie: str, task_name: str, theme_name: str, types: list = ['zip'], 
    before_date: Union[str, datetime]='', after_date: Union[str, datetime]='', 
    scraper: Union[str, object]='default2019'):
        """
        Creates a :class:`LoadSubmissions` object with information necessary to fetch submissions
        from a webpage

        Parameters
        ----------
        task_url: str
        cookie: str
        task_name: str
        theme_name: str
        types: list
        before_date: Union[str, datetime]
        after_date: Union[str, datetime]
        scraper: str or :class:`Scraper`

        Returns
        -------
        :class:`LoadSubmissions`

        Examples
        --------
        .. doctest::

            >>> task_url = 'http://old.e-yantra.org/admin/grade/task0'
            >>> task_name = 'Task0'
            >>> theme_name = 'Homecoming'
            >>> types = ['png', 'ipynb', 'txt']
            >>> scraper = 'default2019'
            >>> cookie = {'name': 'eyrc18_session', 'value': 
            ... eyJpdiI6Ikk1T1JtRnl3WFdlM2l5TXBDc0RITHc9PSIsInZhbHVlIjoiemZ0b2JzaEh...DE1ZiJ9'}
            >>> LoadSubmissions.from_url(task_url, cookie, task_name, 
            ... theme_name, types=types, method=method)
            <gradefast.submission.LoadSubmissions object at 0x7ff510f4d550>

        """
        # Constructor used to create submission objects from url
        return LoadSubmissions(task_url=task_url, task_name=task_name, cookie=cookie, types=types, 
        before_date=before_date, after_date=after_date, scraper=scraper, theme_name=theme_name)

    @staticmethod
    def from_fs(fs_location: str, task_name: str, theme_name: str):
        """
        Creates a :class:`LoadSubmissions` object with information necessary to fetch submissions
        from a filesystem location

        Parameters
        ----------
        fs_location: str
        task_name: str
        theme_name: str

        Returns
        -------
        :class:`LoadSubmissions`

        Examples
        --------
        .. doctest::

            >>> LoadSubmissions.from_fs('Task2', 'Planter Bot', 'tests/resources/HC_TASK0')
            <gradefast.submission.LoadSubmissions object at 0x7ff510f4fe4>
        """
        # Constructor used to create submission objects from fs
        return LoadSubmissions(fs_location=fs_location, theme_name=theme_name, task_name=task_name)

    def get_file_item_name(self, team_id, file_full_path):
        """
        Returns file item name from full file path

        Parameters
        ----------
        file_full_path: str
            Full path of the submission item
        
        Notes
        ------

        In gradefast, all submission file items are named as <team_id>_<file_item_name>.<extension>.
        For an unzipped folder, the extension part is excluded. <team_id> is always a :class:`int`.
        
        Following are some examples of files: 4_zip.zip, 98_png.png, 257_txt3.txt, 36_text_file.txt,
        8_test_task_1a.py

        For the same files, following are the file_item_names: zip, png, txt3, text_file, test_task_1a.
        
        Returns
        -------
        str
            file_item_name
        """
        # remember all the extensions and file names with that particular extension
        file_name = os.path.basename(file_full_path)
        file_extension = Path(file_full_path).suffix
        try:
            matches = re.match("{}_(.+){}".format(team_id, file_extension), file_name)
            if matches == None or matches.group(1) == None:
                return None
            file_item_name = matches.group(1)
        except Exception as e:
            logger.exception('Exception when attempting to extract "file_item_name"'\
            + ' for team_id: {} from {}'.format(team_id, file_name))
            return None
        # includes a "." in extension like ".zip"
        return file_item_name

    def make_submissions_from_fs(self):
        """
        Creates a :class:`SubmissionGroup` from given file system location where
        the submission files are downloaded

        Assumes that files and extracted folders are named according to gradefast's 
        convention. Gradefast falls back to using this method if there is no submission_group.json
        in the provided :attr:`fs_location` attribute.

        Returns
        -------
        :class:`SubmissionGroup`

        """
        list_of_submissions = []
        for idx, dir_item in enumerate(os.listdir(self.fs_location)):
            # convention 1: names of folders are team ids
            if not utils.is_string_number(dir_item):
                continue    
            logger.debug('Attempting make submissions from fs on team-id: {} '.format(dir_item) \
                + 'and path {}'.format(os.listdir(os.path.join(self.fs_location, dir_item))))
            team_id = dir_item

            # go inside the folder and store the file_paths of downloaded items for offline working
            # go over the items of the student team submission
            # and build items dictionary
            items = {}
            for idx, team_item in enumerate(os.listdir(os.path.join(self.fs_location, dir_item))):
                file_full_path = os.path.join(self.fs_location, dir_item, team_item)
                file_item_name = self.get_file_item_name(team_id, file_full_path)
                if file_item_name != None:
                    items[file_item_name] = {'path': file_full_path, 'downloaded': True}
                
            submission = Submission(team_id, items)
            list_of_submissions.append(submission)
        return SubmissionGroup(self.task_name, self.theme_name, list_of_submissions)

    def get_submissions(self):
        """
        Returns a :class:`SubmissionGroup` after populating it with information from
        webpage or filesystem

        Based on the method used for fetching, `url` or `fs`, the resulting :class:`SubmissionGroup`
        will differ. For example, a :class:`SubmissionGroup` created from manually made directory
        structure won't contain a url key in :attr:`~Submission.items` 

        Returns
        -------
        :class:`SubmissionGroup`

        Examples
        --------
        .. doctest::

            >>> load_submissions.get_submissions() # calling get_submissions() on load_submissions object
            SubmissionGroup(...)

        """
        # list of submission objects
        list_of_submissions = []
        if self.task_url != '':
            if self.scraper == '' or self.scraper == 'default':
                self.scraper = DefaultScraper
            elif self.scraper == 'default2019':
                self.scraper = DefaultScraper2019
            else:
                # TODO (manjrekarom): Use custom scraper
                pass

            all_submission_info_dict = self.scraper(self.task_url, self.cookie, self.types,
            before_date=self.before_date, after_date=self.after_date).scrape()
            
            # fill all data inside the submission object
            # TODO:
            for team_id, info_dict in all_submission_info_dict.items():
                # convert team_id into number
                list_of_submissions.append(Submission(int(team_id), info_dict))

        elif self.fs_location != '':
            # convert submissions array to json array
            submission_file_path = os.path.abspath(self.fs_location)
            # if path is not file
            if not os.path.isfile(submission_file_path):
                # then look if theres a file in the directory names submission.json
                if any(i == 'submission.json' for i in listdir(submission_file_path)) == True:
                    submission_file_path = os.path.join(self.fs_location, 'submission.json')
                    return SubmissionGroup.from_json(submission_file_path)
                else:
                    # else fall back to making submission_group by looking at downloaded
                    # files
                    return self.make_submissions_from_fs()
            else:
                # else make a submission_group from the file and return 
                return SubmissionGroup.from_json(submission_file_path)
        else:
            logger.exception("Neither URL nor File location found.Try again")
            raise CannotMakeSubmissionsFS()
        
        return SubmissionGroup(self.task_name, self.theme_name, list_of_submissions)


class Scraper(ABC):
    def __init__(self, task_url: str, cookie: str, types: list = ['zip', 'png', 'ipynb'],
    before_date: Union[str, datetime]='', after_date: Union[str, datetime]=''):
        self.task_url = task_url
        self.cookie = cookie
        self.types = types
        self.before_date = before_date
        self.after_date = after_date

    @abstractmethod
    def scrape(self):
        """
        Scrapes important information from the page as a dictionary
        
        The dictionary contains team_id as key and all information
        as a dictionary again if needed
        """
        raise NotImplementedError()

class NoRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        infourl = addinfourl(fp, headers, req.get_full_url())
        infourl.status = code
        infourl.code = code
        return infourl

    http_error_300 = http_error_302
    http_error_301 = http_error_302
    http_error_303 = http_error_302
    http_error_307 = http_error_302

class DefaultScraper(Scraper):
    def __init__(self, task_url: str, cookie: str, types: list = ['zip'],
    before_date='', after_date=''):
        super().__init__(task_url, cookie, types=types, before_date=before_date, after_date=after_date)

    def download(self):
        """
        Downloads and returns a given web_page after parsing it with bs4. 
        
        Raises
        ------
        ServerOrScraperException

        Returns
        -------
        :class:`BeautifulSoup`
            Web page after parsing it with beautiful soup 4
        """
        # if cookie is expired or invalid, the server makes a redirect
        # we can check if the server redirected and throw an exception
        
        # data.task_url = 'http://23.253.205.190/eyrc18/public/admin/grade/task0'
        # data.task_url = 'http://23.253.205.190/eyrc18/public/admin/grade/task1b'
        opener = urllib2.build_opener(NoRedirectHandler())
        opener.addheaders.append(('Cookie', self.cookie['name'] + '=' + self.cookie['value']))
        web_page = opener.open(self.task_url)
        # check if cookie is valid? or the request succeeded
        # 2xx is correct code
        if web_page.getcode() / 100 != 2:
            raise ServerOrScraperException()
        
        html_response = web_page.read()
        encoding = web_page.headers.get_content_charset('utf-8')
        decoded_html = html_response.decode(encoding)
        return decoded_html

    def compare_dates(self, date1, date2, method='greater'):
        """
        Returns greater or smaller date

        If default='greater', checks if date1 is greater than date2 and
        returns True

        If default='small', checks if date1 is smaller than date2 and
        returns True

        If default='equal', checks if date1 is equal to date2 and
        returns True

        Parameters
        ----------
        date1: :class:`datetime`
        date2: :class:`datetime`

        Returns
        -------
        bool

        """
        date1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S") 
        date2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S") 
        
        if method.lower() == 'greater':
            return date1 > date2
        if method.lower() == 'smaller':
            return date1 < date2
        if method.lower() == 'equal':
            return date1 == date2

    def parse_info_as_dict(self, file_item_atags_list: list, method: str='latest'):
        """
        Parse information from HTML markups of file_item atags as a dictionary
        """
        info_dict = {}
        if method=='latest':
            date_compare = 'greater'
        # if method=='old':
        #     date_compare = 'smaller'

        for idx, atag in enumerate(file_item_atags_list):
            if info_dict.get(atag.get_text(), 'False') == 'False':
                # "png" = "http://..."
                info_dict[atag.get_text()] = {'url': atag['href'], 'upload_time': atag['data-tooltip']}
            else:
                if self.compare_dates(atag['data-tooltip'], info_dict[atag.get_text()]['upload_time'], 
                method=date_compare):
                # if url['data-tooltip'] > latest_urls[url.get_text()]['data-tooltip']: 
                    info_dict[atag.get_text()]['url'] = atag['href']
                    info_dict[atag.get_text()]['upload_time'] = atag['data-tooltip']
        return info_dict
        
    def parse(self, web_page):
        """
        Parses required (as much as) information from the given webpage
        """
        parsed_web_page = BeautifulSoup(web_page, 'html.parser')
        # button (a tags actually) that says "GRADE"
        grade_team_atags_list = parsed_web_page.find_all('a', {'class': 'gradeTeam'})
        all_submission_info = {}
        # for each of the teams do this
        for grade_team_atag in grade_team_atags_list:
            # buttons (a tags actually) with names like "TXT", "PNG", etc
            file_item_atags_list = grade_team_atag.parent.parent.find_all('a', {'class': 'waves-effect'})
            
            # filter file_item_atags_list
            filtered_file_items_atags_list = list(filter(lambda file_item_atag: 
            self.types in [None, '', []] or file_item_atag.get_text().lower() in self.types, file_item_atags_list))
            
            # get {"png": {"url": ..., "upload_time": ...}, "zip": {...}}
            info_dict = self.parse_info_as_dict(filtered_file_items_atags_list)
            # add team id and info dict: {"4": {"png": {"url": ..., "upload_time": ...}, "zip": {...}}}
            all_submission_info[grade_team_atag['data-teamid']] = info_dict
        return all_submission_info

    # TODO: Accept team_ids and file urls 
    # also incorporate other data like time of download etc
    def scrape(self):
        """
        Scrape submission information from theme uploads page
        """
        # download html page
        web_page = self.download()
        return self.parse(web_page)

class DefaultScraper2019(Scraper):
    def __init__(self, task_url: str, cookie: str, types: list = ['zip'],
    before_date='', after_date=''):
        super().__init__(task_url, cookie, types=types, before_date=before_date,
        after_date=after_date)

    def download(self):
        """
        Downloads and returns a given web_page after parsing it with bs4. 
        
        Raises
        ------
        ServerOrScraperException

        Returns
        -------
        :class:`BeautifulSoup`
            Web page after parsing it with beautiful soup 4
        """
        # if cookie is expired or invalid, the server makes a redirect
        # we can check if the server redirected and throw an exception
        
        # data.task_url = 'http://23.253.205.190/eyrc18/public/admin/grade/task0'
        # data.task_url = 'http://23.253.205.190/eyrc18/public/admin/grade/task1b'
        opener = urllib2.build_opener(NoRedirectHandler())
        opener.addheaders.append(('Cookie', self.cookie['name'] + '=' + self.cookie['value']))
        web_page = opener.open(self.task_url)
        # check if cookie is valid? or the request succeeded
        # 2xx is correct code
        if web_page.getcode() / 100 != 2:
            raise ServerOrScraperException()
        
        html_response = web_page.read()
        encoding = web_page.headers.get_content_charset('utf-8')
        decoded_html = html_response.decode(encoding)
        return decoded_html

    def compare_dates(self, date1, date2, method='greater'):
        """
        Returns greater or smaller date

        If default='greater', checks if date1 is greater than date2 and
        returns True

        If default='small', checks if date1 is smaller than date2 and
        returns True

        If default='equal', checks if date1 is equal to date2 and
        returns True

        Parameters
        ----------
        date1: :class:`datetime`
        date2: :class:`datetime`

        Returns
        -------
        bool

        """
        date1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S") 
        date2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S") 
        
        if method.lower() == 'greater':
            return date1 > date2
        if method.lower() == 'smaller':
            return date1 < date2
        if method.lower() == 'equal':
            return date1 == date2

    def is_date_between_before_after(self, date_to_compare, before_date, after_date):
        if not isinstance(date_to_compare, datetime):
            date_to_compare = datetime.strptime(date_to_compare, "%Y-%m-%d %H:%M:%S")

        if before_date != '':
            if not isinstance(before_date, datetime):
                before_date = datetime.strptime(before_date, "%Y-%m-%d %H:%M:%S")
            if not date_to_compare <= before_date:
                return False

        if after_date != '':    
            if not isinstance(after_date, datetime):
                after_date = datetime.strptime(after_date, "%Y-%m-%d %H:%M:%S")
            if not date_to_compare >= after_date:
                return False
        return True

    def parse_info_as_dict(self, file_item_atags_list: list, method: str='latest'):
        """
        Parse information from HTML markups of file_item atags as a dictionary
        """
        info_dict = {}
        if method=='latest':
            date_compare = 'greater'
        # if method=='old':
        #     date_compare = 'smaller'

        for idx, atag in enumerate(file_item_atags_list):
            if not self.is_date_between_before_after(atag['title'], self.before_date,
            self.after_date):
                continue

            if info_dict.get(slugify(atag.get_text()), None) == None:
                # "png" = "http://..."
                info_dict[slugify(atag.get_text())] = {'url': atag['href'], 'upload_time': atag['title']}
            else:
                if self.compare_dates(atag['title'], info_dict[slugify(atag.get_text())]['upload_time'], 
                method=date_compare):
                # if url['data-tooltip'] > latest_urls[url.get_text()]['data-tooltip']: 
                    info_dict[slugify(atag.get_text())]['url'] = atag['href']
                    info_dict[slugify(atag.get_text())]['upload_time'] = atag['title']
        return info_dict
    
    def parse(self, web_page):
        """
        Parses required (as much as) information from the given webpage
        """
        parsed_web_page = BeautifulSoup(web_page, 'html.parser')
        # button (a tags actually) that says "GRADE"
        grade_team_atags_list = parsed_web_page.find_all('a', {'class': 'gradeTeam'})
        logger.debug('All teams to grade {}'.format(grade_team_atags_list))
        all_submission_info = {}
        # for each of the teams do this
        for grade_team_atag in grade_team_atags_list:
            # buttons (a tags actually) with names like "TXT", "PNG", etc
            file_item_atags_list = grade_team_atag.parent.parent.find_all('a', {'class': 'btn-outline-success'})
            
            # filter file_item_atags_list
            filtered_file_items_atags_list = list(filter(lambda file_item_atag: 
            self.types in [None, '', []] or slugify(file_item_atag.get_text().lower()) in self.types, file_item_atags_list))
            
            # get {"png": {"url": ..., "upload_time": ...}, "zip": {...}}
            logger.debug('Team id: {} Filtered teams with types, the items are {}'.format(
                grade_team_atag['data-teamid'], filtered_file_items_atags_list))
            info_dict = self.parse_info_as_dict(filtered_file_items_atags_list)
            # add team id and info dict: {"4": {"png": {"url": ..., "upload_time": ...}, "zip": {...}}}
            all_submission_info[grade_team_atag['data-teamid']] = info_dict
        logger.debug(all_submission_info)
        return all_submission_info

    # TODO: Accept team_ids and file urls
    # also incorporate other data like time of download etc
    def scrape(self):
        """
        Scrape submission information from theme uploads page
        """
        # download html page
        web_page = self.download()
        return self.parse(web_page)


if __name__ == "__main__":
    import doctest
    doctest.testmod()