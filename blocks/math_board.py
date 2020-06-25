class MathBoard:
    def __init__(self):
        self.record = []
        self.blocks = 0
        self.question_targets = []
        self.answer_targets = []

    def log(self, record):
        self.record.append(record)

    def track(self):
        self.blocks += 1
        return self.blocks - 1

    def add_question_data(self, target):
        self.question_targets.append(target.math_board_id)

    def add_answer(self, target):
        self.answer_targets.append(target.math_board_id)
