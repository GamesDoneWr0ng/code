from methods.template import Template
from numpy import count_nonzero, argmax, zeros
class HiddenSingles(Template):
    def __init__(self, board, notes):
        super().__init__(board, notes)

    def solve(self):
        changes = zeros((9,9))
        for i in range(9):
            for n in range(9):
                if count_nonzero(self.noteGetRow(i)[:,n]) == 1:
                    changes[i][argmax(self.noteGetRow(i)[:,n])] = n+1

                if count_nonzero(self.noteGetCol(i)[:,n]) == 1:
                    changes[:,i][argmax(self.noteGetCol(i)[:,n])] = n+1
                    
                if count_nonzero(self.noteGetBox(i)[:,n]) == 1:
                    box_row, box_col = divmod(i, 3)  # get box row and column
                    cell_idx = argmax(self.noteGetBox(i)[:,n])  # get cell index within box
                    cell_row, cell_col = divmod(cell_idx, 3)  # get cell row and column within box
                    changes[box_row*3 + cell_row][box_col*3 + cell_col] = n+1
        self.board[changes != 0] = changes[changes != 0]
        self.notes[changes != 0] = 0
        return self.board, self.notes, len(changes.nonzero()) != 0