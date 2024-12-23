from itertools import permutations
from functools import cache
data = """029A
980A
179A
456A
379A"""

data = """208A
586A
341A
463A
593A"""

positions = {"7": 0+0j,
             "8": 1+0j,
             "9": 2+0j,
             "4": 0+1j,
             "5": 1+1j,
             "6": 2+1j,
             "1": 0+2j,
             "2": 1+2j,
             "3": 2+2j,
             "0": 1+3j,
             "A": 2+3j,

             "^": 1+0j,
             "a": 2+0j,
             "<": 0+1j,
             "v": 1+1j,
             ">": 2+1j}

directions = {"^": -1j,
              ">":  1,
              "v":  1j,
              "<": -1}

def getMoveSet(start, end, avoid):
    dz = end-start
    s = ""

    if dz.real > 0:
        s += ">" * int(dz.real)
    else:
        s += "<" * int(abs(dz.real))
    if dz.imag > 0:
        s += "v" * int(dz.imag)
    else:
        s += "^" * int(abs(dz.imag))

    moves = ["".join(p)+"a" 
             for p in set(permutations(s)) 
             if sum(
                 sum(directions[d] for d in p[:i])+start == avoid
                 for i in range(len(p))
                 ) == 0]
    #print(moves)
    return moves

@cache
def getShortestPath(s, lim=2, depth=0):
    a = "A" if depth == 0 else "a"
    avoid = positions[a]-2
    pos = positions[a]
    lenght = 0

    for i in s:
        nextPos = positions[i]
        moveSet = getMoveSet(pos, nextPos, avoid)
        if depth == lim:
            lenght += len(moveSet[0])
        else:
            lenght += min(getShortestPath(move, lim, depth+1) for move in moveSet)
        pos = nextPos
    return lenght

totalComplexity = 0
for i in data.split("\n"):
    totalComplexity += getShortestPath(i, 25) * int(i[:-1])
print(totalComplexity)