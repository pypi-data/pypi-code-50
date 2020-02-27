from precept import Argument

from top_drawer import _thesaurus

WORD = Argument(
    'word',
    help='The word to search.'
)
CASING = Argument(
    '-c', '--casing',
    choices=['snakecase', 'spinalcase'],
    default='spinalcase',
    help='The casing to apply to synonyms.'
)
PYPI = Argument(
    '--pypi',
    help='Disable validation on pypi.',
    action='store_false'
)
NPM = Argument(
    '--npm',
    help='Disable validation on npm.',
    action='store_false'
)
FULL = Argument(
    '-f', '--full',
    help='Include the invalids in the output.',
    action='store_true'
)
WORD_TYPE = Argument(
    '-w', '--word-type',
    choices=_thesaurus.WORD_TYPES,
    nargs='+',
    action='extend',
    help='Type of words to use.'
)
MODE = Argument(
    '-m', '--mode',
    choices=_thesaurus.THESAURUS_MODES,
    nargs='+',
    action='extend',
    help='Thesaurus mode.'
)
