# a Pandoc filter for acronyms based on panflute.

import panflute
import sys
import re
import click

from acronyms.acronyms import Acronyms
from acronyms.index import Index
from acronyms.logging import debug, info, error


class Filter:
    """The Filter class manages the configuration of a single filter run."""

    def __init__(self):
        self.acronyms = Acronyms()
        self.index = Index()
        self.suggest = False
        self.report_error = False
        self.has_error = False

    @property
    def acronyms(self):
        return self._acronyms

    @acronyms.setter
    def acronyms(self, value):
        self._acronyms = value

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value

    @property
    def suggest(self):
        return self._suggest == True

    @suggest.setter
    def suggest(self, value):
        self._suggest = (value == True)

    @property
    def report_error(self):
        return self._report_error

    @report_error.setter
    def report_error(self, value):
        self._report_error = value

    @property
    def has_error(self):
        return self._has_error

    @has_error.setter
    def has_error(self, value):
        self._has_error = value

    def run(self, acronymfiles, doc=None):
        if acronymfiles:
            for input in acronymfiles:
                info('Loading acronyms from {}...'.format(input))
                with open(input, "r") as handle:
                    dictionary = Acronyms.Read(handle)
                    self.acronyms.merge(dictionary)
        else:
            info('No acronym definitions specified!')
        return self.process_document(doc)

    def filter_acronyms(self, element, doc):
        """The panflute filter function."""
        if type(element) == panflute.Str:
            pattern = element.text
            element.text = self.process_string_token(pattern, self.acronym_replacer)
            if self.suggest:
                suggestions = self.check_for_suggestions(pattern)
                for suggestion in suggestions:
                    info(suggestion, True)

    def process_string_token(self, token, replacer):
        """Parse the token, isolate the acronyms and pass them to the replacer function. Return the reassembled text."""
        result = ""
        while token:
            match = Filter.acronym_markup_expression().search(token)
            if match:
                (left, right) = match.span()
                result += token[0:left]
                pattern = match.group(1)
                result += replacer(pattern, token[left:right]) or ''  # pattern could be empty
                token = token[right:]
            else:
                # no match left in token
                result += token
                token = ""
        return result

    def acronym_replacer(self, pattern, matchtext):
        match_attributes = self.return_acronym_match(pattern)
        if not match_attributes:
            error('Error: invalid acronym expression "{}".'.format(pattern))
            self.has_error = True
            return matchtext
        [ key, plural, uppercase, form ] = match_attributes
        # is this an acronym?
        acronym = self.acronyms.get(key)
        if not acronym:
            if self.report_error:
                error("Error: acronym {} undefined.".format(key))
                self.has_error = True
            else:
                info("Warning: acronym {} undefined.".format(key))
            return
        # register the use of the acronym:
        count = self.index.register(acronym)
        # # is this the first use of the acronym?
        if count == 1:
            info("First use of acronym {} found.".format(key))
        else:
            debug("Acronym {} found again.".format(key))
        return self.expand_acronym(acronym, count == 1, plural, uppercase, form)

    def expand_acronym(self, acronym, firstuse, plural, uppercase, form):
        # TODO how to handle the case if all forms are empty?
        shortform = acronym.shortform
        if plural:
            shortform = "{}s".format(acronym.shortform)
        longform = acronym.longform
        if longform and plural:
            longform = "{}s".format(longform)
        if longform and uppercase:
            longform = longform.capitalize()
        explained = "{} ({})".format(longform, shortform)
        if not form:
            if firstuse:
                return explained
            return shortform
        elif form == '!':
            return explained
        elif form == '>':
            return longform
        else: # the parser checks for the allowed values
            return shortform

    def check_for_suggestions(self, pattern):
        elements = pattern.split()
        acronyms = self.acronyms.values
        results = []
        for key, acronym in acronyms.items():
            if acronym.shortform in elements:
                results.append('NOTE: "{}" in "{}" could be an acronym. Consider replacing it with [!{}].'.format( acronym.shortform, pattern, key))
        return results

    def process_document(self, doc):
        """The entry method to execute the filter."""
        # We need state in the filter function, so we create a filter function that references the filter object:

        def filter_closure(element, doc):
            return self.filter_acronyms(element, doc)

        return panflute.run_filter(filter_closure, doc=doc)

    _acronym_specification_expression = re.compile(r'^(\+?)(\^?)(\w[\w_+-]*)([\<\>\!]?)$')
    _acronym_markup_expression = re.compile(r'\[\!(.+?)\]')

    @staticmethod
    def acronym_specification_expression():
        return Filter._acronym_specification_expression

    @staticmethod
    def return_acronym_match(token):
        """return_acronym_match returns True if the token text is recognized as an acronym."""
        match = Filter.acronym_specification_expression().match(token)
        if match:
            plural = bool(match.group(1))
            uppercase = bool(match.group(2))
            key = match.group(3)
            form = match.group(4) or None
            return [ key, plural, uppercase, form ]
        return None

    @staticmethod
    def acronym_markup_expression():
        return Filter._acronym_markup_expression
