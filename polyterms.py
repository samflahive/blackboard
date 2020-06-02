from scribble import Scribble
from numbers import number, random_number
from polycomps import polycomp
import math_blocks

class polyterm(Scribble):
    def __init__(self, coeff, pcomp, sign=True, board=None, log=True):
        if isinstance(coeff, random_number):
            coeff = number(coeff, board=coeff.board)
        elif not isinstance(coeff, Scribble):
            raise ValueError("math_board polyterm must take a random_number source or a Scribble object as its coefficient")
        if not isinstance(pcomp, polycomp):
            raise ValueError("math_board polyterm must take a polycomp object object for the 'pcomp' parameter (second argument)")
        
        if board == None:
            board = pcomp.board

        if log:
            board_message = f"{coeff.math_board_id}~{pcomp.math_board_id}~{'T' if sign else 'F'}|pt|_i_"
        else:
            board_message = None

        block = math_blocks.polyterm(coeff=coeff.block, pcomp=pcomp.block, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)



