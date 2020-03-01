# Copyright (c) 2018..2020 Bobby Noelte.
#
# SPDX-License-Identifier: Apache-2.0


class OutputMixin(object):
    __slots__ = []

    def _out(self, output='', dedent=False, trimblanklines=False):
        if trimblanklines and ('\n' in output):
            lines = output.split('\n')
            if lines[0].strip() == '':
                del lines[0]
            if lines and lines[-1].strip() == '':
                del lines[-1]
            output = '\n'.join(lines)+'\n'
        if dedent:
            output = reindentBlock(output)

        if self._context.script_is_python():
            self._context._outstring += output
        return output

    def msg(self, s):
        return self.prout("Message: "+s)

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
