 

from ._version import __version__


import derpconf.config as multidir_config
from derpconf.config import Config


Config.allow_environment_variables()


Config.define(
        'REMOTECV_MULTIDIR_LOADER_DIRS',
        [],
        'The list of paths where the File Loader will try to find images',
        'Loader'
)

