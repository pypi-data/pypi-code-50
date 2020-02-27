# Global Benchmark Database (GBD)
# Copyright (C) 2019 Markus Iser, Luca Springer, Karlsruhe Institute of Technology (KIT)
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# python packages
import sqlite3
import multiprocessing

from urllib.error import URLError

# internal packages
from gbd_tool import groups, benchmark_administration, search, algo, import_data
from gbd_tool.db import Database
from gbd_tool.gbd_hash import gbd_hash
from gbd_tool.http_client import post_request, is_url, USER_AGENT_CLI
from gbd_tool.util import eprint


class GbdApi:
    # create a new GbdApi object which operates on a database. The file for this database is parameterized in the
    # constructor and cannot be changed
    def __init__(self, database):
        self.database = database
        self.db_is_url = is_url(self.database)

    # hash a CNF file
    @staticmethod
    def hash_file(path):
        return gbd_hash(path)

    # Import CSV file
    def import_file(self, path, key, source, target, delimiter):
        if self.db_is_url:
            raise NotImplementedError
        with Database(self.database) as database:
            import_data.import_csv(database, path, key, source, target, delimiter)

    # Initialize the GBD database. Create benchmark entries in database if path is given, just create a database
    # otherwise. With the constructor of a database object the __init__ method in db.py will be called
    def init_database(self, path=None, jobs=1):
        eprint('Initializing local path entries: {}'.format(path))
        if self.db_is_url:
            raise NotImplementedError
        eprint('Using {} cores'.format(jobs))
        if jobs == 1 and multiprocessing.cpu_count() > 1:
            eprint("Activate parallel initialization using --jobs={}".format(multiprocessing.cpu_count()))
        with Database(self.database) as database:
            benchmark_administration.remove_benchmarks(database)
            benchmark_administration.register_benchmarks(database, path, jobs)

    def bootstrap(self, jobs=1):
        if self.db_is_url:
            raise NotImplementedError
        with Database(self.database) as database:
            algo.algo_horn(self, database, jobs)

    # Get information of the whole database
    def get_database_info(self):
        if self.db_is_url:
            raise NotImplementedError
        with Database(self.database) as database:
            return {'name': self.database, 'version': database.get_version(), 'hash-version': database.get_hash_version()}

    # Checks weather a group exists in given database object
    def check_group_exists(self, name):
        if self.db_is_url:
            raise NotImplementedError
        with Database(self.database) as database:
            return name in groups.reflect(database)

    # Adds a group to given database representing for example an attribute of a benchmark
    def add_attribute_group(self, name, type, unique):
        if self.db_is_url:
            raise NotImplementedError
        with Database(self.database) as database:
            groups.add(database, name, unique is not None, type, unique)

    # Remove group from database
    def remove_attribute_group(self, name):
        if self.db_is_url:
            raise NotImplementedError
        with Database(self.database) as database:
            groups.remove(database, name)

    # Get all groups which are in the database
    def get_all_groups(self):
        if self.db_is_url:
            raise NotImplementedError
        with Database(self.database) as database:
            return groups.reflect(database)

    # Delete entries in groups from database, but don't delete the according group
    def clear_group(self, name):
        if self.db_is_url:
            raise NotImplementedError
        with Database(self.database) as database:
            groups.remove(database, name)

    # Retrieve information about a specific group
    def get_group_info(self, name):
        if self.db_is_url:
            raise NotImplementedError
        if name is not None:
            with Database(self.database) as database:
                return {'name': name, 'type': groups.reflect_type(database, name),
                        'uniqueness': groups.reflect_unique(database, name),
                        'default': groups.reflect_default(database, name),
                        'entries': groups.reflect_size(database, name)}
        else:
            raise ValueError('No group given')

    # Retrieve all values the given group contains
    def get_group_values(self, name):
        if self.db_is_url:
            raise NotImplementedError
        if name is not None:
            return self.query_search(None, [name], False)
        else:
            raise ValueError('No group given')

    # Associate hashes with a hash-value in a group
    def set_attribute(self, name, value, hash_list, force):
        if self.db_is_url:
            raise NotImplementedError
        with Database(self.database) as database:
            print("Setting {} to {} for benchmarks {}".format(name, value, hash_list))
            for h in hash_list:
                benchmark_administration.add_tag(database, name, value, h, force)

    # Remove association of a hash with a hash-value in a group
    def remove_attribute(self, name, value, hash_list):
        if self.db_is_url:
            raise NotImplementedError
        with Database(self.database) as database:
            for h in hash_list:
                benchmark_administration.remove_tag(database, name, value, h)

    def search(self, attribute, hashvalue):
        if self.db_is_url:
            raise NotImplementedError
        if not attribute in self.get_all_groups():
            raise ValueError("Attribute '{}' is not available".format(attribute))
        with Database(self.database) as database:
            return database.value_query("SELECT value FROM {} WHERE hash = '{}'".format(attribute, hashvalue))

    # Search for benchmarks which have to pertain to the query semantics. Before searching, some groups must be added
    # and filled with hashes and their values for the according group. Returns list of hashes
    def query_search(self, query=None, resolve=[], collapse=False):
        # remote queries
        if self.db_is_url:
            try:
                # TODO: make sure to to generate the same datastructure and resultset as with local queries:
                return set(post_request("{}/query".format(self.database), {'query': query}, {'User-Agent': USER_AGENT_CLI}))
            except URLError:
                raise ValueError('Cannot send request to host')
        # local queries
        else:
            with Database(self.database) as database:
                try:
                    resultset = search.find_hashes(database, query, resolve)
                    if collapse:
                        returnset = list()
                        for result in resultset:
                            result_list = list(result)
                            return_list = list()
                            for item in result_list:
                                item = "".join([item.split(',')[0]])
                                return_list.append(item)
                            returnset.append(tuple(return_list))
                        resultset = returnset
                except sqlite3.OperationalError as err:
                    raise ValueError("Query error for database '{}': {}".format(self.database, err))
                return resultset
