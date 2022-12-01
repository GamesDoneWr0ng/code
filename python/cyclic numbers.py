import re

REPEATER = re.compile(r"(.+?)\1+$")

def repeated(s):
    match = REPEATER.match(s)
    return True if match else False

def repeat(string):
    if repeated(string):
        return False
    for i in range(10):
        if repeated(string+str(i)):
            return False
        if repeated(string[:-i]):
            return False
    return True
    
i = 2
while True:
    n = (10**i)-1
    if n % (i+1) == 0:
        n = str(n // (i+1))
        if repeat(n):
            print('(10^{}-1)/{} = {}  {}'.format(i, i+1, n, len(n)))
    i = i + 2