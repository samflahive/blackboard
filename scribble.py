class Scribble:
    def __init__(self, block, board=None, message=None):
        if board == None:
            raise ValueError("scribble objects require a math_board")
        self.block = block
        self.board = board
        if message != None:
            self.board.log(message)

        self.math_board_id = self.board.track()

    def latex(self):
        return self.block.latex()

    def evaluate(self):
        return self.block.evaluate()

    def __add__(self, other):
        self.board.log(f"{self.math_board_id}~{other.math_board_id}|+|op")
        block = self.block + other.block

        return Scribble(block=block, board=self.board)

    def __mul__(self, other):
        self.board.log(f"{self.math_board_id}~{other.math_board_id}|*|op")
        block = self.block * other.block

        return Scribble(block=block, board=self.board)

    def __truediv__(self, other):
        self.board.log(f"{self.math_board_id}~{other.math_board_id}|/|op")
        block = self.block / other.block

        return Scribble(block=block, board=self.board)

    def __sub__(self, other):
        self.board.log(f"{self.math_board_id}~{other.math_board_id}|-|op")
        block = self.block - other.block

        return Scribble(block=block, board=self.board)
