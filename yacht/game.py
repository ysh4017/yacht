from .board import *
from .board.__base import Board
from .commands import *
from collections import OrderedDict
from .state import State
from .constant import BONUS_SCORE, BONUS_BOUND


class Game:
    state: State

    def __init__(self):
        self.boards = OrderedDict(
            [
                ('1', Aces()),
                ('2', Deuces()),
                ('3', Threes()),
                ('4', Fours()),
                ('5', Fives()),
                ('6', Sixes()),

                ('c', Choice()),
                ('p', Poker()),
                ('f', FullHouse()),
                ('s', SmallStraight()),
                ('l', LargeStraight()),
                ('y', Yacht()),
            ])

    @property
    def has_bonus(self) -> bool:
        numerical_boards = [self.boards[key] for key in '123456']
        return sum(board.score for board in numerical_boards) >= BONUS_BOUND

    def show_current_state(self):
        print(f'Current state: {self.state}')

    @property
    def unfilled_boards(self) -> list[Board]:
        return [board for board in self.boards.values() if not board.is_filled]

    @property
    def filled_boards(self) -> list[Board]:
        return [board for board in self.boards.values() if board.is_filled]

    @property
    def current_score(self) -> float:
        return (
            sum(board.score for board in self.boards.values())
            + BONUS_SCORE * self.has_bonus
        )

    def play(self):
        while self.unfilled_boards:
            self.play_one_round()
        print('Game Over!')
        self.show()
        print(f'Final Score: {self.current_score}')
        input('Press Enter to quit')

    def play_one_round(self):
        current_round = len(self.filled_boards) + 1

        def cjust(s, width_, fillchar=' '):
            padding = (width_ - len(s)) // 2
            left_padding = padding
            right_padding = padding + (width_ - len(s)) % 2
            return fillchar * left_padding + s + fillchar * right_padding

        width = 30
        print('#' * width)
        print(cjust(f'Round {current_round} start!', width))
        print('#' * width)
        self.state = State()
        self.state.roll()
        self.ask()
        print(f'Current Score: {self.current_score}')

    def ask(self):
        self.show_current_state()
        command_input = input("What will you do? (type 'help' to see commands)")
        command_key, *args = command_input.split()
        self.process_command(command_key, *args)

    def process_command(self, command_key: str, *args):
        try:
            all_commands = [GoCommand, HelpCommand, KeepCommand, UnkeepCommand, RerollCommand, ShowBoardCommand]
            command_mapping = {
                key: command
                for command in all_commands
                for key in command.aliases
            }
            command = command_mapping[command_key](self)
            result = command.process(*args)
            if not result:
                self.ask()

        except Exception:
            print("Invalid command! (type 'help' to see commands)")
            self.ask()

    def show(self):
        print('************************')
        print('slot\t\t\tscore')
        print('========================')
        for board in self.boards.values():
            if isinstance(board, Choice):
                print('------------------------')
                bonus = BONUS_SCORE * self.has_bonus
                print(f'(Bonus)\t\t\t{bonus}')
                print('========================')
            slot_name = type(board).__name__
            if board.is_filled:
                score = board.score
            else:
                score = '-'

            if len(slot_name) < 8:
                num_tabs = 3
            else:
                num_tabs = 2
            print(f'{slot_name}' + '\t' * num_tabs + f'{score}')
        print('************************')
