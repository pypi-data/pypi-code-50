import copy, logging, unicodedata, yaml, os
import re
from dateutil import tz, parser

logger = logging.getLogger('datefinder')


class DateFinder(object):
    """
    Locates dates in a text
    """

    def __init__(self, base_date=None):
        self.base_date = base_date

        dirname = os.path.dirname(os.path.dirname(__file__))
        filename = os.path.join(dirname, 'config/datefinder.yaml')
        with open(filename) as file:
            self.settings = yaml.load(file)
            file.close()

        self.DIGITS_MODIFIER_PATTERN = self.settings['DIGITS_MODIFIER_PATTERN']
        self.DIGITS_PATTERN = self.settings['DIGITS_PATTERN']
        self.DAYS_PATTERN = self.settings['DAYS_PATTERN']
        self.MONTHS_PATTERN = self.settings['MONTHS_PATTERN']
        self.TIMEZONES_PATTERN = self.settings['TIMEZONES_PATTERN']
        self.NA_TIMEZONES_PATTERN = self.settings['NA_TIMEZONES_PATTERN']
        self.DELIMITERS_PATTERN = self.settings['DELIMITERS_PATTERN']
        self.TIME_PERIOD_PATTERN = self.settings['TIME_PERIOD_PATTERN']
        self.EXTRA_TOKENS_PATTERN = self.settings['EXTRA_TOKENS_PATTERN']
        self.RELATIVE_PATTERN = self.settings['RELATIVE_PATTERN']
        self.TIME_SHORTHAND_PATTERN = self.settings['TIME_SHORTHAND_PATTERN']
        self.UNIT_PATTERN = self.settings['UNIT_PATTERN']
        self.STRIP_CHARS = self.settings['STRIP_CHARS']
        self.REPLACEMENTS = self.settings['REPLACEMENTS']
        self.TIMEZONE_REPLACEMENTS = self.settings['TIMEZONE_REPLACEMENTS']
        self.TRANSLATIONS = self.settings['TRANSLATIONS']

        self.ALL_TIMEZONES_PATTERN = self.TIMEZONES_PATTERN + '|' + self.NA_TIMEZONES_PATTERN

        ## Time pattern is used independently, so specified here.
        self.TIME_PATTERN = """
        (?P<time>
            ## Captures in format XX:YY(:ZZ) (PM) (EST)
            (
                (?P<hours>\d{{1,2}})
                \:
                (?P<minutes>\d{{1,2}})
                (\:(?P<seconds>\d{{1,2}}))?
                ([\.\,](?P<microseconds>\d{{1,6}}))?
                \s*
                (?P<time_periods>{time_periods})?
                \s*
                (?P<timezones>{timezones})?
            )
            |
            ## Captures in format 11 AM (EST)
            ## Note with single digit capture requires time period
            (
                ## regex in lambda bug: Note re module does not allow repeated group names but regex module does
                (?P<hours2>\d{{1,2}})
                \s*
                (?P<time_periods2>{time_periods})
                \s*
                (?P<timezones2>{timezones})*
            )
        )
        """
        self.TIME_PATTERN = self.TIME_PATTERN.format(
            time_periods=self.TIME_PERIOD_PATTERN,
            timezones=self.ALL_TIMEZONES_PATTERN
        )
        self.TIME_REGEX = re.compile(self.TIME_PATTERN, re.IGNORECASE | re.MULTILINE | re.UNICODE | re.DOTALL | re.VERBOSE)

        self.DATES_PATTERN = """
        (
            (
                {time}
                |
                ## Grab any digits
                (?P<digits_modifier>{digits_modifier})
                |
                (?P<digits>{digits})
                |
                (?P<days>{days})
                |
                (?P<months>{months})
                |
                ## Delimiters, ie Tuesday[,] July 18 or 6[/]17[/]2008
                ## as well as whitespace
                (?P<delimiters>{delimiters})
                |
                ## These tokens could be in phrases that dateutil does not yet recognize
                ## Some are US Centric
                (?P<extra_tokens>{extra_tokens})
            ## We need at least three items to match for minimal datetime parsing
            ## ie 10pm
            ){{3,}}
        )
        """
        self.DATES_PATTERN = self.DATES_PATTERN.format(
            time=self.TIME_PATTERN,
            digits=self.DIGITS_PATTERN,
            digits_modifier=self.DIGITS_MODIFIER_PATTERN,
            days=self.DAYS_PATTERN,
            months=self.MONTHS_PATTERN,
            delimiters=self.DELIMITERS_PATTERN,
            extra_tokens=self.EXTRA_TOKENS_PATTERN
        )
        self.DATE_REGEX = re.compile(self.DATES_PATTERN, re.IGNORECASE | re.MULTILINE | re.UNICODE | re.DOTALL | re.VERBOSE)

    def find_dates(self, text, source=False, index=False, strict=False):

        for date_string, indices, captures in self.extract_date_strings(text, strict=strict):
            as_dt = self.parse_date_string(date_string, captures)
            if as_dt is None:
                ## Dateutil couldn't make heads or tails of it
                ## move on to next
                continue

            returnables = (as_dt,)
            if source:
                returnables = returnables + (date_string,)
            if index:
                returnables = returnables + (indices,)

            if len(returnables) == 1:
                returnables = returnables[0]
            yield returnables

    def _find_and_replace(self, date_string, captures):
        """
        :warning: when multiple tz matches exist the last sorted capture will trump
        :param date_string:
        :return: date_string, tz_string
        """
        # add timezones to replace
        cloned_replacements = copy.copy(self.REPLACEMENTS)  # don't mutate
        # for tz_string in captures.get('timezones', []):  # regex in lambda bug
        #    cloned_replacements.append({tz_string: ' '})  # regex in lambda bug
        tz_string = captures.get('timezones')  # regex in lambda bug
        if tz_string is not None:  # regex in lambda bug
            cloned_replacements.append({tz_string: ' '})  # regex in lambda bug

        date_string = date_string.lower()
        for item in cloned_replacements:
            key = list(item.keys())[0]
            replacement = item[key]
            # we really want to match all permutations of the key surrounded by whitespace chars except one
            # for example: consider the key = 'to'
            # 1. match 'to '
            # 2. match ' to'
            # 3. match ' to '
            # but never match r'(\s|)to(\s|)' which would make 'october' > 'ocber'
            date_string = re.sub(r'(^|\s)' + key + '(\s|$)', replacement, date_string, flags=re.IGNORECASE)

        # Translations support - Change month names to standard english.
        for item in self.TRANSLATIONS:
            key = list(item.keys())[0]
            replacement = item[key]
            date_string = re.sub(key, replacement, date_string, flags=re.IGNORECASE)

        # return date_string, self._pop_tz_string(sorted(captures.get('timezones', [])))  # regex in lambda bug, also Sorting is not needed
        return date_string, self._pop_tz_string([captures.get('timezones', '')])  # regex in lambda bug

    def _pop_tz_string(self, list_of_timezones):
        try:
            tz_string = list_of_timezones.pop()
            # make sure it's not a timezone we
            # want replaced with better abbreviation
            return self.TIMEZONE_REPLACEMENTS.get(tz_string, tz_string)
        except IndexError:
            return ''
        except Exception as e:  # Exception handling for re.groupdict() instead of regex.capturesdict()
            logger.debug(e)
            return ''

    def _add_tzinfo(self, datetime_obj, tz_string):
        """
        take a naive datetime and add dateutil.tz.tzinfo object
        :param datetime_obj: naive datetime object
        :return: datetime object with tzinfo
        """
        if datetime_obj is None:
            return None

        tzinfo_match = tz.gettz(tz_string)
        return datetime_obj.replace(tzinfo=tzinfo_match)

    def parse_date_string(self, date_string, captures):
        # For well formatted string, we can already let dateutils parse them
        # otherwise self._find_and_replace method might corrupt them
        try:
            as_dt = parser.parse(date_string, default=self.base_date)
        except ValueError:
            # replace tokens that are problematic for dateutil
            date_string, tz_string = self._find_and_replace(date_string, captures)

            ## One last sweep after removing
            date_string = date_string.strip(self.STRIP_CHARS)
            ## Match strings must be at least 3 characters long
            ## < 3 tends to be garbage
            if len(date_string) < 3:
                return None

            try:
                logger.debug('Parsing {0} with dateutil'.format(date_string))
                as_dt = parser.parse(date_string, default=self.base_date)
            except Exception as e:
                logger.debug(e)
                as_dt = None
            if tz_string:
                as_dt = self._add_tzinfo(as_dt, tz_string)
        except Exception as e:  # Catching unknown exceptions
            logger.debug(e)
            return None
        return as_dt

    def extract_date_strings(self, text, strict=False):
        """
        Scans text for possible datetime strings and extracts them
        source: also return the original date string
        index: also return the indices of the date string in the text
        strict: Strict mode will only return dates sourced with day, month, and year
        """
        for match in self.DATE_REGEX.finditer(text):
            match_str = match.group(0)
            indices = match.span(0)

            ## Get individual group matches
            # captures = match.capturesdict()  # regex in lambda bug
            captures = match.groupdict()  # regex in lambda bug
            time = captures.get('time')
            digits = captures.get('digits')
            digits_modifiers = captures.get('digits_modifiers')
            days = captures.get('days')
            months = captures.get('months')
            timezones = captures.get('timezones')
            delimiters = captures.get('delimiters')
            time_periods = captures.get('time_periods')
            extra_tokens = captures.get('extra_tokens')

            if strict:
                complete = False
                ## 12-05-2015
                if len(digits) == 3:
                    complete = True
                ## 19 February 2013 year 09:10
                elif (len(months) == 1) and (len(digits) == 2):
                    complete = True

                if not complete:
                    continue

            ## sanitize date string
            ## replace unhelpful whitespace characters with single whitespace
            match_str = re.sub('[\n\t\s\xa0]+', ' ', match_str)
            match_str = match_str.strip(self.STRIP_CHARS)

            ## Save sanitized source string
            yield match_str, indices, captures


def find_dates(
    text,
    source=False,
    index=False,
    strict=False,
    base_date=None
    ):
    """
    Extract datetime strings from text
    :param text:
        A string that contains one or more natural language or literal
        datetime strings
    :type text: str|unicode
    :param source:
        Return the original string segment
    :type source: boolean
    :param index:
        Return the indices where the datetime string was located in text
    :type index: boolean
    :param strict:
        Only return datetimes with complete date information. For example:
        `July 2016` of `Monday` will not return datetimes.
        `May 16, 2015` will return datetimes.
    :type strict: boolean
    :param base_date:
        Set a default base datetime when parsing incomplete dates
    :type base_date: datetime
    :return: Returns a generator that produces :mod:`datetime.datetime` objects,
        or a tuple with the source text and index, if requested
    """
    date_finder = DateFinder(base_date=base_date)
    return date_finder.find_dates(text, source=source, index=index, strict=strict)
