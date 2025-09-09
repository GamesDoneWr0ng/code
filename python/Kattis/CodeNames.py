n = int(input())
words = {input() for _ in range(n)}

def isSwap(word1, word2):
    c = 0
    for a,b in zip(word1, word2):
        if a != b:
            if c == 2:
                return False
            c += 1
    return True

free = 0
edges = dict()
for i in words:
    newEdges = set()
    for j in words:
        if i != j and isSwap(i, j):
            newEdges.add(j)
    edges[i] = newEdges

while len(edges)!=0 and len(min(edges.values(), key=len)) <= 1:
    for key, item in edges.items():
        if len(item) == 0:
            free += 1
            words.remove(key)
            for k, v in edges.items():
                if key in v:
                    v.remove(key)
            del edges[key]
            break
        elif len(item) == 1:
            free += 1
            other = next(iter(item))
            words.remove(key)
            words.remove(other)
            for k, v in edges.items():
                if key in v:
                    v.remove(key)
                if other in v:
                    v.remove(other)
            del edges[key]
            del edges[other]
            break

if len(edges) == 0:
    print(free)
    exit()

subsets = []
while len(words) != 0:
    i = next(iter(words))
    newSubset = [i]
    remaining = [i]
    minDegree = len(edges[i])
    while len(remaining) != 0:
        current = remaining.pop()
        minDegree = max(minDegree, len(edges[current]))
        for j in edges[current]:
            if j not in newSubset:
                newSubset.append(j)
                remaining.append(j)
    if minDegree == 2:
        free += len(newSubset) // 2
    else:
        subsets.append(newSubset)
    for i in newSubset:
        words.remove(i)

def compute(current, index=0, maxsize=0, words:set=words, n=n, edges:dict[str,set]=edges) -> int:
    while index < n:
        if not edges[words[index]].isdisjoint(current):
            index += 1
            continue

        size = compute(current+[words[index]], index+1, len(current)+1, words=words,n=n)
        if size > maxsize:
            maxsize = size
            for i in words:
                for j in words:
                    if i != j and j not in edges[i] and n - len(edges[i].union(edges[j])) < maxsize:
                        edges[i].add(j)
                        edges[j].add(i)
        index += 1
    
    return maxsize

print(sum(compute([], words=i, n=len(i)) for i in subsets) + free)