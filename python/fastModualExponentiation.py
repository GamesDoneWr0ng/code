from cProfile import run

# implementation for fast modular exponentiation
# set variabels
# a**b % n
a = 9876500
b = 123400
n = 12355700

# check
expected = (a**b) % n

# convert b to binary and reverses
b = f"{b:b}"[::-1]

# the thing
def fastModularExponetiation(a=a, b=b, n=n):
    sum = 1
    d = -1
    for i in b:
        d = a % n if d == -1 else (d*d) % n
        if i == "1":
            sum *= d
    sum %= n
    return sum

print(expected)
print(fastModularExponetiation())
#run("fastModularExponetiation()")