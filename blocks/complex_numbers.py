from .scribble import Scribble
from .numbers import Number, RandomNumber
import math_blocks.algebra.exponentials

class ComplexNumber(Scribble):
    def __init__(self, real, imaginary, sign=True, board=None, log=True):
        if isinstance(real, RandomNumber):
            real = Number(real, board=real.board)
        elif not isinstance(real, Scribble):
            raise ValueError("math_board ComplexNumber must take a RandomNumber or scribble object as its real value")

        if isinstance(imaginary, RandomNumber):
            imaginary = Number(imaginary, board=real.board)
        elif not isinstance(imaginary, Scribble):
            raise ValueError("math_board ComplexNumber must take a RandomNumber or scribble object as its imaginary value")
            
            
        if board == None:
            board = real.board

        if log:
            board_message = f"{real.math_board_id}~{imaginary.math_board_id}~{'T' if sign else 'F'}|cx|_i_"
        else:
            board_message = None

        block = math_blocks.algebra.exponentials.ComplexNumber(real=real.block, imaginary=imaginary.block, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)


    def to_polar(self):
        board_message = f"{self.math_board_id}|cx|tp"
        block = self.block.to_polar()
        return Scribble.__init__(self, block=block, board=self.board, message=board_message)

    @staticmethod
    def from_polar(angle, radius, sign=True, board=None, log=True):
        if isinstance(angle, RandomNumber):
            angle = Number(angle, board=board)
        elif not isinstance(angle, Scribble):
            raise ValueError("math_board ComplexNumber.from_polar must take a RandomNumber or scribble object as its angle value")

        if isinstance(radius, RandomNumber):
            radius = Number(radius, board=board)
        elif not isinstance(radius, Scribble):
            raise ValueError("math_board ComplexNumber.from_polar must take a RandomNumber or scribble object as its radius value")

        block = math_blocks.algebra.exponentials.ComplexNumber.from_polar(angle=angle.block, radius=radius.block, sign=sign)
        board_message = f"{angle.math_board_id}~{radius.math_board_id}~{'T' if sign else 'F'}|cx|fp"
        return Scribble.__init__(self, block=block, board=self.board, message=board_message)
            





