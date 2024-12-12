from collections import Counter
from time import time
data = Counter([28, 4, 3179, 96938, 0, 6617406, 490, 816207])
#data = [125, 17]

def split(data:Counter=data):
    nextIter = Counter()
    keys = data.keys()
    for i in keys:
        if i == 0:
            nextIter[1] += data[0]
        elif len(str(i))%2 == 0:
            text = str(i)
            nextIter[int(text[len(text)//2:])] += data[i]
            nextIter[int(text[:len(text)//2])] += data[i]
        else:
            nextIter[i*2024] += data[i]
    #print(data)
    return nextIter

start = time()
for i in range(1000):
    data = split(data)
    #print(i)
print(time()-start)
print(sum(data.values()))
print(len(data))