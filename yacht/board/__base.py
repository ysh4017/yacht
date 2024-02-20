from yacht.state import State
from abc import ABC, abstractmethod


class Board(ABC):
    def __init__(self):
        self.score = 0
        self.is_filled = False

    @classmethod
    @abstractmethod
    def evaluate(cls, state: State) -> float:
        pass

    def fill(self, state: State) -> None:
        self.score = self.evaluate(state)
        self.is_filled = True


