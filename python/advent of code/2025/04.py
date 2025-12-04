import numpy as np
from scipy.signal import convolve2d
import sys
np.set_printoptions(threshold=sys.maxsize)

with open("data/04.txt") as f:
    data = f.read().split("\n")

cells = np.zeros((len(data), len(data[0])), dtype=np.uint8)
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "@":
            cells[i][j] = 1

kernel = np.ones((3, 3), np.uint8)
kernel[1, 1] = 0
count = 0
while True:
    neighbors = convolve2d(cells, kernel, mode="same", boundary="fill", fillvalue=0)
    movable = np.logical_and(neighbors < 4, cells == 1)
    if not np.any(movable):
        break
    count += np.sum(movable)
    cells[movable] = 0

print(count)
