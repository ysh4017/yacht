from .__base import Command


class KeepCommand(Command):
    aliases = ('k', 'keep')

    def process(self, *args) -> bool:
        print(args)
        # 1 ~ 5
        dice_nos = sorted({i for item in args for i in item})
        # 0 ~ 4
        dice_indices = [i - 1 for i in map(int, dice_nos)]

        self.game.state.keep(dice_indices)
        print(f'Dices {", ".join(dice_nos)} kept!')
        return False


class UnkeepCommand(Command):
    aliases = ('u', 'uk', 'unkeep')

    def process(self, *args) -> bool:
        # 1 ~ 5
        dice_nos = sorted({i for item in args for i in item})
        # 0 ~ 4
        dice_indices = [i - 1 for i in map(int, dice_nos)]

        self.game.state.unkeep(dice_indices)
        print(f'Dices {", ".join(dice_nos)} unkept!')
        return False
