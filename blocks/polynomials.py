from .scribble import Scribble
from .numbers import Number, RandomNumber
from .polyterms import PolyTerm
from .variables import Variable
import math_blocks.algebra.polynomials

class Polynomial(Scribble):
    def __init__(self, items, sign=True, board=None, log=True):
        blocks = []
        for item in items:
            if not isinstance(item, PolyTerm):
                raise ValueError("math_board polynomials take only math_board PolyTerm objects in its items list")
            blocks.append(item.block)
            
        if board == None:
            board = items[0].board

        if log:
            board_message = f"{' '.join(str(i.math_board_id) for i in items)}~{'T' if sign else 'F'}|py|_i_"
        else:
            board_message = None

        block = math_blocks.algebra.polynomials.Polynomial(items=blocks, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)


    @staticmethod
    def root_to_factor(var, val, log=True, board=None):
        if isinstance(val, RandomNumber):
            val = Number(val)
        elif not isinstance(val, Scribble):
            raise ValueError("polynomial root_to_factor needs RandomNumber or Scribble object")

        if not isinstance(var, Variable):
            raise ValueError("polynomial root_to_factor takes a Variable object")

        if board == None:
            board = var.board

        if log:
            board_message = f"{var.math_board_id}~{val.math_board_id}|py|rf"
        else:
            board_message = None

        block = math_blocks.algebra.polynomials.Polynomial.root_to_factor(var.block, val.block)

        return Scribble(block=block, board=board, message=board_message)
        
