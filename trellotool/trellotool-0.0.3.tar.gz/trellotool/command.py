#!/usr/bin/env python
#
# command.py - really basic command line processing library
#
# Copyright (C) 2020 Michael Davies <michael@the-davies.net>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
# Or try here: http://www.fsf.org/copyleft/gpl.html

from trellotool import utils


class Command:

    def __init__(self, name):
        self.commands = {}
        self.default_func = None
        self.name = name
        self.add('help', self.help, '- Display help information')

    def set_default(self, func):
        self.default_func = func

    def add(self, command, func, help_text=None, valid_args=None):
        if utils.debug:
            print("Registering '{}' to {}".format(command, func))
        self.commands[command] = {'func': func,
                                  'valid_args': valid_args,
                                  'help_text': help_text}
        if utils.debug:
            self.show_jumptable()
            print("\n")

    def parse(self, args=None):

        # Subcommands can be valid by themselves, but might not be.
        # If a default_func has been set, we'll invoke it.
        # TODO(mrda): Need an additional check for callable
        if args is None:
            if self.default_func is not None:
                self.default_func()
            else:
                self.usage()
            return

        # Parse what we've been given and try to invoke the registered function
        command = args[0]
        rest = args[1:]

        if utils.debug:
            print("Parsing: {} ( {} )".format(command, rest))

        try:
            func = self.commands[command]['func']
            if rest is None or len(rest) == 0:
                func()
            else:
                func(rest)

        except KeyError as e:
            print("Unknown subcommand: {}".format(", ".join(args)))
            self.usage()
        except TypeError as e:
            print("Wrong number of arguments for '{}'".format(command))
            self.usage()
        except Exception as e:
            print("Problem invoking subcommand '{}' ({})".format(command, e))
            self.usage()

    def help(self):
        self.usage()
        for k in sorted(self.commands):
            help = self.commands[k]['help_text']
            if help is None:
                print(k)
            else:
                print(k, help)

    def usage(self):
        print("Available commands for {} are: {}".
              format(self.name, ', '.join(k for k in sorted(self.commands))))

    def usage_for_cmd(self, cmd):
        print(self.commands[cmd]['help_text'])

    def get_commands(self):
        return sorted(self.commands.keys())

    def show_jumptable(self):
        print("==== Jump table for {} ====".format(self.name))
        for k, v in self.commands.items():
            print("{} {} {} {}".format(k, v[0], v[0].__name__,
                                       v[0].__module__))
