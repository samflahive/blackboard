from .scribble import Scribble
from .numbers import Number, RandomNumber
import math_blocks.algebra.polynomials

class Variable(Scribble):
    def __init__(self, symbol, value=None, sign=True, board=None, log=True):
        if isinstance(value, RandomNumber):
            value = Number(value, board=board)
        if value != None and not isinstance(value, Scribble):
            raise ValueError("math_board Numbers need a RandomNumber or scribble object as its value")
        if board == None and value != None:
            board = value.board

        if log:
            board_message = f"{symbol}~{value.math_board_id if value != None else ' '}~{'T' if sign else 'F'}|v|_i_"
        else:
            board_message = None
        if value != None:
            value = value.block
        block = math_blocks.algebra.polynomials.Variable(symbol=symbol, value=value, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)
