"""phases
Usage:
  phases [-v] ...
  phases create [-f] [-p <projectfile>] [-o <outputdir>]  [-v]
  phases -h | --help
  phases --version
Options:
  -h --help                         Show this screen.
  --version                         Show version.
  -p <projectfile>                  project file [default: project.yaml]
  -o <outputdir>                    output directory [default: .]
  -f                                force to overwrite existing files
  -v                                verbose output
Examples:
  phases --version
  phases create 
  phases create -f
  phases create -f -o myOutput -p myProject.yaml
Help:
  For help using this tool, please open an issue on the Github repository:
"""

from inspect import getmembers, isclass
from docopt import docopt
from phases import __version__ as VERSION
import phases.commands
from phases.util.Logger import Logger, LogLevel

# import phases.commands as commands


def main():
    """Main CLI entrypoint."""
    options = docopt(__doc__, version=VERSION)

    if options['-v']:
        Logger.verboseLevel = LogLevel.DEBUG
    Logger.log("Phase " + VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(phases.commands, k) and v:
            module = getattr(phases.commands, k)
            phases.commands = getmembers(module, isclass)
            command = [command[1] for command in phases.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
