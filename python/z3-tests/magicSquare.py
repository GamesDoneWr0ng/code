import z3

size = 4
sum = 34
offset = 1
square = [[z3.Int(f"x_{i}_{j}") for j in range(size)] for i in range(size)]
top_c = [square[0][0] == 20, square[0][1] == 6, square[0][2] == 9, square[0][3] == 22]

range_c = [z3.And(1 <= i, i <= size**2) for row in square for i in row]
uniqe_c = [z3.Distinct([i for row in square for i in row])]
row_c   = [z3.Sum(i) == sum for i in square]
col_c   = [z3.Sum([square[j][i] for j in range(size)]) == sum for i in range(size)]
diag_c  = [z3.And(z3.And([z3.Sum([square[i]   [(i+j)%size] for i in range(size)]) == sum for j in range(size)]), 
                  z3.And([z3.Sum([square[-i-1][(i+j)%size] for i in range(size)]) == sum for j in range(size)]))]
small_c = [z3.Sum([square[i][j],          square[i][(j+1)%size], 
                   square[(i+1)%size][j], square[(i+1)%size][(j+1)%size]]) == sum 
                   for i in range(size) for j in range(size)]


solver = z3.Solver()
solver.add(range_c + uniqe_c + row_c + col_c + diag_c + small_c)
if solver.check() == z3.sat:
    m = solver.model()
    for row in range(size):
        string = ""
        for col in range(size):
            string += (str(m.evaluate(square[row][col])).zfill(2) + " ")
        print(string)
else:
    print("no solution found")