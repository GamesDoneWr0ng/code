"""You are given an array 𝑎1,𝑎2,…,𝑎𝑛
, where each element is an integer from 1
 to 𝑥
.

You can perform the following operation with it any number of times:

choose three integers 𝑙
, 𝑟
 and 𝑘
 such that 1≤𝑙≤𝑟≤𝑛
, 1≤𝑘≤𝑥
 and each element 𝑎𝑖
 such that 𝑙≤𝑖≤𝑟
 is different from 𝑘
. Then, for each 𝑖∈[𝑙,𝑟]
, replace 𝑎𝑖
 with 𝑘
.
In other words, you choose a subsegment of the array and an integer from 1
 to 𝑥
 which does not appear in that subsegment, and replace every element in the subsegment with that chosen integer.

Your goal is to make all elements in the array equal. What is the minimum number of operations that you have to perform?

Input
The first line contains one integer 𝑡
 (1≤𝑡≤100
) — the number of test cases.

Each test case consists of two lines:

the first line contains two integers 𝑛
 and 𝑥
 (1≤𝑥≤𝑛≤100
);
the second line contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤𝑥
).
Additional constraint on the input: the sum of 𝑛
 over all test cases does not exceed 500
.

Output
For each test case, print one integer — the minimum number of operations you have to perform."""
import numpy as np
from cProfile import run

x = np.random.randint(1, 101)
n = np.random.randint(x, 101)
a = np.random.randint(1, x+1, n)

print(n,x)
print(a)

def replaceOnSegment(a, x):
    if len(set(a)) == 1:
        return 0
    minimum = np.zeros(x, dtype=np.int16)
    last = a[0]
    for i in a[1:]:
        if last == i:
            continue
        else:
            minimum[i-1] += 1
        last = i
    return minimum+1

print(replaceOnSegment(a,x))
#run("replaceOnSegment(a,x)")

#print(replaceOnSegment([3, 3], 3))