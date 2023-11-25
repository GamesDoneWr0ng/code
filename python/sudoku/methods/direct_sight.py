from numpy import any
from methods.template import Template
class DirectSight(Template):
    def __init__(self, board, notes):
        super().__init__(board, notes, "Direct Sight")

    def solve(self):
        change = False
        for i, col in enumerate(self.board):
            for j, cell in enumerate(col):
                if cell:
                    if not change:
                        change = any(self.notes[i][:,cell-1] != 0) or any(self.notes[:,j][:,cell-1] != 0)
                    self.notes[i][:,cell-1] = 0 # col
                    self.notes[:,j][:,cell-1] = 0 # row
                    # 3x3 box
                    box_i = i // 3
                    box_j = j // 3
                    if not change:
                        change = any(self.notes[box_i*3:box_i*3+3,box_j*3:box_j*3+3].reshape(9,9)[:,cell-1] != 0)
                    self.notes[box_i*3:box_i*3+3,box_j*3:box_j*3+3][0][:,cell-1] = 0
                    self.notes[box_i*3:box_i*3+3,box_j*3:box_j*3+3][1][:,cell-1] = 0
                    self.notes[box_i*3:box_i*3+3,box_j*3:box_j*3+3][2][:,cell-1] = 0
        return self.board, self.notes, change