from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..game import Game

from abc import ABC, abstractmethod


class Command(ABC):
    aliases: tuple[str, ...] = ()

    def __init__(self, game: Game):
        self.game = game

    @abstractmethod
    def process(self, *args) -> bool:
        """
        returning value indicates whether the game proceeds to the next round or not
        """
        pass
