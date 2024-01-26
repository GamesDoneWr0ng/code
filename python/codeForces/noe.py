"""Alex doesn't like boredom. That's why whenever he gets bored, he comes up with games. One long winter evening he came up with a game and decided to play it.

Given a sequence a consisting of n integers. The player can make several steps. In a single step he can choose an element of the sequence (let's denote it ak) and delete it, at that all elements equal to ak + 1 and ak - 1 also must be deleted from the sequence. That step brings ak points to the player.

Alex is a perfectionist, so he decided to get as many points as possible. Help him.

Input
The first line contains integer n (1 ≤ n ≤ 105) that shows how many numbers are in Alex's sequence.

The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 105).

Output
Print a single integer — the maximum number of points that Alex can earn.

"""

import numpy as np
import cProfile

n = 10**5#np.random.randint(1, 10**5)
a = np.random.randint(1, 10**5, n, dtype=np.uint32)

print(n)
print(a)

def boredom(a):
    sum = np.zeros(np.max(a), dtype=np.uint32)
    for i in a:
        sum[i-1] += i

    score = 0
    i = 0
    lenght = len(sum)
    while i+3 < lenght:
        if sum[i] == 0:
            i += 1
        elif sum[i] > sum[i+1]:
            score += sum[i]
            sum[i:i+2] = 0
            i += 2
        elif sum[i+1] > sum[i+2]:
            score += sum[i+1]
            sum[i:i+3] = 0
            i += 3
        else:
            j = 0
            while sum[i+j] < sum[i+j+1]:
                j+=1
                if i+j+1 >= lenght:
                    break

            score += np.sum(sum[i+j:i-1 if i-1 >= 0 else None:-2])
            sum[i:i+j+2] = 0
            i += j
    score += np.max(sum[-3:])
    return int(score)

#cProfile.run("theThing(a)")
print(boredom(a))