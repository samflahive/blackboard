from scribble import Scribble
from numbers import number, random_number

import math_blocks

class polycomp(Scribble):
    def __init__(self, expos, sign=True, board=None, log=True):
        blocks = []
        for item in expos:
            if not isinstance(item, Scribble):
                raise ValueError("math_board polycomp take math_board block objects only")
            blocks.append(item.block)
        if board == None:
            board = expos[0].board

        if log:
            board_message = f"{' '.join(str(item.math_board_id) for item in expos)}~{'T' if sign else 'F'}|pc|_i_"
        else:
            board_message = None

        block = math_blocks.polycomp(expos=blocks, sign=sign)

        Scribble.__init__(self, block=block, board=board, message=board_message)


    



