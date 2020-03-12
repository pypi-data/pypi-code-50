import os
import configparser
import warnings

# load the configuration INI file
# this file should be present on any Windows system with ChemStation installed
try:
    _config_ini_location = 'C:\\ProgramData\\Agilent Technologies\\ChemStation\\ChemStation.ini'
    _config = configparser.ConfigParser()
    result = _config.read(
        _config_ini_location,
        encoding='utf16',
    )
    if result == []:
        raise FileNotFoundError(f'ChemStation.ini was not found')

    # installation folder for ChemStation
    CHEMSTATION_INSTALL_PATH = _config.get('PCS', 'Path')[:-1]
    CHEMSTATION_CORE_PATH = _config.get('PCS,1', '_EXEPATH$')
    CHEMSTATION_DATA_PATH = _config.get('PCS,1', '_DATAPATH$')
    CHEMSTATION_METHOD_PATH = _config.get('PCS,1', '_CONFIGMETPATH$')
    # remove extraneous backslash
    if CHEMSTATION_CORE_PATH.endswith('\\'):
        CHEMSTATION_CORE_PATH = CHEMSTATION_CORE_PATH[:-1]
    if CHEMSTATION_DATA_PATH.endswith('\\'):
        CHEMSTATION_DATA_PATH = CHEMSTATION_DATA_PATH[:-1]
    if CHEMSTATION_METHOD_PATH.endswith('\\'):
        CHEMSTATION_METHOD_PATH = CHEMSTATION_METHOD_PATH[:-1]

except FileNotFoundError:
    warnings.warn(f'ChemStation.ini was not found in ProgramData, attempting to load from environment variables')
    # todo come up with a more explicit naming convention for manual specification
    # try to find ChemStation folder (priority: 'hplcfolder' environment variable > default install location)
    if os.getenv('hplcfolder') is None:  # if the environment variable is not set
        if os.path.isdir('C:\\Chem32') is True:  # try default location for ChemStation
            CHEMSTATION_DATA_PATH = 'C:\\Chem32'
        else:
            warnings.warn(f'The hplcfolder envrionment variable is not set on this computer '
                          f'and the default folder does not exist, functionality will be reduced.')
            CHEMSTATION_DATA_PATH = None
    else:
        CHEMSTATION_DATA_PATH = os.getenv('hplcfolder')