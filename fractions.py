from scribble import Scribble
from numbers import number, random_number
import math_blocks

class fraction(Scribble):
    def __init__(self, numerator, denominator, sign=True, board=None, log=True):
        if isinstance(numerator, random_number):
            numerator = number(numerator, board=board)
        if isinstance(denominator, random_number):
            denominator = number(denominator, board=board)

        valid_operands = (isinstance(denominator, Scribble)) and (isinstance(numerator, Scribble))

        if not valid_operands:
            raise ValueError("math_board fractions need a math_board block object as its numerator and denominator")
        if board == None:
            board = numerator.board

        if log:
            board_message = f"{numerator.math_board_id}~{denominator.math_board_id}~{'T' if sign else 'F'}|f|_i_"
        else:
            board_message = None

        block = math_blocks.fraction(numerator=numerator.block, denominator=denominator.block, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)


