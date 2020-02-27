# ##############################################################################
#  Author: echel0n <echel0n@sickrage.ca>
#  URL: https://sickrage.ca/
#  Git: https://git.sickrage.ca/SiCKRAGE/sickrage.git
#  -
#  This file is part of SiCKRAGE.
#  -
#  SiCKRAGE is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  -
#  SiCKRAGE is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  -
#  You should have received a copy of the GNU General Public License
#  along with SiCKRAGE.  If not, see <http://www.gnu.org/licenses/>.
# ##############################################################################


"""Custom exceptions used or raised by thetvdb
"""

__author__ = "echel0n"
__version__ = "1.9"

__all__ = ["tvdb_error", "tvdb_shownotfound", "tvdb_showincomplete", "tvdb_seasonnotfound", "tvdb_episodenotfound",
           "tvdb_attributenotfound", "tvdb_unauthorized"]


class tvdb_exception(Exception):
    """Any exception generated by thetvdb
    """
    pass


class tvdb_error(tvdb_exception):
    """An error with thetvdb.com (Cannot connect, for example)
    """
    pass


class tvdb_shownotfound(tvdb_exception):
    """Show cannot be found on thetvdb.com (non-existant show)
    """
    pass


class tvdb_showincomplete(tvdb_exception):
    """Show found but incomplete on thetvdb.com (incomplete show)
    """
    pass


class tvdb_seasonnotfound(tvdb_exception):
    """Season cannot be found on thetvdb.com
    """
    pass


class tvdb_episodenotfound(tvdb_exception):
    """Episode cannot be found on thetvdb.com
    """
    pass


class tvdb_attributenotfound(tvdb_exception):
    """Raised if an episode does not have the requested
    attribute (such as a episode name)
    """
    pass


class tvdb_unauthorized(tvdb_exception):
    """Need JWT Token
    """
    pass
