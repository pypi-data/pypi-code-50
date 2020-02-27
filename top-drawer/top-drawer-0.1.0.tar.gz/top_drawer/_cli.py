import asyncio
import functools
import sys
import os
import shutil

import appdirs
import aiohttp
import stringcase

from ruamel import yaml
from colorama import Fore

from precept import Precept, Command
from precept.console import format_table, spinner, colorize

from top_drawer._version import __version__
from top_drawer._validations import validate_pypi, validate_npm
from top_drawer._config import TopDrawerConfig
from top_drawer._thesaurus import thesaurus, reduce_thesaurus
from top_drawer import _args


UNDONE = 'undone'
undefined = object()


def format_valid(valid):
    if valid:
        return colorize('VALID', fg=Fore.GREEN)
    return colorize('INVALID', fg=Fore.RED)


class TopDrawer(Precept):
    """
    Thesaurus search and availability validators to find new package names.
    """
    prog_name = 'top-drawer'
    version = __version__
    config = TopDrawerConfig()

    def __init__(self):
        super().__init__(
            config_file=[
                'top-drawer.toml',
                os.path.join(
                    appdirs.user_config_dir(self.prog_name),
                    "config.toml"
                )
            ]
        )
        self._cache_dir = appdirs.user_cache_dir(self.prog_name)
        self._validations_cache = os.path.join(self._cache_dir, 'validations.yml')
        self._thesaurus_cache = os.path.join(self._cache_dir, 'synonyms')
        os.makedirs(self._thesaurus_cache, exist_ok=True)

    def read_cached_names(self):
        if os.path.exists(self._validations_cache):
            self.logger.debug(f'Using cache file: {self._validations_cache}')
            with open(self._validations_cache) as f:
                cached_names = yaml.load(f, Loader=yaml.RoundTripLoader)
        else:
            cached_names = {}
        return cached_names

    def write_cached_names(self, obj):
        self.logger.debug(f'Writing cache file: {self._validations_cache}')
        with open(self._validations_cache, 'w+') as cf:
            yaml.dump(obj, cf, Dumper=yaml.RoundTripDumper)

    def word_path(self, word):
        return os.path.join(self._thesaurus_cache, word)

    def read_cached_thesaurus(self, word: str):
        word_path = self.word_path(word)
        if os.path.exists(word_path):
            self.logger.debug(f'Reading synonyms from file: {word_path}')
            with open(word_path) as f:
                return yaml.safe_load(f)
        return undefined

    def write_cached_thesaurus(self, word: str, synonyms: list):
        word_path = self.word_path(word)
        self.logger.debug(f'Writing synonym file: {word_path}')
        with open(word_path, 'w+') as f:
            yaml.safe_dump(synonyms, f)

    async def get_thesaurus_from_word(self, session, word):
        if not self.config.api_key:
            self.logger.error(
                'No bighugelabs.com api key provided!\n\n'
                'Register for a free account at '
                'https://words.bighugelabs.com/account/getkey\n\n'
                'Set the api key with:\n\n'
                '  - `--api-key` argument\n'
                '  - `BHL_API_KEY` environment variable\n'
                '  - `api_key` in a config file.\n'
            )
            sys.exit(1)

        thesaurus_data = self.read_cached_thesaurus(word)

        if thesaurus_data is undefined:
            thesaurus_data = await thesaurus(
                session,
                self.config.api_key,
                word,
            )
            self.write_cached_thesaurus(word, thesaurus_data)

        return thesaurus_data

    @Command(
        _args.WORD,
        _args.CASING,
        _args.PYPI,
        _args.NPM,
        _args.FULL,
        _args.WORD_TYPE,
        _args.MODE,
        description='Search for valid words from the thesaurus definition.'
    )
    async def search(self, word, casing, pypi, npm, full, word_type, mode):
        ns = {
            'message': '',
            'done': False
        }

        def message():
            return ns['message']

        def is_done():
            return ns['done']

        cached_names = self.read_cached_names()

        # Do all the action in a callback for the spinner
        async def operate():
            await asyncio.sleep(0.001)  # Make the spinner start
            casing_method = getattr(stringcase, casing)

            async with aiohttp.ClientSession() as session:
                thesaurus_data = await self.get_thesaurus_from_word(session, word)
                synonyms = [
                    casing_method(x) for x in reduce_thesaurus(
                        thesaurus_data,
                        word_type,
                        mode
                    )
                ]

                self.logger.debug(f'Found {len(synonyms)} words.')
                validations = {
                    s: {
                        'pypi': UNDONE,
                        'npm': UNDONE
                    }
                    for s in synonyms
                }

                def _done(future, synonym='', validator=''):
                    validations[synonym][validator] = future.result()

                ns['message'] = 'Validating thesaurus ...'

                tasks = []
                for s in synonyms:
                    cached = cached_names.get(s)

                    if cached:
                        validations[s] = cached

                    if validations[s]['pypi'] == UNDONE and pypi:
                        t = asyncio.ensure_future(validate_pypi(
                            session, s
                        ))
                        # noinspection PyTypeChecker
                        t.add_done_callback(
                            functools.partial(_done,
                                              synonym=s,
                                              validator='pypi')
                        )
                        tasks.append(t)

                    if validations[s]['npm'] == UNDONE and npm:
                        t = asyncio.ensure_future(validate_npm(
                            session, s
                        ))
                        # noinspection PyTypeChecker
                        t.add_done_callback(
                            functools.partial(_done,
                                              synonym=s,
                                              validator='npm')
                        )
                        tasks.append(t)
                await asyncio.gather(*tasks)
                updated_cache = cached_names.copy()
                updated_cache.update(validations)
                self.write_cached_names(updated_cache)

            ns['done'] = True
            await asyncio.sleep(0.30)  # Wait for the spinner...
            print('\n\n', file=sys.stderr)
            valids = [
                k for k, v in validations.items()
                if (not pypi or v['pypi']) and (not npm or v['npm'])
            ]
            self.logger.debug(f'{len(valids)} valid out of {len(synonyms)}')
            await asyncio.sleep(0.30)
            if not valids:
                print('No valid results!')
                sys.exit(1)
            if not full:
                print('\n'.join(format_table(valids)))
            else:
                def formatter(key):
                    value = validations.get(key.strip())  # The key is centered
                    if (not pypi or value['pypi']) and \
                            (not npm or value['npm']):
                        fore = Fore.GREEN
                    else:
                        fore = Fore.RED
                    return colorize(key, fg=fore)
                print('\n'.join(format_table(
                    list(validations.keys()), formatting=formatter)))

        sp = spinner(is_done, message=message)
        op = operate()
        await asyncio.gather(sp, op)

    @Command(
        _args.WORD,
        _args.PYPI,
        _args.NPM,
        description='Validate a word is available.'
    )
    async def validate(self, word, pypi, npm):
        cached_names = self.read_cached_names()
        cached = cached_names.setdefault(word, {})

        async with aiohttp.ClientSession() as session:
            if pypi:
                pypi_valid = cached.get('pypi')
                if pypi_valid is None or pypi_valid == UNDONE:
                    pypi_valid = await validate_pypi(session, word)
                    cached_names[word]['pypi'] = pypi_valid
                print(f'pypi: {format_valid(pypi_valid)}')
            if npm:
                npm_valid = cached.get('npm')
                if npm_valid is None or npm_valid == UNDONE:
                    npm_valid = await validate_npm(session, word)
                    cached_names[word]['npm'] = npm_valid
                print(f'npm:  {format_valid(npm_valid)}')

        self.write_cached_names(cached_names)

    @Command(
        _args.WORD,
        description='Get the thesaurus definition from Big Huge Thesaurus.'
    )
    async def thesaurus(self, word):
        async with aiohttp.ClientSession() as session:
            data = await self.get_thesaurus_from_word(session, word)
            print(yaml.round_trip_dump(data))

    @Command(
        description='Clear the validations cache.'
    )
    async def clear_cache(self):
        shutil.rmtree(self._cache_dir)


def cli():
    c = TopDrawer()
    c.start()


if __name__ == '__main__':
    cli()
