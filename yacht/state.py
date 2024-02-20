from .dice import Dice


class State:
    def __init__(self):
        self.dices = [Dice() for _ in range(5)]
        self.num_rolled = 0

    def keep(self, indices: list[int]):
        for i in indices:
            self.dices[i].keep()

    def unkeep(self, indices: list[int]):
        for i in indices:
            self.dices[i].unkeep()

    def roll(self):
        for dice in self.dices:
            dice.roll()
        self.num_rolled += 1

    @property
    def eyes(self) -> tuple[int, ...]:
        return tuple(dice.eye for dice in self.dices)

    def __repr__(self):

        return " ".join(
            f'[{dice.eye}]' if dice.is_keeped
            else f'{dice.eye}'
            for dice in self.dices
        )
