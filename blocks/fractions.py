from .scribble import Scribble
from .numbers import Number, RandomNumber
import math_blocks.algebra.core

class Fraction(Scribble):
    def __init__(self, numerator, denominator, sign=True, board=None, log=True):
        if isinstance(numerator, RandomNumber):
            numerator = Number(numerator, board=board)
        if isinstance(denominator, RandomNumber):
            denominator = Number(denominator, board=board)

        valid_operands = (isinstance(denominator, Scribble)) and (isinstance(numerator, Scribble))

        if not valid_operands:
            raise ValueError("math_board fractions need a math_board block object as its numerator and denominator")
        if board == None:
            board = numerator.board

        if log:
            board_message = f"{numerator.math_board_id}~{denominator.math_board_id}~{'T' if sign else 'F'}|f|_i_"
        else:
            board_message = None

        block = math_blocks.algebra.core.Fraction(numerator=numerator.block, denominator=denominator.block, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)


    def split(self):
        board_message = f"{self.math_board_id}|f|sp"
        block = self.block.split()
        
        return Scribble(self, block=block, board=self.board, message=board_message)

    def inverse(self):
        board_message = f"{self.math_board_id}|f|iv"
        block = self.block.inverse()
        
        return Scribble(self, block=block, board=self.board, message=board_message)


