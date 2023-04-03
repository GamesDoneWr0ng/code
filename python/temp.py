import numpy as np

prob = np.array([[1,2,3,4],
                 [1,2,3,4],
                 [1,2,3,4],
                 [1,2,3,4]])

advan = np.array([1,2,3,4])

out = np.apply_along_axis(np.multiply, 0, prob, advan.T)
print()