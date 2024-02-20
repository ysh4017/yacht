from .__base import Command
from ..constant import MAX_NUM_ROLL


class RerollCommand(Command):
    aliases = ('r', 're', 'reroll')

    def process(self, *args) -> bool:
        state = self.game.state
        if state.num_rolled < MAX_NUM_ROLL:
            state.roll()
            roll_left = MAX_NUM_ROLL - state.num_rolled
            print(f'Re-rolled! ({roll_left} rolls left)')
        else:
            print(f"Cannot re-roll. You've used all {MAX_NUM_ROLL} chances.")
        return False
