from z3 import *

# 9x9 matrix of integer variables
X = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(9) ] 
      for i in range(9) ]

# each cell contains a value in {1, ..., 9}
cells_c  = [ And(1 <= X[i][j], X[i][j] <= 9) 
             for i in range(9) for j in range(9) ]

# each row contains a digit at most once
rows_c   = [ Distinct(X[i]) for i in range(9) ]

# each column contains a digit at most once
cols_c   = [ Distinct([ X[i][j] for i in range(9) ]) 
             for j in range(9) ]

# each 3x3 square contains a digit at most once
# sq_c     = [ Distinct([ X[3*i0 + i][3*j0 + j] 
#                         for i in range(3) for j in range(3) ]) 
#              for i0 in range(3) for j0 in range(3) ]
jigsaw = [[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[1,3],[2,1],[2,2]],
          [[0,3],[0,4],[0,5],[1,4],[2,3],[2,4],[2,5],[3,4],[4,4]],
          [[0,6],[0,7],[0,8],[1,5],[1,6],[1,7],[1,8],[2,6],[2,7]],
          [[2,0],[3,0],[3,1],[4,0],[4,1],[4,2],[5,0],[5,1],[5,2]],
          [[3,2],[3,3],[4,3],[5,3],[5,4],[5,5],[4,5],[3,5],[3,6]],
          [[2,8],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]],
          [[6,0],[6,1],[6,2],[6,3],[7,0],[7,1],[7,2],[8,0],[8,1]],
          [[6,4],[7,3],[7,4],[7,5],[8,2],[8,3],[8,4],[8,5],[8,6]],
          [[6,5],[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,7],[8,8]]]

sq_c = [ Distinct([X[val[0]][val[1]] for val in piece]) for piece in jigsaw]

sudoku_c = cells_c + rows_c + cols_c + sq_c

# sudoku instance, we use '0' for empty cells
instance = [[3,0,0, 0,0,0, 0,7,0],
            [0,8,7, 0,0,0, 0,0,0],
            [0,0,0, 0,7,0, 2,0,0],

            [0,0,0, 0,0,3, 0,4,0],
            [8,0,6, 2,0,4, 5,0,0],
            [0,4,0, 9,0,0, 0,0,0],

            [0,0,9, 0,1,0, 0,0,0],
            [0,0,0, 0,0,0, 4,2,0],
            [0,0,0, 0,0,0, 0,0,1]]


instance_c = [ If(instance[i][j] == 0, 
                  True, 
                  X[i][j] == instance[i][j]) 
               for i in range(9) for j in range(9) ]

s = Solver()
s.add(sudoku_c + instance_c)
if s.check() == sat:
    m = s.model()
    r = [ [ m.evaluate(X[i][j]) for j in range(9) ] 
          for i in range(9) ]
    print_matrix(r)
else:
    print ("failed to solve")