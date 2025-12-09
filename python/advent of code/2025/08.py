import numpy as np

with open("data/08.txt") as f:
    data = f.read().split("\n")

# data = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689""".split("\n")

points = [np.array(list(map(int, line.split(",")))) for line in data]

distances = np.array([[(np.sum((p-q)**2) if not np.all(p==q) else np.inf) for q in points] for p in points])

connections: dict[int, list[int]] = dict()

#for _ in range(1000):
while True:
    minIdx, minPair = np.unravel_index(np.argmin(distances), distances.shape)

    if minIdx in connections and minPair in connections[minIdx]:
        pass
    elif minIdx in connections and minPair in connections:
        connections[minIdx] += connections[minPair]
        for i in connections[minPair]:
            connections[i] = connections[minIdx]

        # part 2 check
        if len(connections[minIdx]) == len(points):
            print(points[minIdx][0] * points[minPair][0])
            break
    elif minIdx in connections:
        connections[minIdx].append(minPair)
        connections[minPair] = connections[minIdx]
    elif minPair in connections:
        connections[minPair].append(minIdx)
        connections[minIdx] = connections[minPair]
    else:
        connections[minIdx] = [minIdx, minPair]
        connections[minPair] = connections[minIdx]

    distances[minPair][minIdx] = np.inf
    distances[minIdx][minPair] = np.inf

sizes = []
while len(connections) != 0:
    _, nodes = connections.popitem()
    sizes.append(len(nodes))
    for node in nodes:
        if node in connections:
            del connections[node]

sizes.sort(reverse=True)
from math import prod
print(prod(sizes[:3]))