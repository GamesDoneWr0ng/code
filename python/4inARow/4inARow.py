import numpy as np
from copy import deepcopy

maxDeapth = 2

board = np.zeros((6,7), dtype=np.int8)
#turn = 1
seen = {}

def check_vicinity(board, column, row, player):
    # Check horizontal, vertical, and diagonal directions
    for direction in [(0, 1), (1, 0), (1, 1), (1, -1)]:
        count = 0
        for offset in range(-3, 4):
            new_column = column + direction[0]*offset
            new_row = row + direction[1]*offset
            
            # Check if the position is valid
            if new_column >= 0 and new_column < board.shape[1] and new_row >= 0 and new_row < board.shape[0]:
                if board[new_row, new_column] == player:
                    count += 1
                    if count >= 4:
                        return True
                else:
                    count = 0

    return False

def doTurn(b, turn, column, maxDeapth, depth=0):
    if str(b) in seen:
        return seen[str(b)], column
    board = deepcopy(b)
    if depth > maxDeapth:
        return 0, column

    # apply the opponents move
    if board[0][column] != 0:
        return -2, column

    row = np.where(board[:, column] == 0)[0][-1]
    board[row][column] = -turn # -turn for opponent

    if check_vicinity(board, column, row, -turn):
        return 1, column

    # next move
    moves = np.array([doTurn(board, -turn, i, maxDeapth, depth+1) for i in range(0, board.shape[1])])
    #moves[:,0] *= turn
    if turn == 1:
        best = moves[np.argmax(moves[:,0])]
    else:
        best = moves[np.argmin(moves[:,0])]
    seen[str(b)] = best[0]
    return best[0], best[1]

def justMakeMove(board, turn, column):
    row = np.where(board[:, column] == 0)[0][-1]
    board[row][column] = turn
    if check_vicinity(board, column, row, turn):
        print(f"{turn} wins")
        print(board)
        exit()

    return board

# test
board = np.array(
[[ 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0],
 [ 0, 0, 0, 0, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0],
 [ 1, 1, 0, 0, 0, 0, 0]])
#print(doTurn(board, -1, 2, maxDeapth))
#exit()
for _ in range(board.size//2):
    player = int(input(f"{board}\nMake your move 0-6: "))
    ai = doTurn(board, -1, player, maxDeapth)
    board = justMakeMove(board, 1, player)
    board = justMakeMove(board, -1, ai[1])

print("Board is full, draw")