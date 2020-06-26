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
        if len(self.board.answer_targets) == 1:
            self.answer_type = "expression"
            self.answer_targets = self.board.answer_targets[0]
            
        elif len(self.board.answer_targets) > 1:
            self.answer_type = "numberlist"
            self.answer_targets = self.board.answer_targets
        else:
            raise ValueError("cannot have zero answer elements")

    def compress(self):
        string = ",".join(self.board.record)
        self.instruction = string
        question_data_instructions = " ".join(str(q) for q in self.question_targets)
        if self.answer_type == "expression":
            decode_instructions = f"ex,{question_data_instructions},{self.answer_targets}"
        else:
            answer_targets_instructions = " ".join(str(q) for q in self.answer_targets)
            decode_instructions = f"nl,{question_data_instructions},{answer_targets_instructions}"

        self.decode_instructions = decode_instructions

    
    def extract(self):
        return get_question_info(self.instruction, self.decode_instructions)


def get_question_info(instructions, extraction):
    blocks = decode_math_board(instructions)
    extraction = extraction.split(",")

    question_targets = extraction[1].split(" ")
    question_targets = [int(i) for i in question_targets]
    question_data = [blocks[index].latex() for index in question_targets]

    if extraction[0] == "ex":
        answer_target = int(extraction[2])
        answer_data = blocks[answer_target].latex()
        answer_type = "expression"

    elif extraction[0] == "nl":
        answer_target  = extraction[2].split(" ")
        answer_target = [int(i) for i in answer_target]

        answer_data = [blocks[index].evaluate() for index in answer_targets]
        answer_type = "numberlist"

    else:
        raise ValueError("answers must be expressions or numberlists")

    return {"question_data":question_data, "answer_data":answer_data, "answer_type":answer_type}

