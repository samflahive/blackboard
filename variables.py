from scribble import Scribble
from numbers import number, random_number
import math_blocks

class variable(Scribble):
    def __init__(self, symbol, value=None, sign=True, board=None, log=True):
        if isinstance(value, random_number):
            value = number(value, board=board)
        if value != None and not isinstance(value, Scribble):
            raise ValueError("math_board numbers need a random_number or scribble object as its value")
        if board == None and value != None:
            board = value.board

        if log:
            board_message = f"{symbol}~{value.math_board_id if value != None else ' '}~{'T' if sign else 'F'}|v|_i_"
        else:
            board_message = None

        block = math_blocks.variable(symbol=symbol, value=value.block, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)


