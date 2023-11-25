from methods.template import Template
from numpy import count_nonzero, setdiff1d, unique

class IntersectionRemoval(Template):
    def __init__(self, board, notes):
        super().__init__(board, notes, "Intersection Removal")

    def solve(self):
        change = False
        for i in range(9):
            for j, indicies in enumerate([[3,4,5,6,7,8], [0,1,2,6,7,8], [0,1,2,3,4,5]]):
                # row
                diff = self.notes[i][setdiff1d(range(9), indicies)]
                for n in unique(diff)[unique(diff)!=0]: # notes in that row
                    if count_nonzero(self.notes[i][indicies][:,n-1]) == 0:
                        # remove box
                        for k in range(3):
                            if k == i % 3:
                                continue
                            if count_nonzero(self.notes[3*(i//3) + k][j*3: j*3 + 3][:,n-1]) != 0:
                                change = True

                            self.notes[3*(i//3) + k][j*3: j*3 + 3][:,n-1] = 0

                # col
                diff = self.notes[:,i][setdiff1d(range(9), indicies)]
                for n in unique(diff)[unique(diff)!=0]: # notes in that col
                    if count_nonzero(self.notes[:,i][indicies][:,n-1]) == 0:
                        # remove box
                        for k in range(3):
                            if k == i % 3:
                                continue
                            if count_nonzero(self.notes[:,3*(i//3) + k][j*3: j*3 + 3][:,n-1]) != 0:
                                change = True

                            self.notes[3*(i//3) + k][j*3: j*3 + 3][:,n-1] = 0

                # box
                box = self.notes[3*(i//3):3*(i//3)+3, 3*(i%3):3*(i%3)+3]
                

        return self.board, self.notes, change