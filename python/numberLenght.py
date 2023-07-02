import numpy as np
from functools import lru_cache
import cProfile

words = {
    1: 'en',
    2: 'to',
    3: 'tre',
    4: 'fire',
    5: 'fem',
    6: 'seks',
    7: 'sju',
    8: 'åtte',
    9: 'ni',
    10: 'ti',
    11: 'elleve',
    12: 'tolv',
    13: 'tretten',
    14: 'fjorten',
    15: 'femten',
    16: 'seksten',
    17: 'sytten',
    18: 'atten',
    19: 'nitten',
    20: 'tjue',
    30: 'treti',
    40: 'førti',
    50: 'femti',
    60: 'seksti',
    70: 'sytti',
    80: 'åtti',
    90: 'nitti'
}

@lru_cache(maxsize=2000)
def numberToString(n, et = False):
    if n == 1 and et:
        return 'ett'
    
    string = ''
    if n in words:
        return words[n]

    t = n // 1000
    if t > 0:
        string += numberToString(t, True) + 'tusen'
        n = n % 1000

    t = n // 100
    if t > 0:
        string += numberToString(t, True) + 'hundre'
        n = n % 100
        if n > 0:
            string += 'og'

    if n in words:
        return string + words[n]

    t = n // 10
    if t > 0:
        string += numberToString(10 * t)
        n = n % 10

    if n > 0:
        string += words[n]
    
    return string

#lenghts = np.array([0] * 999999)
#counts = np.array([0] * 999999)
#finals = np.array([0] * 999999)
#print(np.max(lenghts))
#for i in range(1, 1000000):
#    lenght = len(numberToString(i))
#    lenghts[i-1] = lenght
#    count = 1
#    while lenght != len(numberToString(lenght)):
#        lenght = len(numberToString(lenght))
#        count += 1
#
#    counts[i-1] = count
#    finals[i-1] = lenght
#
#    string = numberToString(i)
#    print(f"{i}: {string}, {len(string)}, {count}")

cProfile.run('[numberToString(i) for i in range(1, 1000000)]')
print()
#[numberToString(i) for i in range(1, 1000000)]

#print(np.max(lenghts))
#print(np.unique(finals, return_counts=True)[1])
#print([i / 999999 for i in np.unique(finals, return_counts=True)[1]])