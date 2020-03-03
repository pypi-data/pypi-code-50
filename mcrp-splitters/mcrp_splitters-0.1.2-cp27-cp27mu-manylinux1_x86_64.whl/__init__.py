from .input import InputSplitter
from .meshtal import meshtal_read


try:
    from .version import version
except ImportError:
    version = 'git.development'
__version__ = version
