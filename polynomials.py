from scribble import Scribble
from numbers import number, random_number
from polyterms import polyterm
import math_blocks

class polynomial(Scribble):
    def __init__(self, items, sign=True, board=None, log=True):
        blocks = []
        for item in items:
            if not isinstance(item, polyterm):
                raise ValueError("math_board polynomials take only math_board polyterm objects in its items list")
            blocks.append(item.block)
            
        if board == None:
            board = items[0].board

        if log:
            board_message = f"{' '.join(str(i.math_board_id) for i in items)}~{'T' if sign else 'F'}|py|_i_"
        else:
            board_message = None

        block = math_blocks.polynomial(items=blocks, sign=sign)

        Scribble(self, block=block, board=board, message=board_message)
