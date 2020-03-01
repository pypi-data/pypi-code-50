# Copyright 2004-2016 Ned Batchelder
#           http://nedbatchelder.com/code/cog
# Copyright (c) 2018..2020 Bobby Noelte
#
# SPDX-License-Identifier: MIT

import os
import sys
import argparse
from pathlib import Path

class Options(object):

    ##
    # @brief argument parser for options
    _parser = argparse.ArgumentParser(
                          description='Generate code with inlined Python code.')

    ##
    # @brief Configuration state of parser arguments
    # Used to detect option parser changes
    _parser_config_state = 0

    _parser_arguments = []

    @classmethod
    def _parser_add_argument(cls, *args, **kwargs):
        if args[0] not in cls._parser_arguments:
            cls._parser.add_argument(*args, **kwargs)
            cls._parser_arguments.append(args[0])
            cls._parser_config_state += 1
        return cls._parser_config_state

    @staticmethod
    def is_valid_directory(parser, arg):
        try:
            path = Path(arg).resolve()
        except:
            path = Path(arg)
        if not path.is_dir():
            parser.error('The directory {} does not exist!'.format(path))
        else:
            # File directory exists so return the directory
            return str(path)

    @staticmethod
    def is_valid_file(parser, arg):
        try:
            path = Path(arg).resolve()
        except:
            path = Path(arg)
        if not path.is_file():
            parser.error('The file {} does not exist!'.format(path))
        else:
            # File exists so return the file
            return str(path)

    def __init__(self, argv):
        self._argv = argv

        # Add arguments to parser
        self._parser_add_argument('-x', '--delete-code',
            dest='delete_code', action='store_true',
            help='Delete the generator code from the output file.')
        self._parser_add_argument('-w', '--warn-empty',
            dest='bWarnEmpty', action='store_true',
            help='Warn if a file has no generator code in it.')
        self._parser_add_argument('-n', '--encoding', nargs=1,
            dest='sEncoding', action='store', metavar='ENCODING',
            type=lambda x: self.is_valid_file(self._parser, x),
            help='Use ENCODING when reading and writing files.')
        self._parser_add_argument('-U', '--unix-newlines',
            dest='bNewlines', action='store_true',
            help='Write the output with Unix newlines (only LF line-endings).')
        self._parser_add_argument('-D', '--define', nargs=1, metavar='DEFINE',
            dest='defines', action='append',
            help='Define a global string available to your generator code.')
        self._parser_add_argument('-m', '--modules', nargs='+', metavar='DIR',
            dest='modules_paths', action='append',
            help='Use modules from modules DIR. We allow multiple')
        self._parser_add_argument('-t', '--templates', nargs='+', metavar='DIR',
            dest='templates_paths', action='append',
            help='Use templates from templates DIR. We allow multiple')
        self._parser_add_argument('-i', '--input', nargs=1, metavar='FILE',
            dest='input_file', action='store',
            type=lambda x: self.is_valid_file(self._parser, x),
            help='Get the input from FILE.')
        self._parser_add_argument('-o', '--output', nargs=1, metavar='FILE',
            dest='output_file', action='store',
            help='Write the output to FILE.')
        self._parser_add_argument('-l', '--log', nargs=1, metavar='FILE',
            dest='log_file', action='store',
            help='Log to FILE.')
        self._parser_add_argument('-k', '--lock', nargs=1, metavar='FILE',
            dest='lock_file', action='store',
            help='Use lock FILE for concurrent runs of cogeno.')

        # Defaults for argument values.
        #self._args.includePath = []
        #self._args.defines = {}
        #self._args.bNoGenerate = False
        #self._args.output_file = None
        #self._args.bWarnEmpty = False
        #self._args.delete_code = False
        #self._args.bNewlines = False
        #self._args.sEncoding = "utf-8"
        #self._args.verbosity = 2

        #self._args.modules_paths = None
        #self._args.templates_paths = None
        #self._args.bindings_paths = None
        #self._args.input_file = None
        #self._args.output_file = None
        #self._args.log_file = None
        #self._args.lock_file = None

        # Do the initial argument parse
        self._argv_parsed_with_state = 0
        self._parse_args()

    def __str__(self):
        sb = []
        for key in self._args.__dict__:
            sb.append("{key}='{value}'".format(key=key, value=self._args.__dict__[key]))
        return ', '.join(sb)

    def __repr__(self):
        return self.__str__()


    def __eq__(self, other):
        """ Comparison operator for tests to use.
        """
        return self._args.__dict__ == other._args.__dict__

    def clone(self):
        """ Make a clone of these options, for further refinement.
        """
        return copy.deepcopy(self)

    def _parse_args(self):
        if self._argv_parsed_with_state >= self._parser_config_state:
            # arguments already parsed with latest state of parser
            return

        # We skip unknown arguments to allow modules to add arguments later on
        self._args, self._args_unknown = \
            self._parser.parse_known_args(self._argv[1:])
        self._argv_parsed_with_state = self._parser_config_state
        # sanitize some of the options
        # --modules
        modules_paths = []
        if self._args.modules_paths is not None:
            paths = self._args.modules_paths
            if not isinstance(paths, list):
                paths = [paths]
            if isinstance(paths[0], list):
                paths = [item for sublist in paths for item in sublist]
            for path in paths:
                try:
                    path = Path(path).resolve()
                except FileNotFoundError:
                    # Python 3.4/3.5 will throw this exception
                    # Python >= 3.6 will not throw this exception
                    path = Path(path)
                if path.is_dir():
                    modules_paths.append(path)
                elif path.is_file():
                    modules_paths.append(path.parent)
                else:
                    print("options.py: Unknown modules path", path, "- ignored")
        self._args.modules_paths = modules_paths
        # --templates
        templates_paths = []
        if self._args.templates_paths is not None:
            paths = self._args.templates_paths
            if not isinstance(paths, list):
                paths = [paths]
            if isinstance(paths[0], list):
                paths = [item for sublist in paths for item in sublist]
            for path in paths:
                try:
                    path = Path(path).resolve()
                except FileNotFoundError:
                    # Python 3.4/3.5 will throw this exception
                    # Python >= 3.6 will not throw this exception
                    path = Path(path)
                if path.is_dir():
                    templates_paths.append(path)
                elif path.is_file():
                    templates_paths.append(path.parent)
                else:
                    print(f"options.py: Unknown templates path '{path}' - ignored")
        self._args.templates_paths = templates_paths
        # --input
        if self._args.input_file is None:
            self._args.input_file = None
        else:
            self._args.input_file = self._args.input_file[0]
        # --output
        if self._args.output_file is None:
            self._args.output_file = None
        else:
            self._args.output_file = self._args.output_file[0]
        # --log_file
        if self._args.log_file is None:
            self._args.log_file = None
        else:
            self._args.log_file = self._args.log_file[0]
        # --lock_file
        if self._args.lock_file is None:
            self._args.lock_file = None
        else:
            self._args.lock_file = self._args.lock_file[0]
        # --defines
        defines = {}
        if self._args.defines is not None:
            for define in self._args.defines:
                d = define[0].split('=')
                if len(d) > 1:
                    value = d[1]
                else:
                    value = None
                defines[d[0]] = value
            self._args.defines = defines

    def add_argument(self, *args, **kwargs):
        return self._parser_add_argument(*args, **kwargs)

    def option(self, name):
        self._parse_args()
        return getattr(self._args, name, None)


class OptionsMixin(object):
    __slots__ = []

    ##
    # @brief Get option of actual context.
    #
    # @param name Name of option
    # @return option value
    def option(self, name):
        return self._context._options.option(name)

    ##
    # @brief Add option arguments to option parser of actual context.
    #
    # Cogeno modules may add arguments to the cogeno option parser.
    # The argument variables given to cogeno are rescanned after new
    # option arguments are provided.
    #
    # @code
    # def mymodule(cogeno):
    #     if not hasattr(cogeno, '_mymodule'):
    #         cogeno._mymodule = None
    #
    #         cogeno.options_add_argument('-m', '--mymodule', metavar='FILE',
    #             dest='mymodule_file', action='store',
    #             type=lambda x: cogeno.options_is_valid_file(x),
    #             help='Load mymodule data from FILE.')
    #
    #    if getattr(cogeno, '_mymodule') is not None:
    #        return cogeno._mymodule
    #
    #    if cogeno.option('mymodule_file'):
    #        mymodule_file = cogeno.option('mymodule_file')
    #    else:
    #        cogeno.error(..., 2)
    #
    #    ...
    #    cogeno._mymodule = ...
    # @endcode
    def options_add_argument(self, *args, **kwargs):
        return self._context._options.add_argument(*args, **kwargs)

    def options_is_valid_file(self, filepath):
        return Options.is_valid_file(self._context._options._parser, filepath)

    def options_is_valid_directory(self, directorypath):
        return Options.is_valid_directory(self._context._options._parser, directorypath)
