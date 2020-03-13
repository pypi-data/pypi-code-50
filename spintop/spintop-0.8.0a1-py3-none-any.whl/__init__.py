from .spintop import Spintop

import pkgutil
res = pkgutil.get_data('spintop', 'VERSION')
__version__ = res.decode()