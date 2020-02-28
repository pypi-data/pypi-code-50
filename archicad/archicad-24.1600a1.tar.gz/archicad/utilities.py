"""GRAPHISOFT"""

from .commands import BasicCommands

class Utilities:
    """Collection of utility functions to the ARCHICAD JSON interface
    """
    def __init__(self, commands: BasicCommands):
        self.commands = commands
