import numpy as np
from functools import lru_cache
import cProfile
import timeit
np.set_printoptions(threshold=np.inf)

@lru_cache(maxsize=None) # if the function is called with the same arguments, it will return the cached value instead of running the function again
def check(n: str):
    sort = sorted(n)
    #if len(set(sort)) == 1: # if all elements are
    #    return "0"
    stigende = "".join(sort)
    synkende = "".join(reversed(sort))
    stigende = int(stigende)
    synkende = int(synkende)
    return str(synkende -  stigende)

# kaprekars algorythm
def kaprekars():
    results = np.zeros((9000, 2), dtype=np.int16)
    for i in range(1000, 10000):
        result = str(i)
        lastResult = result
        while True:
            result = check(result)
            if result == lastResult:# or result == "0":
                results[i - 1000] = np.array([i, result])
                break
            lastResult = result
    return results

results = kaprekars()
print(results)
secondColumn = results[:, 1]
nonZeros = secondColumn[secondColumn != 0]
print(np.all(nonZeros == 6174))             # if all nonZeros are 6174, then the algorithm works
print(set(secondColumn))                    # all uniqe ellements

cProfile.run('kaprekars()')                 # profiles how long each opperation takes
print(timeit.timeit('kaprekars()', number=100, globals=globals()) / 100) # average time