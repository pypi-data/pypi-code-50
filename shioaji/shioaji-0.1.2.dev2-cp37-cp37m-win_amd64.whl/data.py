import typing

from shioaji.base import BaseModel


class Ticks(BaseModel):
    ts: typing.List[int]
    close: typing.List[float]
    volume: typing.List[int]
    bid_price: typing.List[float]
    bid_volume: typing.List[int]
    ask_price: typing.List[float]
    ask_volume: typing.List[int]

    def lazy_setter(self, **kwargs):
        [
            setattr(self, kwarg, value)
            for kwarg, value in kwargs.items()
            if hasattr(self, kwarg)
        ]
