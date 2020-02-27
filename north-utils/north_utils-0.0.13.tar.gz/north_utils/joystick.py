from typing import List, Dict, Tuple, Union, Callable
import logging
import pygame
from north_utils.mixins import Runnable

logger = logging.getLogger(__name__)


JoystickState = Union[bool, float, Tuple[int, int]]
JoystickHandler = Callable[[JoystickState], None]


class JoystickError(Exception):
    pass


class JoystickNotFoundError(JoystickError):
    pass


class Joystick(Runnable):
    AXIS_START = 0
    LEFT_STICK_X_AXIS = 0
    LEFT_STICK_Y_AXIS = 1
    RIGHT_STICK_X_AXIS = 2
    RIGHT_STICK_Y_AXIS = 3
    LEFT_TRIGGER_AXIS = 5
    RIGHT_TRIGGER_AXIS = 4

    HAT_START = 100
    DPAD_HAT = HAT_START + 0
    # fake hat axes
    HAT_AXIS_START = 150
    DPAD_X_AXIS = HAT_AXIS_START + 0
    DPAD_Y_AXIS = HAT_AXIS_START + 1

    BUTTON_START = 200
    CROSS_BUTTON = BUTTON_START + 1
    CIRCLE_BUTTON = BUTTON_START + 2
    TRIANGLE_BUTTON = BUTTON_START + 3
    SQUARE_BUTTON = BUTTON_START + 0

    L1_BUTTON = BUTTON_START + 4
    R1_BUTTON = BUTTON_START + 5
    L2_BUTTON = BUTTON_START + 6
    R2_BUTTON = BUTTON_START + 7

    SHARE_BUTTON = BUTTON_START + 8
    OPTIONS_BUTTON = BUTTON_START + 9

    LEFT_STICK_BUTTON = BUTTON_START + 10
    RIGHT_STICK_BUTTON = BUTTON_START + 11

    PLAYSTATION_BUTTON = BUTTON_START + 12
    TOUCHPAD_BUTTON = BUTTON_START + 13

    # Axis Mapping
    X_AXIS = LEFT_STICK_X_AXIS
    Y_AXIS = LEFT_STICK_Y_AXIS
    Z_AXIS = RIGHT_STICK_Y_AXIS
    GRIPPER_LEFT_AXIS = LEFT_TRIGGER_AXIS
    GRIPPER_RIGHT_AXIS = RIGHT_TRIGGER_AXIS
    PRECISE_X_AXIS = DPAD_X_AXIS
    PRECISE_Y_AXIS = DPAD_Y_AXIS

    # Button Mapping
    GRIPPER_MODE_BUTTON = TOUCHPAD_BUTTON
    PLAYBACK_MODE_BUTTON = SHARE_BUTTON
    SLOW_SPEED_BUTTON = L1_BUTTON
    HIGH_SPEED_BUTTON = R1_BUTTON

    GRIPPER_TOGGLE_BUTTON = CROSS_BUTTON
    PROBE_TOGGLE_BUTTON = SQUARE_BUTTON
    ELBOW_SWAP_BUTTON = TRIANGLE_BUTTON
    SPIN_GRIPPER_BUTTON = CIRCLE_BUTTON

    RECORD_BUTTON = OPTIONS_BUTTON
    STOP_BUTTON = PLAYSTATION_BUTTON

    @staticmethod
    def find_joystick(name: str) -> pygame.joystick.JoystickType:
        if not pygame.joystick.get_init():
            pygame.joystick.init()

        for id in range(pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(id)
            if joystick.get_name() == name:
                joystick.init()
                return joystick

        raise JoystickNotFoundError(f'Joystick not found: "{name}"')

    def __init__(self, name: str='Wireless Controller', update_rate: int=240, deadzone: float=0.05):
        Runnable.__init__(self, logger)
        self.name = name
        self.update_rate = update_rate
        self.handlers: Dict[int, List[JoystickHandler]] = {}
        self.clock = pygame.time.Clock()
        self.joystick = self.find_joystick(name)
        self.button_state = [0] * self.joystick.get_numbuttons()
        self.axis_state = [0.0] * self.joystick.get_numaxes()
        self.hat_state = [(0, 0)] * self.joystick.get_numhats()
        self.deadzone = deadzone

    def add_handler(self, event: int, handler: JoystickHandler):
        self.handlers[event] = self.handlers.get(event, []) + [handler]

    def dispatch_event(self, event: int, state: JoystickState):
        if event in self.handlers:
            for handler in self.handlers[event]:
                handler(state)

    def run(self):
        pygame.init()
        self.joystick.init()

        while self.running:
            for id in range(len(self.button_state)):
                state = self.joystick.get_button(id)
                if state != self.button_state[id]:
                    self.dispatch_event(id + self.BUTTON_START, bool(state))
                    self.button_state[id] = state

            for id in range(len(self.axis_state)):
                state = self.joystick.get_axis(id)

                if abs(state) < self.deadzone:
                    state = 0

                if state != self.axis_state[id]:
                    self.dispatch_event(id + self.AXIS_START, state)
                    self.axis_state[id] = state

            for id in range(len(self.hat_state)):
                state = self.joystick.get_hat(id)
                if state != self.hat_state[id]:
                    self.dispatch_event(id + self.HAT_START, state)

                    if state[0] != self.hat_state[id][0]:
                        self.dispatch_event(id * 2 + self.HAT_AXIS_START, float(state[0]))

                    if state[1] != self.hat_state[id][1]:
                        self.dispatch_event(id * 2 + 1 + self.HAT_AXIS_START, float(state[1]))

                    self.hat_state[id] = state

            pygame.event.pump()
            self.clock.tick(self.update_rate)
