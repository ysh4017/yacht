from .__base import Command


class ShowBoardCommand(Command):
    aliases = ('s', 'show')

    def process(self, *args) -> bool:
        self.game.show()
        return False
