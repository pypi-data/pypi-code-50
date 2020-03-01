# The Click application that is the front-end to the acronyms filter.

import sys
import os
import click
from acronyms.acronym_filter import Filter
from acronyms.logging import configure_logging, error as logerror, debug as logdebug, info


@click.command()
@click.option('-a', '--acronyms', envvar='PANDOC_ACRONYMS_ACRONYMS', default="", help='A file with acronym definitions in JSON format.', multiple=True)
@click.option('-v', '--verbose/--no-verbose', envvar='PANDOC_ACRONYMS_VERBOSE', default=False, help='Enable verbose output.')
@click.option('-s', '--suggest/--no-suggest', envvar='PANDOC_ACRONYMS_SUGGEST', default=False, help='Suggest marking acronyms detected in the text.')
@click.option('-e', '--error/--no-error', envvar='PANDOC_ACRONYMS_ERROR', default=False, help='Exit with an error if an undefined acronym is used.')
@click.option('-d', '--debug/--no-debug', envvar='PANDOC_ACRONYMS_DEBUG', default=False, help='Enable debug output.')
@click.version_option()
@click.argument('format', nargs=-1)
def filter(acronyms, verbose, suggest, error, debug, format):
    """The pandoc-acronyms filter."""
    filter = Filter()
    filter.suggest = suggest
    filter.report_error = error
    configure_logging(verbose, debug)
    logdebug("command line: {}".format(" ".join(sys.argv)))
    logdebug("configuration: verbose: {}, debug: {}, suggest: {}, error: {}".format(verbose, debug, suggest, error))
    try:
        filter.run(acronyms)
        if filter.has_error:
            logerror("Errors encountered.")
            sys.exit(1)
    except Exception as e:
        error(str(e))
        if verbose:
            raise e


if __name__ == '__main__':
    filter()  # pylint: disable=no-value-for-parameter
