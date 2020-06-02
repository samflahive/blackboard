from scribble import Scribble
from numbers import number, random_number
import math_blocks

class logarithm(Scribble):
    def __init__(self, exponent, base, sign=True, board=None, log=True):
        if isinstance(base, random_number):
            base = number(base, board=board)
        if isinstance(exponent, random_number):
            exponent = number(exponent, board=board)

        valid_operands = (isinstance(base, Scribble)) and (isinstance(exponent, Scribble))

        if not valid_operands:
            raise ValueError("math_board logarithms need a math_board block object as its exponent and base")
        if board == None:
            board = base.board

        if log:
            board_message = f"{exponent.math_board_id}~{base.math_board_id}~{'T' if sign else 'F'}|l|_i_"
        else:
            board_message = None

        block = math_blocks.logarithm(base=base.block, exponent=exponent.block, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)


