import numpy as np
from cProfile import run

def prefixSum(arr: np.ndarray) -> np.ndarray:
    prefixSum = np.zeros(len(arr))
    prefixSum[0] = arr[0]
    for i in range(1, len(arr)):
        prefixSum[i] = prefixSum[i-1] + arr[i]
    return prefixSum.astype(int)

def parallelPrefixSum(arr: np.ndarray) -> np.ndarray:
    prefixSum = arr.copy()
    for i in range(int((np.log2(len(arr))))):
        prefixSum[2**(i+1)-1::2**(i+1)] += prefixSum[2**(i)-1::2**(i+1)]
    
    for i in range(int(np.log2(len(arr)))-1, 0, -1):
        prefixSum[int(3/2*2**i)-1::2**i] += prefixSum[2**i-1:len(arr)-1:2**i]
        
    return prefixSum
    

if __name__ == '__main__':
    arr = np.random.randint(0, 1000000, size=2**24)
    run("prefixSum(arr)")
    run("parallelPrefixSum(arr)")
    #print(parallelPrefixSum(arr))
#    arr = np.arange(16)+1
#    print(prefixSum(arr))
#    print(parallelPrefixSum(arr))