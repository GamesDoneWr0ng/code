"""We saw the little game Marmot made for Mole's lunch. Now it's Marmot's dinner time and, as we all know, Marmot eats flowers. At every dinner he eats some red and white flowers. Therefore a dinner can be represented as a sequence of several flowers, some of them white and some of them red.

But, for a dinner to be tasty, there is a rule: Marmot wants to eat white flowers only in groups of size k.

Now Marmot wonders in how many ways he can eat between a and b flowers. As the number of ways could be very large, print it modulo 1000000007 (109 + 7).

Input
Input contains several test cases.

The first line contains two integers t and k (1 ≤ t, k ≤ 10**5), where t represents the number of test cases.

The next t lines contain two integers a_i and b_i (1 ≤ a_i ≤ b_i ≤ 10**5), describing the i-th test.

Output
Print t lines to the standard output. The i-th line should contain the number of ways in which Marmot can eat between ai and bi flowers at dinner modulo 1000000007 (109 + 7).

Examples
input
3 2
1 3
2 3
4 4
output
6
5
5

Note
For K = 2 and length 1 Marmot can eat (R).
For K = 2 and length 2 Marmot can eat (RR) and (WW).
For K = 2 and length 3 Marmot can eat (RRR), (RWW) and (WWR).
For K = 2 and length 4 Marmot can eat, for example, (WWWW) or (RWWR), but for example he can't eat (WWWR).
"""

import numpy  as np
from math import comb
import cProfile

k = np.random.randint(1,10**4)
a = np.random.randint(1,10**5)
b = np.random.randint(1,10**5)

print(k)
print(a, b)

def count_flowers(k=k,a=a,b=b):
    sets = a // k
    count = comb(sets + b, b)
    return count

#print(count_flowers(1, 100000, 100000))
cProfile.run('count_flowers(1, 100000, 100000)')