from methods.template import Template
from numpy import count_nonzero
class LastPosibleNumber(Template):
    def __init__(self, board, notes):
        super().__init__(board, notes)

    def solve(self):
        change = False
        for i in range(9):
            for j in range(9):
                if count_nonzero(self.notes[i][j]) == 1:
                    change = True
                    self.board[i][j] = int(self.notes[i][j].nonzero()[0])+1
                    self.notes[i][j] = 0

        return self.board, self.notes, change