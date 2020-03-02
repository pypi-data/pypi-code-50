from typing import Optional, List, Tuple
import time
import threading
import atexit
from north_c9.controller import C9Controller
from north_c9.axis import RevoluteAxis, Output
from north_robots.robot import Robot, RobotError


class SpinCoaterError(RobotError):
    """ Base class for SpinCoater exceptions """
    pass


class SpinCoaterProfileRunningError(SpinCoaterError):
    """ SpinCoater profile running exception """
    pass


class SpinCoater(Robot):
    """
    THe SpinCoater class is a basic Robot class that controls the North Robotics Spin Coater.

    It supports basic spinning and stopping of the spin coater axis, along with spin "profiles" that allow you to run
    a profile of different velocities with a single method call. These methods create a thread to manage the spin
    velocities.
    """
    def __init__(self, controller: C9Controller, axis: int=0, suction_output: int=0, cover_open_output: int=1, cover_close_output: int=2, home: bool=False):
        """
        :param controller: a C9Controller instance for the spin coater
        :param axis: the axis number of the spin coater axis, defaults to 0
        :param suction_output: the output number for the spin coater suction, defaults to 0
        :param cover_open_output: the output number for opening the spin coater cover, defaults to 1
        :param cover_close_output: the output number for closing the spin coater cover, defaults to 2
        :param home: automatically home the spin coater if True, defaults to False
        """
        Robot.__init__(self, controller)
        self.axis = RevoluteAxis(controller, axis)
        self.suction_output = Output(controller, suction_output)
        self.cover_open_output = Output(controller, cover_open_output)
        self.cover_close_output = Output(controller, cover_close_output)
        self.spin_profile_thread: Optional[threading.Thread] = None
        self.spin_profile_running: bool = False

        if home:
            self.home()

        atexit.register(self.halt)

    @property
    def spinning(self) -> bool:
        """
        Returns True if the spin coater is spinning
        """
        return self.controller.axis_moving(self.axis.axis_number)

    def halt(self, timeout: float=5.0):
        """
        Halt the spin coater immediately and turn off power for the axis
        """
        self.spin_profile_running = False

        if self.spin_profile_thread:
            self.spin_profile_thread.join(timeout)

        if self.axis.moving():
            self.axis.spin_stop(wait=False)

    def home(self):
        """
        Home the spin coater
        """
        self.axis.home()

    def open_cover(self):
        """
        Open the spin coater cover
        """
        self.cover_close_output.off()
        self.cover_open_output.on()

    def close_cover(self):
        """
        Close the spin coater cover
        """
        self.cover_open_output.off()
        self.cover_close_output.on()

    def suction_on(self):
        """
        Turn on the spin coater suction
        """
        self.suction_output.on()

    def suction_off(self):
        """
        Turn off the spin coater suction
        """
        self.suction_output.off()

    def spin(self, velocity_rpm: float, acceleration_rpm: float, duration: Optional[float]=None):
        """
        Start spinning the spin coater axis with the given velocity and acceleration (in RPM)

        :param velocity_rpm: spin velocity in RPM
        :param acceleration_rpm: spin acceleration in RPM^2
        :param duration: [Optional] stop spinning the axis after a specified time if given, defaults to None
        """
        self.axis.spin(velocity_rpm, acceleration_rpm, duration)

    def wait_for_stop(self):
        """
        Wait for the spin coater to stop spinning
        """
        if self.spin_profile_running:
            self.spin_profile_thread.join()
        else:
            self.axis.wait()

    def spin_stop(self, profile_timeout: float=5.0, wait: bool=True, stop_thread: bool=True):
        """
        Safely stop the spin coater

        :param profile_timeout: the amount of time to wait for the spin profile to stop, defaults to 5.0s
        :param wait: wait for the spin coater to stop if True, defaults to True
        :param stop_thread: stop any running spin profile threads
        """
        self.axis.spin_stop(wait=False)

        if stop_thread and self.spin_profile_thread is not None and self.spin_profile_running:
            self.spin_profile_running = False

            if wait:
                self.spin_profile_thread.join(timeout=profile_timeout)

        if wait:
            self.axis.wait()

    def run_spin_profile(self, profile: List[Tuple[int, int, float]], home: bool=False):
        self.spin_profile_running = True

        try:
            for velocity, acceleration, duration in profile:
                self.spin(velocity, acceleration)

                end_time = time.time() + duration
                while time.time() < end_time:
                    if not self.spin_profile_running:
                        return self.halt()

                    time.sleep(0.01)
        except KeyboardInterrupt:
            return self.halt()

        self.spin_stop(wait=True, stop_thread=False)

        time.sleep(1)

        if home:
            self.axis.home()

        self.spin_profile_running = False

    def spin_profile(self, profile: List[Tuple[int, int, float]], wait: bool=True, home: bool=False):
        """
        Run a spin profile with varying velocities and durations

        :param profile: a list with a 3-element tuples of spin profile keyframes with the form: (<velocity rpm>, <acceleration rpm>, <duration seconds>)
        :param wait: wait for the profile to finish if True, defaults to True
        :param home: home the spin coater after the profile is finished if True, defaults to False
        """
        if wait:
            self.run_spin_profile(profile, home=home)
        else:
            if self.spin_profile_running:
                raise SpinCoaterProfileRunningError(f'Cannot run profile while a profile is currently running')

            self.spin_profile_thread = threading.Thread(target=self.run_spin_profile, args=[profile], daemon=True)
            self.spin_profile_thread.start()
