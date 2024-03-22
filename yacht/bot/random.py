from .base import BotBase
from ..board import *


class RandomBot(BotBase):
    def play(self):
        # any board
        any_board = next(iter(self.game.unfilled_boards))
        self.go(any_board)
