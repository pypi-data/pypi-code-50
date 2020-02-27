import enum
import time
from dataclasses import dataclass
from enum import Enum
from threading import Thread
from typing import Optional, Union

from BotballKit.bot import Bot


class SensorType(Enum):
    DIGITAL = enum.auto()
    ANALOG = enum.auto()


@dataclass
class Sensor:
    bot: Bot
    type: SensorType
    port: int

    def status(self) -> Union[bool, int]:
        if self.type == SensorType.ANALOG:
            return self.bot.kipr.analog(self.port)
        elif self.type == SensorType.DIGITAL:
            return self.bot.kipr.digital(self.port) == 1


@dataclass
class Motor:
    bot: Bot
    port: int

    def stop(self):
        self.bot.kipr.off(self.port)

    def move(self, power: int, seconds: float):
        self.bot.kipr.motor(self.port, power)
        time.sleep(seconds)
        self.bot.kipr.motor(self.port, 0)

    def move_async(self, power: int, seconds: float):
        Thread(target=self.move, args=(power, seconds), daemon=True).start()


@dataclass
class Servo:
    bot: Bot
    port: int

    def enable(self, default_position: Optional[int] = None):
        self.bot.kipr.enable_servo(self.port)
        if default_position is not None:
            self.position(default_position)

    def disable(self, default_position: Optional[int] = None):
        if default_position is not None:
            self.position(default_position)
        self.bot.kipr.disable_servo(self.port)

    def is_enabled(self) -> bool:
        return self.bot.kipr.get_servo_enabled(self.port) == 1

    def toggle(self, default_position: Optional[int] = None):
        if self.is_enabled():
            self.disable(default_position)
        else:
            self.enable(default_position)

    def position(self, position: Optional[int] = None) -> Optional[int]:
        if position is not None:
            self.bot.kipr.set_servo_position(self.port, max(0, min(position, 1024)))
        else:
            return self.bot.kipr.get_servo_position(self.port)
