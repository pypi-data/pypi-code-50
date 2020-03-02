from typing import Optional, Union, Tuple, List
from north_utils.location import Vector3
from north_c9.axis import RevoluteAxis, PrismaticAxis, OpenOutput
from north_c9.controller import C9Controller
from north_robots.robot import Robot
from north_robots.components import Component, Location, Quaternion

MovementOrderItem = Union[int, Tuple[int, int], Tuple[int, int, int]]
MovementOrder = List[MovementOrderItem]
GripperOffset = Union[Vector3, Tuple[float, float, float], List[float]]


class N9RobotError(Exception):
    """ Base class for N9Robot exceptions """
    pass


class N9RobotMovementError(N9RobotError):
    """ N9Robot movement exceptions """
    pass


class N9RobotMovementUnreachableLocation(N9RobotMovementError):
    """ N9Robot unreachable location exceptions """
    pass


class N9RobotMovementInvalidMovementOrder(N9RobotMovementError):
    """ N9Robot invalid movement order exception """
    pass


class N9Robot(Robot):
    """
    The N9Robot class is used to control the N9 robot at a higher level than using the C9Controller directly. It provides
    axis instances for the different joints in the arm, as well as a move_to_location method that will work with
    Location instances.
    """

    GRIPPER = 0
    ELBOW = 1
    SHOULDER = 2
    COLUMN = 3

    MOVE_STEP_XY: MovementOrderItem = (ELBOW, SHOULDER)
    MOVE_STEP_Z: MovementOrderItem = (COLUMN, )
    MOVE_STEP_XYZ: MovementOrderItem = (ELBOW, SHOULDER, COLUMN)

    MOVE_Z_XY: MovementOrder = (MOVE_STEP_Z, MOVE_STEP_XY)
    """ Spit up arm movements and move the column before the rest of the arm """
    MOVE_XY_Z: MovementOrder = (MOVE_STEP_XY, MOVE_STEP_Z)
    """ Spit up arm movements and move the arm before the column """
    MOVE_XYZ: MovementOrder = (MOVE_STEP_XYZ, )
    """ Don't split up movements and move the arm and column simultaneously """

    def __init__(self, controller: C9Controller=C9Controller.default_controller, column_axis_number: int=3,
                 shoulder_axis_number: int=2, elbow_axis_number: int=1, gripper_axis_number: int=0, probe_offset: float=41.5,
                 gripper_output: int=0, velocity_counts=20_000, acceleration_counts=20_000,
                 elbow_bias: int=C9Controller.BIAS_MIN_SHOULDER, home: bool=False) -> None:
        """
        :param controller: C9Controller instance
        :param velocity_counts: the default velocity to use for movements in counts/s, defaults to 20,000 counts/s
        :param acceleration_counts: the default acceleration to use for movements in counts/s^2, defaults to 20,000 counts/s^2
        :param gripper_offset: the horizontal distance from the center of the gripper to the center of the probe in mm, defaults to 41.5mm
        :param elbow_bias: the default elbow bias to use for movements, defaults to BIAS_MIN_SHOULDER
        :param home: home arm automatically, defaults to False
        :param column_axis_number: override column axis number, defaults to 3
        :param shoulder_axis_number: override shoulder axis number, defaults to 2
        :param elbow_axis_number: override elbow axis number, defaults to 1
        :param gripper_axis_number: override gripper axis number, defaults to 0
        :param gripper_output: the output number for the gripper actuator, defaults to 0
        """
        Robot.__init__(self, controller)

        self.column = PrismaticAxis(controller, column_axis_number, counts_per_mm=100, zero_position_mm=280, inverted=True,
                                    velocity_counts=velocity_counts, acceleration_counts=acceleration_counts)

        self.shoulder = RevoluteAxis(controller, shoulder_axis_number, counts_per_revolution=101_000, zero_position_degrees=-118.87128712871288,
                                     velocity_counts=velocity_counts, acceleration_counts=acceleration_counts,
                                     inverted=True)

        self.elbow = RevoluteAxis(controller, elbow_axis_number, counts_per_revolution=51_000, zero_position_degrees=148.23529411764704,
                                  velocity_counts=velocity_counts, acceleration_counts=acceleration_counts)

        self.gripper = RevoluteAxis(controller, gripper_axis_number, counts_per_revolution=4000, zero_position_degrees=180,
                                    velocity_counts=velocity_counts, acceleration_counts=acceleration_counts)

        self.gripper_output = OpenOutput(controller, gripper_output, open_state=False)
        self.probe_offset = probe_offset
        self.elbow_bias = elbow_bias
        self.velocity_counts = velocity_counts
        self.acceleration_counts = acceleration_counts
        self.first_move = True

        if self.controller.connection.connected:
            self.controller.speed(velocity_counts, acceleration_counts)
            self.controller.elbow_bias(elbow_bias)

            if home:
                self.controller.home()


    @property
    def location(self) -> Vector3:
        """ Get the location of the gripper / end effector """
        return Vector3(*self.controller.cartesian_position())

    def home(self):
        """ Home the robot, will do nothing if robot is already homed """
        self.controller.home(if_needed=True)

    def move(self, x: Optional[float]=None, y: Optional[float]=None, z: Optional[float]=None, gripper: Optional[float]=None,
             order: MovementOrder=MOVE_XYZ, velocity: Optional[float]=None, acceleration: Optional[float]=None,
             relative=False, wait: bool=True, probe: bool=False, gripper_offset: Optional[GripperOffset]=None,
             probe_offset: Optional[float]=None, elbow_bias: Optional[int]=None):
        """
        Move the robot arm. This method tries to minimize the number of axes being moved based on the parameters. For
        example, if an x and y position are given but no z position is given, then the column will not move. Also, the
        gripper will not move unless the gripper parameter is set.

        :param x: x position in mm of final arm position
        :param y: y position in mm of final arm position
        :param z: z position in mm of final arm position
        :param gripper: gripper angle in degrees of final arm position, relative to deck
        :param velocity: velocity to use during movement in counts/s, defaults to self.velocity_counts
        :param acceleration: acceleration to use during movement in counts/s^2, defaults to self.acceleration_counts
        :param order: [Optional] movement order constant (one of N9Robot.MOVE_XYZ, N9Robot.MOVE_Z_XY, N9Robot.MOVE_XY_Z)
        :param relative: perform a relative movement if True, defaults to False
        :param wait: wait for the movement to complete before returning, defaults to True
        :param probe: use the probe when moving
        :param probe_offset: [Optional] the distance from the gripper to the probe, defaults to self.probe_offset
        :param gripper_offset: [Optional] a vector or tuple offset from the gripper to use when moving
        :param elbow_bias: [Optional] specify an elbow bias for the move, one of: C9Controller.BIAS_MIN_SHOULDER, C9Controller.BIAS_MAX_SHOULDER or C9Controller.BIAS_CLOSEST
        """
        if not wait and order != self.MOVE_XYZ:
            raise N9RobotMovementError(f'Cannot split movement when wait is False')

        if velocity is None:
            velocity = self.velocity_counts

        if acceleration is None:
            acceleration = self.acceleration_counts

        if elbow_bias is None:
            elbow_bias = self.elbow_bias

        # calculate the position offset if we are offsetting the gripper position
        if gripper_offset is not None:
            if probe:
                raise N9RobotMovementError('Cannot use probe with gripper_offset')

            if isinstance(gripper_offset, tuple) or isinstance(gripper_offset, list):
                gripper_offset = Vector3(*gripper_offset)

            # the rotation of the gripper joint is inverted
            rotation = 0 if gripper is None else -gripper
            offset = Quaternion.fromEulerAngles(Vector3(0, 0, rotation)) * gripper_offset
        else:
            offset = Vector3(0, 0, 0)

        # use the default probe offset if probe=True and the probe offset argument hasn't been passed
        if probe:
            if probe_offset is None:
                probe_offset = self.probe_offset

            self.controller.use_probe(True, probe_offset=probe_offset)
        # make sure we set the probe state on first move
        elif self.first_move:
            self.controller.use_probe(False)

        self.first_move = False

        position = Vector3(x or 0, y or 0, z or 0) - offset
        kwargs = dict(velocity=velocity, acceleration=acceleration, relative=relative, elbow_bias=elbow_bias)

        # handle special case where we move only the gripper
        if x is None and y is None and z is None and gripper is not None:
            self.controller.move_arm(gripper=gripper, wait=wait, **kwargs)
        else:
            for item in order:
                # this is quite ugly, but I'm not sure of a better way to handle different combinations of movements
                # while supporting a vector offset
                if item == self.MOVE_STEP_Z:
                    if z is not None:
                        self.controller.move_arm(z=position.z(), **kwargs)
                elif item == self.MOVE_STEP_XY:
                    if x is not None and y is not None:
                        self.controller.move_arm(x=position.x(), y=position.y(), gripper=gripper, **kwargs)
                    elif x is not None:
                        raise N9RobotMovementError(f'Cannot move x without a y value')
                    elif y is not None:
                        raise N9RobotMovementError(f'Cannot move y without an x value')
                elif item == self.MOVE_STEP_XYZ:
                    if x is not None and y is not None and z is not None:
                        self.controller.move_arm(x=position.x(), y=position.y(), z=position.z(), gripper=gripper, wait=wait, **kwargs)
                    elif x is not None and y is not None:
                        self.controller.move_arm(x=position.x(), y=position.y(), gripper=gripper, wait=wait, **kwargs)
                    elif x is not None and z is not None:
                        self.controller.move_arm(x=position.x(), z=position.z(), gripper=gripper, wait=wait, **kwargs)
                    elif y is not None and z is not None:
                        self.controller.move_arm(y=position.y(), z=position.z(), gripper=gripper, wait=wait, **kwargs)
                    elif x is not None:
                        raise N9RobotMovementError(f'Cannot move x without a y value')
                    elif y is not None:
                        raise N9RobotMovementError(f'Cannot move y without an x value')
                    elif z is not None:
                        self.controller.move_arm(z=position.z(), gripper=gripper, wait=wait, **kwargs)
                else:
                    raise N9RobotMovementInvalidMovementOrder(f'Invalid movement order item: {item}')

        # reset probe state if needed
        if probe:
            self.controller.use_probe(False)

    def move_to_location(self, location: Union[Location, Vector3, Component, list, dict], gripper: Optional[float]=None,
                         order: MovementOrder=MOVE_XYZ, velocity: Optional[float]=None, acceleration: Optional[float]=None,
                         probe: bool = False, probe_offset: Optional[float]=None, gripper_offset: Optional[GripperOffset]=None,
                         elbow_bias: Optional[int]=None, wait: bool=True):
        """
        Move the arm to given location. The location can be a Location or Vector3 instance, or a list or dictionary of
        x, y,  and z positions. Lists are in the format [<x>, <y>, <z>] and dictionaries use the following format:
        {'x': <x>, 'y': <y>, 'z': <z>}.

        The gripper will not be moved unless the gripper parameter is specified.

        An optional movement order can also be specified to split up the robot movement into multiple steps.

        :param location: Location, Vector3, list or dict with the final arm position in mm
        :param gripper: gripper angle in degrees of final arm position, relative to deck
        :param velocity: velocity to use during movement in counts/s, defaults to self.velocity_counts
        :param acceleration: acceleration to use during movement in counts/s^2, defaults to self.acceleration_counts
        :param order: [Optional] movement order constant (one of N9Robot.MOVE_XYZ, N9Robot.MOVE_Z_XY, N9Robot.MOVE_XY_Z)
        :param wait: wait for the movement to complete before returning, defaults to True
        :param probe: use the probe when moving
        :param probe_offset: [Optional] the distance from the gripper to the probe, defaults to self.probe_offset
        :param gripper_offset: [Optional] a vector or tuple offset from the gripper to use when moving
        :param elbow_bias: [Optional] specify an elbow bias for the move, one of: C9Controller.BIAS_MIN_SHOULDER, C9Controller.BIAS_MAX_SHOULDER or C9Controller.BIAS_CLOSEST
        """

        if isinstance(location, Component):
            position = location.location.position
        elif isinstance(location, list):
            position = Vector3(*location)
        elif isinstance(location, dict):
            position = Vector3(*[location.get(i, 0) for i in ('x', 'y', 'z')])
        elif isinstance(location, Location):
            position = location.position
        else:
            position = location

        self.move(x=position.x(), y=position.y(), z=position.z(), gripper=gripper, order=order, elbow_bias=elbow_bias,
                  velocity=velocity, acceleration=acceleration, probe=probe, probe_offset=probe_offset,
                  gripper_offset=gripper_offset, wait=wait)

    def move_to_locations(self, locations: List[Union[Location, Vector3, Component, list, dict]], gripper: Optional[float]=None,
                          order: MovementOrder=MOVE_XYZ, velocity: Optional[float]=None, acceleration: Optional[float]=None,
                          probe: bool = False, probe_offset: Optional[float] = None, gripper_offset: Optional[GripperOffset] = None,
                          elbow_bias: Optional[int] = None, wait: bool=True):
        """
        Move the arm through a sequential list of locations. This is a convenience method that avoids multiple
        move_to_location calls.

        :param locations: a list of Locations, Vector3s, lists or dicts of the final arm position in mm
        :param gripper: gripper angle in degrees of final arm position, relative to deck
        :param velocity: velocity to use during movement in counts/s, defaults to self.velocity_counts
        :param acceleration: acceleration to use during movement in counts/s^2, defaults to self.acceleration_counts
        :param order: [Optional] movement order constant (one of N9Robot.MOVE_XYZ, N9Robot.MOVE_Z_XY, N9Robot.MOVE_XY_Z)
        :param wait: wait for the movement to complete before returning, defaults to True
        :param probe: use the probe when moving
        :param probe_offset: [Optional] the distance from the gripper to the probe, defaults to self.probe_offset
        :param gripper_offset: [Optional] a vector or tuple offset from the gripper to use when moving
        :param elbow_bias: [Optional] specify an elbow bias for the move, one of: C9Controller.BIAS_MIN_SHOULDER, C9Controller.BIAS_MAX_SHOULDER or C9Controller.BIAS_CLOSEST
        """
        for location in locations:
            self.move_to_location(location, gripper=gripper, order=order, velocity=velocity, acceleration=acceleration,
                                  probe=probe, probe_offset=probe_offset, gripper_offset=gripper_offset,
                                  elbow_bias=elbow_bias, wait=wait)