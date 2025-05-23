from z3 import *
# We know each queen must be in a different row.
# So, we represent each queen by a single integer: the column position
Q = [ Int('Q_%i' % (i + 1)) for i in range(8) ]

# Each queen is in a column {1, ... 8 }
val_c = [ And(1 <= Q[i], Q[i] <= 8) for i in range(8) ]

# At most one queen per column
col_c = [ Distinct(Q) ]

# Diagonal constraint
diag_c = [ If(i == j, 
              True, 
              And(Q[i] - Q[j] != i - j, Q[i] - Q[j] != j - i)) 
           for i in range(8) for j in range(i) ]

#solve(val_c + col_c + diag_c)
solver = Solver()
solver.add(val_c + col_c + diag_c)
n = 0
while solver.check() == sat:
    n += 1
    print(solver.model())
    solver.add(Or([q != solver.model()[q] for q in Q]))
print(n)