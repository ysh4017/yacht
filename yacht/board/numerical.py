from .__base import Board
from yacht.state import State


class NumericalBoard(Board):
    target_number: int

    @classmethod
    def evaluate(cls, state: State) -> float:
        return sum(eye for eye in state.eyes if eye == cls.target_number)

    @property
    def alias(self) -> str:
        return str(self.target_number)


class Aces(NumericalBoard):
    target_number = 1


class Deuces(NumericalBoard):
    target_number = 2


class Threes(NumericalBoard):
    target_number = 3


class Fours(NumericalBoard):
    target_number = 4


class Fives(NumericalBoard):
    target_number = 5


class Sixes(NumericalBoard):
    target_number = 6
