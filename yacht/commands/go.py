from .__base import Command


class GoCommand(Command):
    aliases = ('g', 'go')

    def process(self, *args) -> bool:
        board_key, = args

        # invalid board key
        if board_key not in self.game.boards:
            print('Invalid board!')
            print('Input board must be one of the followings:')
            print('▷ 1 ~ 6')
            print('▷ [c]hoice')
            print('▷ [p]oker')
            print('▷ [f]ull-house')
            print('▷ [s]mall straight')
            print('▷ [l]arge straight')
            print('▷ [y]acht')
            return False

        board = self.game.boards[board_key]
        board_name = type(board).__name__
        if board.is_filled:
            print(f"{board_name} is already filled!")
            return False
        state = self.game.state
        score = board.evaluate(state)

        # ask if user is sure
        while True:
            print(f'{score} points on {board_name}?')
            is_okay = input('[y]/[n]').lower().strip()
            if is_okay == 'y':
                board.fill(state)
                print(f'{score} points on {board_name}!')
                self.game.show()
                return True
            elif is_okay == 'n':
                return False
            else:
                print('please enter [y] or [n].')
                continue

