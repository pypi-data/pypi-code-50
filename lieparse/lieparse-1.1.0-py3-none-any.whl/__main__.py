#! /usr/bin/env python3
"""It is a part fron lieparse package
© 2019-2020 Vidmantas Balčytis
"""

import pkg_resources

version = pkg_resources.get_distribution("lieparse").version
print("lieparse library version {}".format(version))
