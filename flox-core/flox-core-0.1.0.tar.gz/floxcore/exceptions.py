from click import ClickException


class ProfileException(ClickException):
    """Problems with profile"""


class ConfigurationException(ClickException):
    """Missing or invalid configuration"""


class PluginException(ClickException):
    """Problems with plugin"""


class MissingConfigurationValue(ConfigurationException):
    def __init__(self, name):
        self.message = f"Missing configuration parameter '{name}'. Use flox configure"
