from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..game import Game

from ..commands import KeepCommand, UnkeepCommand, RerollCommand, GoCommand
from ..board.__base import Board
from abc import ABC, abstractmethod


class BotBase(ABC):
    game: Game

    def connect_to_game(self, game: Game):
        self.game = game

    @abstractmethod
    def play(self):
        pass

    @property
    def current_state(self):
        return self.game.state

    def keep(self, dice_nos: list[int]):
        KeepCommand(self.game).process(dice_nos)

    def unkeep(self, dice_nos: list[int]):
        UnkeepCommand(self.game).process(dice_nos)

    def reroll(self):
        RerollCommand(self.game).process()

    def go(self, board: Board | str):
        if isinstance(board, Board):
            board_alias = board.alias
        else:
            board_alias = board
        GoCommand(self.game).process(board_alias, ask=False)
