from copy import copy

def step(seen=None, last=0, length = 4):
    if seen==None:
        seen = [[0]*length, [1]+[0]*(length-1)]
    if len(seen) == 2**length:
        #if last == length-1:
        for i in seen:
            print(i)
        return
    if last != 0:
        new = copy(seen[-1])
        new[last-1] ^= 1
        if new not in seen:
            step(seen + [new], last-1, length)
    if last != length-1:
        new = copy(seen[-1])
        new[last+1] ^= 1
        if new not in seen:
            step(seen + [new], last+1, length)

step(length=7)