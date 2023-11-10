from methods.template import Template
from numpy import count_nonzero, argmax
class HiddenSingles(Template):
    def __init__(self, board, notes):
        super().__init__(board, notes)

    def solve(self):
        change = False
        for i in range(9):
            for n in range(9):
                if count_nonzero(self.noteGetRow(i)[:,n]) == 1:
                    change = True
                    self.board[i][argmax(self.noteGetRow(i)[:,n])] = n+1
                    self.notes[i][argmax(self.noteGetRow(i)[:,n])] = 0
                if count_nonzero(self.noteGetCol(i)[:,n]) == 1:
                    change = True
                    self.board[:,i][argmax(self.noteGetCol(i)[:,n])] = n+1
                    self.notes[:,i][argmax(self.noteGetCol(i)[:,n])] = 0
                if count_nonzero(self.noteGetBox(i)[:,n]) == 1:
                    change = True
                    box_row, box_col = divmod(i, 3)  # get box row and column
                    cell_idx = argmax(self.noteGetBox(i)[:,n])  # get cell index within box
                    cell_row, cell_col = divmod(cell_idx, 3)  # get cell row and column within box
                    self.board[box_row*3 + cell_row][box_col*3 + cell_col] = n+1  # set value in board
                    self.notes[box_row*3 + cell_row][box_col*3 + cell_col] = 0  # set value in notes
        return self.board, self.notes, change