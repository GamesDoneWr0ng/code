from methods.template import Template
class NakedCandidates(Template):
    def __init__(self, board, notes):
        super().__init__(board, notes)

    def solve(self):
        change = False
        for i, col in enumerate(self.board):
            for j, cell in enumerate(col):
                pass
        return self.board, self.notes, change