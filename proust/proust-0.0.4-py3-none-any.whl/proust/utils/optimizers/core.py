from abc import ABC, abstractmethod


# TODO: Add type hints
class Optimizer(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError()

    @abstractmethod
    def update(self, params, grad):
        raise NotImplementedError()
