import numpy as np

def generateBoard(n, m):
    n,m-=1
    board = np.zeros((n,m), np.uint8)

    # island
    start = (np.random.randint(1,n-1), np.random.randint(1,m-1))
    