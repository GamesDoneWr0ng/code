from itertools import combinations, pairwise

points = list(map(eval, open("data/09.txt")))
a = b = 0

for (x,y), (u,v) in combinations(points, 2):
    x, u = sorted((x, u))
    y, v = sorted((y, v))
    size = (u - x + 1) * (v - y + 1)

    a = max(a, size)

    for (p,q), (r,s) in pairwise(points + [points[0]]):
        p,r = sorted((p,r))
        q,s = sorted((q,s))
        if all((x<r, u>p, y<s, v>q)): break

    else: b = max(b, size)

print(a, b)