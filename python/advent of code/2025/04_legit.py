with open("data/04.txt") as f:
    data = f.read().split("\n")

cells = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "@":
            cells[i][j] = 1

def getMovable(cells) -> list[tuple[int, int]]:
    movable = []
    for y in range(len(cells)):
        for x in range(len(cells[y])):
            if cells[y][x] and sum(i for j in cells[max(y-1,0):y+2] for i in j[max(x-1,0):x+2]) <= 4:
                movable.append((x, y))
    return movable

movable = getMovable(cells)
total = len(movable)
print(f"part1: {total}")
while movable:
    for x,y in movable:
        cells[y][x] = 0
    movable = getMovable(cells)
    total += len(movable)

print(f"part2: {total}")