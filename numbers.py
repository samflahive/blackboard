import math_blocks
from random import randint
from scribble import Scribble

class random_number:
    def __init__(self, lower, upper, board=None, log=True):
        if board == None:
            raise ValueError("random_number objects require a math_board")
        self.board = board

        if log:
            board.log(f"{lower}~{upper}|rn|_i_")
        
        self.upper = upper
        self.lower = lower

        self.math_board_id = self.board.track()

    def generate(self):
        return randint(self.lower, self.upper)




class number(Scribble):
    def __init__(self, value, sign=True, board=None, log=True):
        if not isinstance(value, random_number):
            raise ValueError("math_board numbers need a random_number object as its value")

        if board == None:
            board = value.board

        if log:
            board_message = f"{value.math_board_id}~{'T' if sign else 'F'}|n|_i_"
        else:
            board_message = None

        block = math_blocks.number(value=value.generate(), sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)
