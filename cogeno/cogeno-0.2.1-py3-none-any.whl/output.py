# Copyright 2004-2016, Ned Batchelder.
#           http://nedbatchelder.com/code/cog
# Copyright (c) 2018..2020 Bobby Noelte.
# SPDX-License-Identifier: Apache-2.0

import re

class OutputMixin(object):
    __slots__ = []

    @staticmethod
    def _b(s):
        return s.encode("latin-1")

    @staticmethod
    def _whitePrefix(strings):
        """ Determine the whitespace prefix common to all non-blank lines
            in the argument list.
        """
        # Remove all blank lines from the list
        strings = [s for s in strings if s.strip() != '']

        if not strings: return ''

        # Find initial whitespace chunk in the first line.
        # This is the best prefix we can hope for.
        pat = r'\s*'
        if isinstance(strings[0], (bytes, )):
            pat = pat.encode("utf8")
        prefix = re.match(pat, strings[0]).group(0)

        # Loop over the other strings, keeping only as much of
        # the prefix as matches each string.
        for s in strings:
            for i in range(len(prefix)):
                if prefix[i] != s[i]:
                    prefix = prefix[:i]
                    break
        return prefix

    @staticmethod
    def _reindentBlock(lines, newIndent=''):
        """ Take a block of text as a string or list of lines.
            Remove any common whitespace indentation.
            Re-indent using newIndent, and return it as a single string.
        """
        sep, nothing = '\n', ''
        if isinstance(lines, (bytes, )):
            sep, nothing = OutputMixin._b('\n'), OutputMixin._b('')
        if isinstance(lines, (str, bytes)):
            lines = lines.split(sep)
        oldIndent = OutputMixin._whitePrefix(lines)
        outLines = []
        for l in lines:
            if oldIndent:
                l = l.replace(oldIndent, nothing, 1)
            if l and newIndent:
                l = newIndent + l
            outLines.append(l)
        return sep.join(outLines)

    def _out(self, output='', dedent=False, trimblanklines=False):
        if trimblanklines and ('\n' in output):
            lines = output.split('\n')
            if lines[0].strip() == '':
                del lines[0]
            if lines and lines[-1].strip() == '':
                del lines[-1]
            output = '\n'.join(lines)+'\n'
        if dedent:
            output = OutputMixin._reindentBlock(output)

        if self._context.script_is_python():
            self._context._outstring += output
        return output

    ##
    # @brief Write text to the output.
    #
    # @param sOut The string to write to the output.
    # @param dedent If dedent is True, then common initial white space is
    #               removed from the lines in sOut before adding them to the
    #               output.
    # @param trimblanklines If trimblanklines is True,
    #                       then an initial and trailing blank line are removed
    #                       from sOut before adding them to the output.
    #
    # ``dedent`` and ``trimblanklines`` make it easier to use
    # multi-line strings, and they are only are useful for multi-line strings:
    #
    # @code
    # cogeno.out("""
    #    These are lines I
    #    want to write into my source file.
    # """, dedent=True, trimblanklines=True)
    # @endcode
    def out(self, sOut='', dedent=False, trimblanklines=False):
        return self._out(sOut, dedent, trimblanklines)

    ##
    # @brief Write text to the output with newline appended.
    #
    # @param sOut The string to write to the output.
    # @param dedent If dedent is True, then common initial white space is
    #               removed from the lines in sOut before adding them to the
    #               output.
    # @param trimblanklines If trimblanklines is True,
    #                       then an initial and trailing blank line are removed
    #                       from sOut before adding them to the output.
    #
    # @see OutputMixin::out(self, sOut='', dedent=False, trimblanklines=False)
    def outl(self, sOut='', dedent=False, trimblanklines=False):
        self._out(sOut, dedent, trimblanklines)
        self._out('\n')
