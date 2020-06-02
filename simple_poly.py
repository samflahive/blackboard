from scribble import Scribble
from numbers import number, random_number
from variables import variable
import math_blocks

class simple_poly(Scribble):
    def __init__(self, coeffs, var, start_power=None, sign=True, board=None, log=True):
        blocks = []
        mb_coeffs = []
        for coeff in coeffs:
            if isinstance(coeff, random_number):
                coeff = number(coeff, board=coeff.board)
            elif not isinstance(coeff, Scribble):
                raise ValueError("math_board simple_poly take only math_board objects or random_numbers in its coeffs list")
            blocks.append(coeff.block)
            mb_coeffs.append(coeff)

        if not isinstance(var, variable):
            raise ValueError("math_board simple_poly takes a math_board variable object as its var parameter (second argument)")
            
        if board == None:
            board = var.board
        if log:
            board_message = f"{' '.join(str(i.math_board_id) for i in mb_coeffs)}~{var.math_board_id}~{'T' if sign else 'F'}|sp|_i_"
        else:
            board_message = None

        block = math_blocks.simple_poly(coeffs=blocks, var=var.block, start_power=start_power, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)
