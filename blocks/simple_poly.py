from .scribble import Scribble
from .numbers import Number, RandomNumber
from .variables import Variable
import math_blocks.algebra.polynomials

class SimplePoly(Scribble):
    def __init__(self, coeffs, var, start_power=None, sign=True, board=None, log=True):
        blocks = []
        mb_coeffs = []
        for coeff in coeffs:
            if isinstance(coeff, RandomNumber):
                coeff = Number(coeff, board=coeff.board)
            elif not isinstance(coeff, Scribble):
                raise ValueError("math_board simple_poly take only math_board objects or RandomNumbers in its coeffs list")
            blocks.append(coeff.block)
            mb_coeffs.append(coeff)

        if not isinstance(var, Variable):
            raise ValueError("math_board simple_poly takes a math_board Variable object as its var parameter (second argument)")
            
        if board == None:
            board = var.board
        if log:
            board_message = f"{' '.join(str(i.math_board_id) for i in mb_coeffs)}~{var.math_board_id}~{'T' if sign else 'F'}|sp|_i_"
        else:
            board_message = None

        block = math_blocks.algebra.polynomials.SimplePoly(coeffs=blocks, var=var.block, start_power=start_power, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)

    def from_roots(var, roots, log=True, board=None):
        mb_roots = []
        blocks = []
        for root in roots:
            if isinstance(root, RandomNumber):
                root = Number(root, board=root.board)
            elif not isinstance(root, Scribble):
                raise ValueError("math_board simple_poly.from_roots take only math_board objects or RandomNumbers in its roots list")
            blocks.append(root.block)
            mb_roots.append(root)

        
        if not isinstance(var, Variable):
            raise ValueError("math_board simple_poly takes a math_board Variable object as its var parameter (second argument)")
            
        if board == None:
            board = var.board
        if log:
            board_message = f"{var.math_board_id}~{' '.join(str(i.math_board_id) for i in mb_roots)}|sp|fr"
        else:
            board_message = None

        block = math_blocks.algebra.polynomials.SimplePoly.from_roots(var=var.block, roots=blocks)

        return Scribble(block=block, board=board, message=board_message)

