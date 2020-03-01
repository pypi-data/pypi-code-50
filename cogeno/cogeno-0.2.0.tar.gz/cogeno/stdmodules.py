# Copyright (c) 2018..2020 Bobby Noelte.
# SPDX-License-Identifier: Apache-2.0

##
# Make relative import work also with __main__
if __package__ is None or __package__ == '':
    # use current directory visibility
    from modules.edtsdatabase import edts as edtsdatabase_edts
    from modules.cmake import cmake as cmakedb_cmake
    from modules.config import configs as configdb_configs
else:
    # use current package visibility
    from .modules.edtsdatabase import edts as edtsdatabase_edts
    from .modules.cmake import cmake as cmakedb_cmake
    from .modules.config import configs as configdb_configs


class StdModulesMixin(object):
    __slots__ = []

    ##
    # @brief Get the extended device tree database.
    #
    # @return Extended device tree database.
    def edts(self):
        return edtsdatabase_edts(self.cogeno_module)

    ##
    # @brief Get the cmake variables database.
    #
    # @return CMake variables database.
    def cmake(self):
        return cmakedb_cmake(self.cogeno_module)

    def cmake_variable(self, variable_name, default="<unset>"):
        return self.cmake().variable(variable_name, default)

    def cmake_cache_variable(self, variable_name, default="<unset>"):
        return self.cmake().cache_variable(variable_name, default)

    ##
    # @brief Get all config properties.
    #
    # The property names are the ones config file.
    #
    # @return A dictionary of config properties.
    def config_properties(self):
        return configdb_configs(self.cogeno_module).properties()

    ##
    # @brief Get the value of a configuration property fromthe config file.
    #
    # If property_name is not given in .config the default value is returned.
    #
    # @param property_name Name of the property
    # @param default Property value to return per default.
    # @return property value
    def config_property(self, property_name, default="<unset>"):
        return configdb_configs(self.cogeno_module).property(property_name,
							     default)



