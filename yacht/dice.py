import random


class Dice:
    def __init__(self):
        self.eye = None
        self.is_keeped = False

    def keep(self):
        self.is_keeped = True

    def unkeep(self):
        self.is_keeped = False

    def roll(self) -> int:
        if not self.is_keeped:
            self.eye = random.randint(1, 6)
        return self.eye
