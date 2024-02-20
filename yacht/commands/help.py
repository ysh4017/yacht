from .__base import Command


class HelpCommand(Command):
    aliases = ('h', 'help')

    def process(self, *args) -> bool:
        print('------------Command list------------')
        print('▶ k, keep (+dice numbers): Keep dices')
        print('▶ u, uk, unkeep (+dice numbers): Unkeep dices')
        print('▶ r, re, reroll: Reroll unkept dices')
        print('▶ s, show: Show current board')
        print('▶ h, help: see commands')
        print('▶ g, go (+board names): go to selected board with current state')
        print('     Board Names')
        print('      ▷ 1 ~ 6')
        print('      ▷ [c]hoice')
        print('      ▷ [p]oker')
        print('      ▷ [f]ull-house')
        print('      ▷ [s]mall straight')
        print('      ▷ [l]arge straight')
        print('      ▷ [y]acht')

        return False
