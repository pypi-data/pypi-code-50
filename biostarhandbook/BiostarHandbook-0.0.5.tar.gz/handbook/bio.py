import os
import sys

import plac

from . import genbank
from . import common
from . import metadata
from . import genotype
from . import combine
from . import file_filter
from .version import version

GENBANK, COMMON, COMBINE, METADATA = "genbank", "common", "combine", "metadata"

GENOTYPE, FILTER = "genotype", "filter"

MAPPER = {
    GENBANK: genbank.run,
    METADATA: metadata.run,
    COMMON: common.run,
    COMBINE: combine.run,
    GENOTYPE: genotype.run,
    FILTER: file_filter.run
}

COMMANDS = MAPPER.keys()

prog = os.path.split(sys.argv[0])[1]

usage = f"""
Biostar Handbook utilities: {version}

Usage: {prog} COMMAND 

    {GENOTYPE:9s}  - genotypes a BAM file
    {GENBANK:9s}  - tranforms a genbank file into other formats
    {COMMON:9s}  - finds common columns in files
    {COMBINE:9s}  - combines kallisto output files
    {METADATA:9s}  - parses NCBI yaml files
    {FILTER:9s}  - filter lines by matching in target file
    
Get more help on each command with:

    bio COMMAND 
"""


@plac.annotations(
    cmd="command"
)
def run(*cmd):

    target = cmd[0].lower() if cmd else None

    # Invalid command.
    if target not in COMMANDS:
        print(f"{usage}", file=sys.stderr)
        if target is not None:
            print(f"*** Invalid command: {target}", file=sys.stderr)
            sys.exit(1)
        else:
            sys.exit(0)

    if len(cmd) == 1:
        cmd = (cmd[0], '-h',)
    try:
        # Find the function to call
        func = MAPPER[target]
        plac.call(func, cmd[1:])
    except KeyboardInterrupt:
        sys.exit(0)  # or 1, or whatever


run.add_help = False


def main():
    plac.call(run)


if __name__ == '__main__':
    main()
