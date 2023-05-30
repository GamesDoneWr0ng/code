from cProfile import run
import timeit
from numba import jit

# implementation for fast modular exponentiation
# set variabels
# a**b % n
a = 987654567876542332458764534255676325476568798706859647506429857698271233459857398475981379890765897586457984675343546263542351243543546756579656879860790869758956475632432354357696807980890789676745463453654657686
b = 3_456_765_676_545_678_876_978_654_356_768_769_870_123_435_465_768_798_700_968_856_429_857_698_273_459_857_398_475_981_379_890_765_897_586_457_984_675_343_546_263_123_542_351_243_543_546_756_579_656_879_860_790_869_758_956_475_632_432_354_357_696_807_980_890_789_676_745_463_453_654_657_687
n = 34567876543456794235367897098675243546576789980765675646576789658746429857698273459857398475981379890765897586457984675343546263542351243543546756579656879860123790869758956475632432354357696807980890789676745463453654657687
# a**b har sirka (len(a) - 1) * b siffer eller 1 kvintrigintilliard siffer på det korte tellesystemet blir dette 1 duoseptuagintillion

# check for huge numbers will this take more time than the heat death of the universe.
#print(timeit.timeit(f"({a}**{b}) % {n}", number=1) / 1)
#expected = (a**b) % n

# convert b to binary and reverses
b = f"{b:b}"[::-1]

# the thing
def fastModularExponetiation(a=a, b=b, n=n):
    sum = 1
    d = a % n
    for i in b:
        if i == "1":
            sum = (sum * d) % n
        d = (d*d) % n
    return sum

#print(expected)
print(timeit.timeit(fastModularExponetiation, number=1000) * 0.001)
print(fastModularExponetiation())
#run("fastModularExponetiation()")