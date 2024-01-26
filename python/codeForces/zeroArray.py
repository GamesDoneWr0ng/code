import numpy as np
import cProfile
import time
def timer(func, args, iters = 100):
    times = []
    for _ in range(iters):
        start = time.time_ns()
        func(args)
        times.append(time.time_ns() - start)
    return sum(times) / len(times)

n = np.random.randint(2, 10**5+1)
a = np.random.randint(1, 10**9+1, n)

def zeroArray(a):
    a %= 2
    return ("YES" if np.count_nonzero(a) %2 == 0 else "NO")

print(n)
print(a)
print()
zeroArray(a)
print(timer(zeroArray, args=a, iters=100000))