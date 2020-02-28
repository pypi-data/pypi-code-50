class _Versioning:
    __slots__ = ('types', 'commands', 'utilities')

    def __init__(self, release: int, build: int, request):
        self.discover(release, build, request)
    
    def discover(self, release: int, build: int, request):
        """Find a corresponding type, command and utility library
        """
        from .releases.ac24.b1600_commands import AC24Commands
        from .releases.ac24 import b1600_types
        self.types = b1600_types
        self.commands = AC24Commands(request)
