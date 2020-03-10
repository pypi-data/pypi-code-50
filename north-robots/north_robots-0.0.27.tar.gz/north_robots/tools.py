from typing import Tuple, Optional
from north_c9.controller import C9Controller
from north_robots.components import Location, Vector3


def find_location(c9: C9Controller, probe: bool=False) -> Tuple[Location, float]:
    pos = c9.joystick.record_position(use_probe=probe)
    return Location(local_position=Vector3(pos[0], pos[1], pos[2])), pos[3]


def find_and_print_location(c9: C9Controller, probe: bool=False, prefix: str=''):
    location, gripper = find_location(c9, probe)
    pos = location.local_position
    print(f'{prefix}Location({pos.x()}, {pos.y()}, {pos.z()})  # gripper = {gripper}')
