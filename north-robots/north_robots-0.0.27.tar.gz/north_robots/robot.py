from north_c9.controller import C9Controller


class RobotError(Exception):
    """ Base class for Robot exceptions """
    pass


class Robot:
    """
    The Robot class is the base class used for the N9Robot class. Currently it doesn't have enough methods to be useful,
    but eventually it will have a set of methods that can be used across different types of robots.
    """
    def __init__(self, controller: C9Controller):
        """
        :param controller: C9Controller instance
        """
        self.controller = controller

    def move(self):
        pass
