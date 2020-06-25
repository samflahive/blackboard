from math_board import decode_math_board

class Question:
    def __init__(self, board):
        self.board = board
        self.answer_type = None
        self.question_targets = None
        self.answer_targets = None
        self.blocks = None

    def setup(self):
        self.question_targets = self.board.question_targets
        if len(self.board.answer) == 1:
            self.answer_type = "expression"
            self.answer_index = self.board.answer_targets[0]
            
        elif len(self.board.answer) > 1:
            self.answer_type = "numberlist"
            self.answer_index = self.board.answer_targets
        else:
            raise ValueError("cannot have zero answer elements")

    def compress(self):
        string = ",".join(self.board.record)
        self.instructions = string

    
    def extract(self):
        blocks = decode_math_board(self.instruction)
        question_data = [blocks[index].latex() for index in self.question_targets]

        if self.answer_type == "expression":
            answer_data = blocks[self.answer_target].latex()

        elif self.answer_type == "numberlist":
            answer_data = [blocks[index].evaluate() for index in self.answer_targets]

        else:
            raise ValueError(f"Invalid answer type: {self.answer_type}")

        self.blocks = blocks

        return {"question_data": question_data,
                "answer_data": answer_data}
