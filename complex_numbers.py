from scribble import Scribble
from numbers import number, random_number
import math_blocks

class complex_number(Scribble):
    def __init__(self, real, imaginary, sign=True, board=None, log=True):
        if isinstance(real, random_number):
            item = number(real, board=real.board)
        elif not isinstance(real, Scribble):
            raise ValueError("math_board complex_number must take a random_number or scribble object as its real value")

        if isinstance(imaginary, random_number):
            item = number(imaginary, board=real.board)
        elif not isinstance(imaginary, Scribble):
            raise ValueError("math_board complex_number must take a random_number or scribble object as its imaginary value")
            
            
        if board == None:
            board = real.board

        if log:
            board_message = f"{real.math_board_id}~{imaginary.math_board_id}~{'T' if sign else 'F'}|cx|_i_"
        else:
            board_message = None

        block = math_blocks.complex_number(real=real.block, imaginary=imaginary.block, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)




