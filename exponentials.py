from scribble import Scribble
from numbers import number, random_number
import math_blocks

class exponential(Scribble):
    def __init__(self, base, power, sign=True, board=None, log=True):
        if isinstance(base, random_number):
            base = number(base, board=board)
        if isinstance(power, random_number):
            power = number(power, board=board)

        valid_operands = (isinstance(base, Scribble)) and (isinstance(power, Scribble))

        if not valid_operands:
            raise ValueError("math_board fractions need a math_board block object as its numerator and denominator")
        if board == None:
            board = base.board

        if log:
            board_message = f"{base.math_board_id}~{power.math_board_id}~{'T' if sign else 'F'}|e|_i_"
        else:
            board_message = None

        block = math_blocks.exponential(base=base.block, power=power.block, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)


