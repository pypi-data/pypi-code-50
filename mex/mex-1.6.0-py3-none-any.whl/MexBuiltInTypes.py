# -*- coding: utf-8 -*-

import nwae.utils.Log as lg
from inspect import getframeinfo, currentframe


class MexBuiltInTypes:

    MEX_TYPE_FLOAT = 'float'
    MEX_TYPE_INT = 'int'
    # String format and will not remove leading 0's
    MEX_TYPE_NUMBER = 'number'
    # Like number type and allow '-'
    MEX_TYPE_ACCOUNT_NUMBER = 'account_number'
    # e.g. 10:12:36, 12:15
    MEX_TYPE_TIME = 'time'
    MEX_TYPE_DATETIME = 'datetime'
    MEX_TYPE_USERNAME = 'username'
    MEX_TYPE_USERNAME_NONWORD = 'username_nonword'
    # e.g. me@gmail.com
    MEX_TYPE_EMAIL = 'email'
    # e.g. https://google.com/folder/?param1=value1&param2=value2
    MEX_TYPE_URI = 'uri'
    # Any Latin string
    MEX_TYPE_STR_EN = 'str-en'
    # Any Chinese string
    MEX_TYPE_STR_CN = 'str-zh-cn'
    # Any Hangul string
    MEX_TYPE_STR_KO = 'str-ko'
    # Any Thai string
    MEX_TYPE_STR_TH = 'str-th'
    # Any Vietnamese string
    MEX_TYPE_STR_VI = 'str-vi'

    #
    # Regex Constants
    #
    USERNAME_CHARS               = 'a-zA-Z0-9_.\-'
    USERNAME_ALLOWED_START_CHARS = 'a-zA-Z0-9'
    USERNAME_ALLOWED_END_CHARS   = 'a-zA-Z0-9_'
    # These characters need to be bracketed if found in mex expressions
    COMMON_REGEX_CHARS = ('*', '+', '[', ']', '{', '}', '|', '$', '^')
    CHARS_VIETNAMESE_LOWER = 'ăâàằầảẳẩãẵẫáắấạặậêèềẻểẽễéếẹệìỉĩíịôơòồờỏổởõỗỡóốớọộợưùừủửũữúứụựđýỳỷỹỵ'
    CHARS_VIETNAMESE = CHARS_VIETNAMESE_LOWER + CHARS_VIETNAMESE_LOWER.upper()

    #
    # Regex Expressions
    #
    # There are internal braces '(', and ')' but this is not a problem
    # since the outer brace will be returned first in re.match()
    REGEX_URI = '(http|ws|file)[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+[^.,，。 ]'
    # Must have mix of character and number
    # Must have "greedy" matching using '*" in front and at the back
    REGEX_USERNAME = \
        '([' + USERNAME_ALLOWED_START_CHARS + ']+[' + USERNAME_CHARS + ']*[' + USERNAME_ALLOWED_END_CHARS + ']+)'
    # Must have both characters and numbers/punctuations
    # Must have "greedy" matching using '*" in front and at the back
    REGEX_USERNAME_NONWORD = \
        '([a-zA-Z]+[0-9_.\-]+[' + USERNAME_CHARS + ']*[' + USERNAME_ALLOWED_END_CHARS + ']+)' + '|' + \
        '([0-9]+[a-zA-Z_.\-]+[' + USERNAME_CHARS + ']*[' + USERNAME_ALLOWED_END_CHARS + ']+)'

    #
    # Language postfixes, for right side params
    #
    COMMON_EXPRESSION_POSTFIXES = {
        'all':   ['=', ' ='],
        'zh-cn': ['是'],
        'en':    [' is', ' are'],
        'ko':    ['는', '은', '가', '이'],
        'th':    ['คือ'],
        'vi':    [' là', ' la']
    }
    DEFAULT_EXPRESSION_POSTFIXES = []
    for lang in ['all', 'en', 'zh-cn']:
        for w in COMMON_EXPRESSION_POSTFIXES[lang]:
            DEFAULT_EXPRESSION_POSTFIXES.append(w)

    TERM_LEFT = 'left'
    TERM_RIGHT = 'right'

    @staticmethod
    def get_mex_built_in_types():
        #
        # Mapping of regular expressions to data type, you may pass in your custom one at constructor
        #
        return {
            MexBuiltInTypes.MEX_TYPE_FLOAT: {
                MexBuiltInTypes.TERM_LEFT: [
                    # float type. Left of variable expression
                    '.*[^0-9\-]+([+\-]*[0-9]+[.][0-9]*)',
                    # float type. Left of variable expression at the start of sentence
                    '^([+\-]*[0-9]+[.][0-9]*)',
                    # float type must also support int type
                    # int type. Left of variable expression
                    '.*[^0-9\-]+([+\-]*[0-9]+)',
                    # int type. Left of variable expression at the start of sentence
                    '^([+\-]*[0-9]+)'
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # float type. Right of non-empty variable expression
                    '([+\-]*[0-9]+[.][0-9]*).*',
                    # float type must also support int type
                    # int type. Right of non-empty variable expression
                    '([+\-]*[0-9]+).*'
                ]
            },
            MexBuiltInTypes.MEX_TYPE_INT: {
                MexBuiltInTypes.TERM_LEFT: [
                    # Left of variable expression
                    '.*[^0-9\-]+([+\-]*[0-9]+)',
                    # Left of variable expression at the start of sentence
                    '^([+\-]*[0-9]+)'
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # Right of non-empty variable expression
                    '([+\-]*[0-9]+).*'
                ]
            },
            MexBuiltInTypes.MEX_TYPE_NUMBER: {
                MexBuiltInTypes.TERM_LEFT: [
                    # Left of variable expression
                    '.*[^0-9\-]+([+\-]*[0-9]+)',
                    # Left of variable expression at the start of sentence
                    '^([+\-]*[0-9]+)'
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # Right of non-empty variable expression
                    '([+\-]*[0-9]+).*'
                ]
            },
            MexBuiltInTypes.MEX_TYPE_ACCOUNT_NUMBER: {
                MexBuiltInTypes.TERM_LEFT: [
                    # Left of variable expression, with trailing '-' removed
                    '.*[^0-9\-]+([0-9]+[0-9\-]*)',
                    # Left of variable expression at the start of sentence, with trailing '-' removed
                    '^([0-9]+[0-9\-]*)'
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # Right of non-empty variable expression
                    '([0-9]+[0-9\-]*).*'
                ]
            },
            MexBuiltInTypes.MEX_TYPE_TIME: {
                MexBuiltInTypes.TERM_LEFT: [
                    # HHMMSS. Check this first
                    # HHMMSS. Left of variable expression
                    '.*[^0-9]+([0-9]+[:][0-9]+[:][0-9]+)',
                    # HHMMSS. Left of variable expression at the start of sentence
                    '^([0-9]+[:][0-9]+[:][0-9]+)',
                    # HHMM. Check this only after checking HHMMSS
                    # HHMM. Left of variable expression
                    '.*[^0-9]+([0-9]+[:][0-9]+)',
                    # HHMM. Left of variable expression at the start of sentence
                    '^([0-9]+[:][0-9]+)',
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # HHMMSS. Right of non-empty variable expression
                    '([0-9]+[:][0-9]+[:][0-9]+).*',
                    # HHMM. Right of non-empty variable expression
                    '([0-9]+[:][0-9]+).*'
                ]
            },
            MexBuiltInTypes.MEX_TYPE_DATETIME: {
                MexBuiltInTypes.TERM_LEFT: [
                    # "yyyymmdd HHMMSS". Check this first
                    # HHMMSS. Left of variable expression
                    '.*[^0-9]+([0-9]{4}[-]*[0-1][0-9][-*][0-3][0-9][ ]+[0-9]+[:][0-9]+[:][0-9]+)',
                    # "yyyymmdd HHMMSS". Left of variable expression at the start of sentence
                    '^([0-9]{4}[-]*[0-1][0-9][-]*[0-3][0-9][ ]+[0-9]+[:][0-9]+[:][0-9]+)',
                    # "yyyymmdd HHMM". Check this only after checking "yyyymmdd HHMMSS"
                    # "yyyymmdd HHMM". Left of variable expression
                    '.*[^0-9]+([0-9]{4}[-]*[0-1][0-9][-]*[0-3][0-9][ ]+[0-9]+[:][0-9]+)',
                    # "yyyymmdd HHMM". Left of variable expression at the start of sentence
                    '^([0-9]{4}[-]*[0-1][0-9][-]*[0-3][0-9][ ]+[0-9]+[:][0-9]+)',
                    # "yyyymmdd". Left of variable expression
                    '.*[^0-9]+([0-9]{4}[-]*[0-1][0-9][-]*[0-3][0-9])',
                    # "yyyymmdd". Left of variable expression at the start of sentence
                    '^([0-9]{4}[-]*[0-1][0-9][-]*[0-3][0-9])',
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # "yyyymmdd HHMMSS". Right of non-empty variable expression
                    '([0-9]{4}[-]*[0-1][0-9][-*][0-3][0-9][ ]+[0-9]+[:][0-9]+[:][0-9]+).*',
                    # "yyyymmdd HHMM". Right of non-empty variable expression
                    '([0-9]{4}[-]*[0-1][0-9][-*][0-3][0-9][ ]+[0-9]+[:][0-9]+).*',
                    # "yyyymmdd"". Right of non-empty variable expression
                    '([0-9]{4}[-]*[0-1][0-9][-*][0-3][0-9]).*',
                ]
            },
            MexBuiltInTypes.MEX_TYPE_USERNAME: {
                MexBuiltInTypes.TERM_LEFT: [
                    # Left of variable expression
                    '.*[^' + MexBuiltInTypes.USERNAME_CHARS + ']+' + '(' + MexBuiltInTypes.REGEX_USERNAME + ').*',
                    # Left of variable expression at the start of sentence
                    '^(' + MexBuiltInTypes.REGEX_USERNAME + ')'
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # Right of non-empty variable expression
                    # Note that if given math expressions are nothing or '', then
                    # 'email@x.com' will be returned correctly on the left side but
                    # the right side will return 'l@x.com'.
                    # The user needs to choose the right one
                    '(' + MexBuiltInTypes.REGEX_USERNAME + ').*'
                ]
            },
            MexBuiltInTypes.MEX_TYPE_USERNAME_NONWORD: {
                MexBuiltInTypes.TERM_LEFT: [
                    # Left of variable expression
                    '.*[^' + MexBuiltInTypes.USERNAME_CHARS + ']+' + '(' + MexBuiltInTypes.REGEX_USERNAME_NONWORD + ').*',
                    # Left of variable expression at the start of sentence
                    '^(' + MexBuiltInTypes.REGEX_USERNAME_NONWORD + ')'
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # Right of non-empty variable expression
                    # Note that if given math expressions are nothing or '', then
                    # 'email@x.com' will be returned correctly on the left side but
                    # the right side will return 'l@x.com'.
                    # The user needs to choose the right one
                    '(' + MexBuiltInTypes.REGEX_USERNAME_NONWORD + ').*'
                ]
            },
            MexBuiltInTypes.MEX_TYPE_EMAIL: {
                MexBuiltInTypes.TERM_LEFT: [
                    # Left of variable expression
                    '.*[^' + MexBuiltInTypes.USERNAME_CHARS + ']+' + '(' + MexBuiltInTypes.REGEX_USERNAME + '[@][a-zA-Z0-9]+[.][a-zA-Z]+)',
                    # Left of variable expression at the start of sentence
                    '^(' + MexBuiltInTypes.REGEX_USERNAME + '[@][a-zA-Z0-9]+[.][a-zA-Z]+)'
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # Right of non-empty variable expression
                    # Note that if given math expressions are nothing or '', then
                    # 'email@x.com' will be returned correctly on the left side but
                    # the right side will return 'l@x.com'.
                    # The user needs to choose the right one
                    '(' + MexBuiltInTypes.REGEX_USERNAME + '[@][a-zA-Z0-9]+[.][a-zA-Z]+).*'
                ]
            },
            MexBuiltInTypes.MEX_TYPE_URI: {
                MexBuiltInTypes.TERM_LEFT: [
                    # Left of variable expression
                    '.*(' + MexBuiltInTypes.REGEX_URI + ')',
                    # Left of variable expression at the start of sentence
                    '^(' + MexBuiltInTypes.REGEX_URI + ')'
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # Right of non-empty variable expression
                    # Note that if given math expressions are nothing or '', then
                    # 'email@x.com' will be returned correctly on the left side but
                    # the right side will return 'l@x.com'.
                    # The user needs to choose the right one
                    '(' + MexBuiltInTypes.REGEX_URI + ').*'
                ]
            },
            MexBuiltInTypes.MEX_TYPE_STR_EN: {
                MexBuiltInTypes.TERM_LEFT: [
                    # Left of variable expression
                    '.*[^a-zA-Z]+([a-zA-Z]+)',
                    # Left of variable expression at the start of sentence
                    '^([a-zA-Z]+)'
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # Right of non-empty variable expression
                    '([a-zA-Z]+).*'
                ]
            },
            MexBuiltInTypes.MEX_TYPE_STR_CN: {
                MexBuiltInTypes.TERM_LEFT: [
                    # Left of variable expression
                    '.*[^\u4e00-\u9fff]+([\u4e00-\u9fff]+)',
                    # Left of variable expression at the start of sentence
                    '^([\u4e00-\u9fff]+)'
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # Right of non-empty variable expression
                    '([\u4e00-\u9fff]+).*'
                ]
            },
            MexBuiltInTypes.MEX_TYPE_STR_KO: {
                MexBuiltInTypes.TERM_LEFT: [
                    # Left of variable expression
                    '.*[^\u1100-\u11ff\uac00-\ud7af]+([\u1100-\u11ff\uac00-\ud7af]+)',
                    # Left of variable expression at the start of sentence
                    '^([\u1100-\u11ff\uac00-\ud7af]+)'
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # Right of non-empty variable expression
                    '([\u1100-\u11ff\uac00-\ud7af]+).*'
                ]
            },
            MexBuiltInTypes.MEX_TYPE_STR_TH: {
                MexBuiltInTypes.TERM_LEFT: [
                    # Left of variable expression
                    '.*[^\u0e00-\u0e5b]+([\u0e00-\u0e5b]+)',
                    # Left of variable expression at the start of sentence
                    '^([\u0e00-\u0e5b]+)'
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # Right of non-empty variable expression
                    '([\u0e00-\u0e5b]+).*'
                ]
            },
            MexBuiltInTypes.MEX_TYPE_STR_VI: {
                MexBuiltInTypes.TERM_LEFT: [
                    # Left of variable expression
                    '.*[^a-zA-Z' + MexBuiltInTypes.CHARS_VIETNAMESE + ']+([a-zA-Z' + MexBuiltInTypes.CHARS_VIETNAMESE + ']+)',
                    # Left of variable expression at the start of sentence
                    '^([a-zA-Z' + MexBuiltInTypes.CHARS_VIETNAMESE + ']+)'
                ],
                MexBuiltInTypes.TERM_RIGHT: [
                    # Right of non-empty variable expression
                    '([a-zA-Z' + MexBuiltInTypes.CHARS_VIETNAMESE + ']+).*'
                ]
            },
        }

    def __init__(self):
        return

