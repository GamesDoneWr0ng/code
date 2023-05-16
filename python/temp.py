import numpy as np
import cProfile
import timeit

def primes(n):
    """returns a list of all primes up til n as fast as posible using numpy and numba for max speed"""
    primes = np.ones(n+1, dtype=np.bool)
    primes[0] = primes[1] = False

    for i in range(2, int(np.sqrt(n))+1):
        if primes[i]:
            primes[i*i:n+1:i] = False
    return np.where(primes)[0]

#print(timeit.timeit("primes(10_000_000)", number=10, globals=globals()))
cProfile.run("primes(10_000_000)")
#print(primes(10_000_000))