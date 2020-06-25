class MathBoard:
    def __init__(self):
        self.record = []
        self.blocks = 0

    def log(self, record):
        self.record.append(record)

    def track(self):
        self.blocks += 1
        return self.blocks - 1
