from typing import List, Tuple, Dict, Optional, Union, Any
from north_robots.robot import Robot
from north_robots.n9 import N9Robot
from north_robots.components import Location, Tray


class ManagerError(Exception):
    """ Base class for Manager exceptions """
    pass


class TrayManagerError(ManagerError):
    """ Tray manager exceptions """
    pass


class TrayManagerEmptyError(TrayManagerError):
    """ Tray manager empty exception """
    pass


class TrayManager:
    """
    The TrayManager class is a simple class that is meant to be subclassed for working with specific types of trays.
    TrayManager classes will keep track of the "current" index in a list of grids, and allow the user to increment the
    "current" index to the next location. It will also raise a TrayManagerEmptyError once it has run out of indexes.
    """
    def __init__(self, robot: N9Robot, trays: List[Tray]):
        """
        :param robot: an instance of N9Robot
        :param trays: a list of Tray instances
        """
        self.robot = robot
        self.trays = trays
        self.current_indexes_index = 0
        self.indexes: List[Tuple[Tray, str]] = []

        self.indexes = self.build_tray_indexes()

    @property
    def remaining(self) -> int:
        """ Get the number of remaining indexes """
        return len(self.indexes) - self.current_indexes_index

    @property
    def empty(self) -> bool:
        """ Return True if there are no remaining indexes """
        return self.current_indexes_index >= len(self.indexes)

    @property
    def current_location(self) -> Location:
        """ Get the location at the current index """
        tray, index = self.indexes[self.current_indexes_index]
        return tray.locations[index]

    @property
    def current_tray(self) -> Tray:
        """ Get the current tray instance """
        tray, index = self.indexes[self.current_indexes_index]
        return tray

    @property
    def current_index(self) -> str:
        """ Get the current index key """
        tray, index = self.indexes[self.current_indexes_index]
        return index

    @property
    def gripper_rotation(self) -> Optional[float]:
        """ Get the suggested gripper rotation for the current index """
        tray, index = self.indexes[self.current_indexes_index]
        return tray.gripper_rotation(index)

    def build_tray_indexes(self):
        indexes = []

        for tray in self.trays:
            indexes += [(tray, index) for index in tray.build_indexes()]

        return indexes

    def increment_location(self):
        """ Incrememnt the current index, raises a TrayManagerEmptyError if empty """
        if self.remaining <= 0:
            raise TrayManagerEmptyError(f'Trays empty')

        self.current_indexes_index += 1


class NeedleTrayManager(TrayManager):
    """
    The NeedleTrayManager class is a needle-tray specific Manager that provides methods to move the N9Robot to pickup
    needles from needle trays.
    """

    def __init__(self, robot: N9Robot, trays: List[Tray], safe_height_mm: float=200.0, probe: bool=True):
        """
        :param robot: an N9Robot instance
        :param trays: a list of Tray instances
        :param safe_height_mm: how far above the tray the robot should move to pickup a needle, defaults to 200mm
        :param probe: use the probe to pickup needles, defaults to True
        """
        TrayManager.__init__(self, robot, trays)
        self.safe_height_mm = safe_height_mm
        self.probe = probe

    def pickup(self) -> Location:
        """
        Move the robot to pickup a needle at the current index, and increment to the index.

        :return: the tray location of the needle that was picked up
        """
        if self.empty:
            raise TrayManagerEmptyError(f'Needle tray empty')

        needle_location = self.pickup_location(self.current_location)

        if not self.empty:
            self.increment_location()

        return needle_location

    def pickup_location(self, needle_location: Location) -> Location:
        """
        Move the robot to pickup a needle at the given needle_location.

        :return: the location of the needle that was picked up
        """
        safe_location = needle_location.copy(z=min(needle_location.z + self.safe_height_mm, 305.0))
        self.robot.move_to_locations([safe_location, needle_location, safe_location], gripper=self.gripper_rotation,
                                     order=N9Robot.MOVE_Z_XY, probe=self.probe)

        if not self.empty:
            self.increment_location()

        return needle_location
