from scribble import Scribble
from numbers import number, random_number
import math_blocks

class chain(Scribble):
    def __init__(self, items, sign=True, board=None, log=True):
        mb_items = []
        blocks = []
        for item in items:
            if isinstance(item, random_number):
                item = number(item, board=item.board)
            if not isinstance(item, Scribble):
                raise ValueError("math_board chain need a math_board block objects only")

            mb_items.append(item)
            blocks.append(item.block)
            
        if board == None:
            board = mb_items[0].board

        if log:
            board_message = f"{' '.join(str(item.math_board_id) for item in mb_items)}~{'T' if sign else 'F'}|c|_i_"
        else:
            board_message = None

        block = math_blocks.chain(items=blocks, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)




