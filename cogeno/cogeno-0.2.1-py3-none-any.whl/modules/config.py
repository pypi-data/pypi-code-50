# Copyright (c) 2018..2020 Bobby Noelte
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

class ConfigDB(object):

    def _extract(self, config_file):
        config_file = Path(config_file)
        if not config_file.is_file():
            raise RuntimeError(
                "Config file '{}' does not exist or is no file.".
                format(config_file))
        with config_file.open(mode = 'r', encoding = 'utf-8') as config_fd:
            for line in config_fd:
                if line.startswith('#') or not line.strip():
                    continue
                config = line.split('=')
                key = config[0].strip()
                value = config[1].strip()
                if value in ('y'):
                    value = "true"
                elif value in ('n'):
                    value = "false"
                else:
                    value = value.replace('"','')
                self._properties[key] = value
        return self._properties

    def __init__(self, config_file, *args, **kw):
        self._properties = dict(*args, **kw)
        self._extract(config_file)

    ##
    # @brief Get the value of a configuration property from .config.
    #
    # If property_name is not given in .config the default value is returned.
    #
    # @param property_name Name of the property
    # @param default Property value to return per default.
    # @return property value
    def property(self, property_name, default="<unset>"):
        property_value = self._properties.get(property_name, default)
        if property_value == "<unset>":
            raise RuntimeError(
                "config property '{}' not defined.".format(property_name))
        return property_value

    ##
    # @brief Get all config properties.
    #
    # The property names are the ones autoconf.conf.
    #
    # @return A dictionary of config properties.
    def properties(self):
        return self._properties


##
# @brief Get config properties database prepared for cogeno use.
# @return config properties database.
def configs(cogeno, force_extract = False):
    if not hasattr(cogeno, '_configdb'):
        # Make the config database a hidden attribute of the generator
        cogeno._configdb = None

        cogeno.options_add_argument('-c', '--config', metavar='FILE',
            dest='config_file', action='store',
            help='Use configuration variables from configuration FILE.')

    if getattr(cogeno, '_configdb') is not None and force_extract is False:
        return cogeno._configdb

    # config cache file
    if cogeno.option('config_file'):
        config_file = cogeno.option('config_file')
    else:
        cogeno.error("No path defined for the config file.", 2)

    cogeno._configdb = ConfigDB(config_file)

    return cogeno._configdb

