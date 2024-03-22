from .__base import Board
from collections import Counter
from abc import ABC, abstractmethod
from yacht.state import State


class Choice(Board):
    alias = 'c'

    @classmethod
    def evaluate(cls, state: State) -> float:
        return sum(state.eyes)


class ConditionalBoard(Board, ABC):
    @classmethod
    @abstractmethod
    def is_condition_met(cls, state: State) -> bool:
        pass

    @classmethod
    @abstractmethod
    def evaluate_unconditioned(cls, state: State) -> float:
        pass

    @classmethod
    def evaluate(cls, state: State) -> float:
        return cls.is_condition_met(state) * cls.evaluate_unconditioned(state)


class Poker(ConditionalBoard):
    alias = 'p'

    @classmethod
    def is_condition_met(cls, state: State) -> bool:
        return any(count >= 4 for count in Counter(state.eyes).values())

    @classmethod
    def evaluate_unconditioned(cls, state: State) -> float:
        return sum(state.eyes)


class FullHouse(ConditionalBoard):
    alias = 'f'

    @classmethod
    def is_condition_met(cls, state: State) -> bool:
        return set(Counter(state.eyes).values()) == {2, 3}

    @classmethod
    def evaluate_unconditioned(cls, state: State) -> float:
        return sum(state.eyes)


class SmallStraight(ConditionalBoard):
    alias = 's'

    @classmethod
    def is_condition_met(cls, state: State) -> bool:
        return any(set(state.eyes).issuperset(s)
                   for s in [{1, 2, 3, 4},
                             {2, 3, 4, 5},
                             {3, 4, 5, 6}])

    @classmethod
    def evaluate_unconditioned(cls, state: State) -> float:
        return 15


class LargeStraight(ConditionalBoard):
    alias = 'l'

    @classmethod
    def is_condition_met(cls, state: State) -> bool:
        return any(set(state.eyes).issuperset(s)
                   for s in [{1, 2, 3, 4, 5},
                             {2, 3, 4, 5, 6}, ])

    @classmethod
    def evaluate_unconditioned(cls, state: State) -> float:
        return 30


class Yacht(ConditionalBoard):
    alias = 'y'

    @classmethod
    def is_condition_met(cls, state: State) -> bool:
        return len(set(state.eyes)) == 1

    @classmethod
    def evaluate_unconditioned(cls, state: State) -> float:
        return 50

