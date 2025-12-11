import matplotlib.pyplot as plt
import numpy as np

with open("data/09.txt") as f:
    data = f.read().split("\n")

# data: list[str] = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3""".split("\n")

# points = list(map(lambda x: tuple(map(lambda x: int(x), x.split(","))), data))
points = list(map(lambda x: tuple(map(lambda x: int(x)//100, x.split(","))), data))

# p,q=(4806,66418), (94664,50278)
# plt.plot(list(map(lambda x: x[0], points)), list(map(lambda x: x[1], points)), c="red", marker='o', linestyle='--')
# plt.plot([p[0], p[0], q[0], q[0], p[0]], [p[1], q[1], q[1], p[1], p[1]], c="blue", marker='o', linestyle='--')
# plt.show()

def isGreen(p, q, perimeter):
    mn = (min(p[0], q[0]), min(p[1], q[1]))
    mx = (max(p[0], q[0]), max(p[1], q[1]))

    return not np.any(perimeter[mn[0]:mx[0]+1, mn[1]:mx[1]+1])

perimeter = np.zeros((max(map(lambda x: x[0], points))+3, max(map(lambda x: x[1], points))+3), dtype=bool)
for i in range(len(points) - 1):
    mn = (min(points[i][0], points[i+1][0]), min(points[i][1], points[i+1][1]))
    mx = (max(points[i][0], points[i+1][0]), max(points[i][1], points[i+1][1]))
    perimeter[mn[0]:mx[0]+1, mn[1]:mx[1]+1] = True

perimeter[min(points[0][0], points[-1][0]):max(points[0][0]+1, points[-1][0]), min(points[0][1], points[-1][1]):max(points[0][1], points[-1][1])+1] = True

opened = {(0,0)}
while len(opened) != 0:
    p = np.array(opened.pop())
    perimeter[*p] = True
    for i in map(np.array, [(1,0), (0,1), (-1,0), (0,-1)]):
        if tuple(p+i) not in opened and np.all(p+i>=0) and np.all((p+i)<perimeter.shape) and not perimeter[*(p+i)]:
            opened.add(tuple(p+i))

for i in range(len(points) - 1):
    mn = (min(points[i][0], points[i+1][0]), min(points[i][1], points[i+1][1]))
    mx = (max(points[i][0], points[i+1][0]), max(points[i][1], points[i+1][1]))
    perimeter[mn[0]:mx[0]+1, mn[1]:mx[1]+1] = False
perimeter[min(points[0][0], points[-1][0]):max(points[0][0], points[-1][0])+1, min(points[0][1], points[-1][1]):max(points[0][1], points[-1][1])+1] = False

maxSize = 0
for i, p in enumerate(points):
    for j, q in enumerate(points):
        size = (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)
        if size > maxSize and isGreen(p, q, perimeter):
            maxSize = size
            print(p,q, i, j)
            print(f"p,q=({data[i]}), ({data[j]})")


print(maxSize)