
from .main import main_entry


try:
    from .version import version
except ImportError:
    version = 'git.development'
__version__ = version
