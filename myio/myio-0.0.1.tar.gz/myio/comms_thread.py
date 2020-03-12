"""This is a communicaton class to myIO-Server."""
import logging
import aiohttp
import json

# from homeassistant.util import slugify  # entity_id friendly string converter
from slugify import slugify

from homeassistant.const import (
    CONF_PASSWORD,
    CONF_USERNAME,
    CONF_HOST,
    CONF_NAME,
)

_LOGGER = logging.getLogger(__name__)
_TIMEOUT = aiohttp.ClientTimeout(total=5)


class CommsThread:
    """CommsThread can poll data from myIO Server, and send post to it"""

    async def send(self, server_data, server_status, config_entry, _post):
        """this function of CommsThread can send a post request to the myIO server,
        the response from the server will update the state, 
        and merged to the previous database.
        """
        # _LOGGER.debug("CommsThread")
        _server_name = slugify(config_entry.data[CONF_NAME])

        authenticate = aiohttp.BasicAuth(
            config_entry.data[CONF_USERNAME], config_entry.data[CONF_PASSWORD],
        )
        _invalid = False
        if server_status != "Online":
            _desc = "/d_"
        else:
            _desc = "/"
        if not config_entry.data[CONF_HOST].startswith("http://"):
            config_entry.data[CONF_HOST] = "http://" + config_entry.data[CONF_HOST]

        try:
            async with aiohttp.ClientSession(timeout=_TIMEOUT) as session:
                async with session.get(
                    config_entry.data[CONF_HOST] + _desc + "sens_out.json",
                    auth=authenticate,
                    data=_post,
                ) as response:
                    if response.status == 200:
                        if _desc == "/d_":
                            server_data = json.loads(await response.text())
                        else:
                            _temp_data = server_data
                            _temp_json = json.loads(await response.text())
                            """ Merge fresh server status to server_data"""
                            for key in _temp_data:
                                for number in _temp_data[key]:
                                    _temp_data[key][number].update(
                                        _temp_json[key][number]
                                    )
                            server_data = _temp_data.copy()
                        server_status = "Online"
                    else:
                        _LOGGER.debug("Invalid")
                        server_status = "Invalid"
                        _invalid = True
        except:
            if not _invalid:
                server_status = "Offline"

        return [server_data, server_status]
