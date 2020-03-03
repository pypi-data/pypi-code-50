class ValidationError(Exception):
    """
    Raised when OpenLab Simulator returns 422 error code
    This happens when:
    * config/sim setpoints are out of simulator boundaries
    * Creating a configuration with name that already exists
    """
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.message = message

class ConfigurationNotFound(Exception):
    """
    Raise when configuration is not found in OpenLab
    """
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.message = message

class SimulationNotFound(Exception):
    """
    Raise when simulation is not found in OpenLab
    """
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.message = message