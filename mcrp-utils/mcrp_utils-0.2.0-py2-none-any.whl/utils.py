import re

newline_re = re.compile('[\r\n]+')


def shorten(s, N=80):
    """
    Return short representation of string s.

    If len(s) <= N return the whole s. Otherwise return string containing the
    begin and end of s.
    """
    if len(s) <= N:
        return s[:]
    else:
        l = (N - 5)/2
        return '{} ... {}'.format(s[:l], s[-l:])


def newlineindex(mlstring, start=0):
    """
    For the multi-line string ``mlstring`` Return two indices, for the end of
    the 1-st line and start of the next one.
    """
    global newline_re
    m = newline_re.search(mlstring, start)
    return m.start(), m.end()


def nol(mlstring, start=None, end=None):
    """
    Return number of lines in the multi-line string ``mlstring``.

    Optional arguments ``start`` and ``end`` have the same meaning as in
    a string's ``count`` method.
    """
    if start is None:
        start = 0
    if end is None:
        end = len(mlstring)
    if '\r' in mlstring:
        return mlstring.count('\r', start, end) + 1
    else:
        return mlstring.count('\n', start, end) + 1


def zip_columns(c1, c2, valign='t'):
    """
    Concatenate lines from iterables c1 and c2 together and return a tuple of
    obtained lines. The length of the returned tuple is max(len(c1), len(c2)).

    If ``c1`` or ``c2`` has less elements than the other onve, it is augmented
    with empty strings. Whether the empty strings are added at the begin or
    to the end -- depends on the optional argument ``valign``.

    ``valign`` is a character specifying the vertical alignment of the column
    with less elements. Can be ``t``, ``b`` or ``c``.
    """

    # Make c1 and c2 the same length
    c1 = tuple(c1)
    c2 = tuple(c2)
    if len(c1) != len(c2):
        l1 = len(c1)
        l2 = len(c2)
        dl = abs(l1 - l2)
        if valign == 't':
            dt1 = ()
            dt2 = ('', ) * dl
        elif valign == 'b':
            dt1 = ('', ) * dl
            dt2 = ()
        elif valign == 'c':
            dl1 = dl / 2
            dl2 = dl - dl1
            dt1 = ('', ) * dl1
            dt2 = ('', ) * dl2
        else:
            raise NotImplementedError('Unknown vertical alignment', valign)
        if l1 > l2:
            c2 = dt1 + c2 + dt2
        else:
            c1 = dt1 + c1 + dt2

    w1 = max(len(l) for l in c1)
    w2 = max(len(l) for l in c2)
    f = '{{:<{}s}}{{:<{}s}}'.format(w1, w2)
    return (f.format(*s) for s in zip(c1, c2))
