
from random import randint
class RandomNumber:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def generate(self):
        return randint(self.lower, self.upper)