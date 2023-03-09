import numpy as np

test = np.array([[1,2,3],
          [4,5,6],
          [7,8,9]])

print(np.zeros_like(test) + 1)
print(test)