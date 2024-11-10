import numpy as np
from itertools import product

n = 4

def check(arr, n):
    print(arr)
    current = 0
    for index, i in enumerate(arr.flatten()):
        current = (index*i)^current

    for pos in range(n**2):
        print(pos, pos^current, f"{pos^current:b}")


for bits in product([0,1],repeat=n**2):
    arr = np.array(bits, dtype=np.uint8).reshape(n,n)

    check(arr, n)