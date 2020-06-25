from .scribble import Scribble
from .numbers import Number, RandomNumber
import math_blocks.algebra.core

class Product(Scribble):
    def __init__(self, items, sign=True, board=None, log=True):
        mb_items = []
        blocks = []
        for item in items:
            if isinstance(item, RandomNumber):
                item = Number(item, board=item.board)
            if not isinstance(item, Scribble):
                raise ValueError("math_board product need a math_board block objects only")

            mb_items.append(item)
            blocks.append(item.block)
            
        if board == None:
            board = mb_items[0].board

        if log:
            board_message = f"{' '.join(str(item.math_board_id) for item in mb_items)}~{'T' if sign else 'F'}|p|_i_"
        else:
            board_message = None

        block = math_blocks.algebra.core.Product(items=blocks, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)

