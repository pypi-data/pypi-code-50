"""
    cfg_loader.exceptions
    ~~~~~~~~~~~~~~~~~~~~~

    Implement configuration loader Exception

    :copyright: Copyright 2017 by ConsenSys France.
    :license: BSD, see :ref:`license` for more details.
"""
import marshmallow


class ConfigLoaderError(Exception):
    """Base class for all application related errors."""


class ConfigFileMissingError(ConfigLoaderError):
    """Error raised when not specifying a config file"""


class ConfigFileNotFoundError(ConfigLoaderError):
    """Error raised when an invalid config file path is provided"""


class LoadingError(ConfigLoaderError):
    """Error raised when loading the configuration file"""


# This must extend the marshmallow error, or marshmallow will swallow nested errors.
class ValidationError(ConfigLoaderError, marshmallow.ValidationError):
    """Error raised when marshmallow raise a validation error at deserialization"""


class UnsetRequiredSubstitution(LoadingError):
    """Error raised when a substitution environment variable is required but unset"""


class InvalidSubstitution(LoadingError):
    """Error raised when an invalid substitution is detected"""
