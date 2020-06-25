from .scribble import Scribble
from .numbers import Number, RandomNumber
from .polycomps import PolyComp
import math_blocks.algebra.polynomials

class PolyTerm(Scribble):
    def __init__(self, coeff, pcomp, sign=True, board=None, log=True):
        if isinstance(coeff, RandomNumber):
            coeff = Number(coeff, board=coeff.board)
        elif not isinstance(coeff, Scribble):
            raise ValueError("math_board polyterm must take a RandomNumber source or a Scribble object as its coefficient")
        if not isinstance(pcomp, PolyComp):
            raise ValueError("math_board polyterm must take a PolyComp object object for the 'pcomp' parameter (second argument)")
        
        if board == None:
            board = pcomp.board

        if log:
            board_message = f"{coeff.math_board_id}~{pcomp.math_board_id}~{'T' if sign else 'F'}|pt|_i_"
        else:
            board_message = None

        block = math_blocks.algebra.polynomials.PolyTerm(coeff=coeff.block, pcomp=pcomp.block, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)



