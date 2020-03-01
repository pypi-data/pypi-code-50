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

    ##
    # @brief Get the value of a CMake variable.
    #
    # If variable_name is not provided to cogeno by CMake the default value
    # is returned.
    #
    # A typical set of CMake variables that are not available in the
    # `CMakeCache.txt` file and have to be provided as defines
    # to cogeno if needed:
    #
    # - "PROJECT_NAME"
    # - "PROJECT_SOURCE_DIR"
    # - "PROJECT_BINARY_DIR"
    # - "CMAKE_SOURCE_DIR"
    # - "CMAKE_BINARY_DIR"
    # - "CMAKE_CURRENT_SOURCE_DIR"
    # - "CMAKE_CURRENT_BINARY_DIR"
    # - "CMAKE_CURRENT_LIST_DIR"
    # - "CMAKE_FILES_DIRECTORY"
    # - "CMAKE_PROJECT_NAME"
    # - "CMAKE_SYSTEM"
    # - "CMAKE_SYSTEM_NAME"
    # - "CMAKE_SYSTEM_VERSION"
    # - "CMAKE_SYSTEM_PROCESSOR"
    # - "CMAKE_C_COMPILER"
    # - "CMAKE_CXX_COMPILER"
    # - "CMAKE_COMPILER_IS_GNUCC"
    # - "CMAKE_COMPILER_IS_GNUCXX"
    #
    # @param variable_name Name of the CMake variable
    # @param default Default value
    # @return value
    def cmake_variable(self, variable_name, default="<unset>"):
        return self.cmake().variable(variable_name, default)

    ##
    # @brief Get the value of a CMake variable from CMakeCache.txt.
    #
    # If variable_name is not given in `CMakeCache.txt` the default value is
    # returned.
    #
    # @param variable_name Name of the CMake variable
    # @param default Default value
    # @return value
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



