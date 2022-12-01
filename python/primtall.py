from time import time, sleep

#startTime = time()
#
#print(1)
#print(2)
#
#i = 3
#n = 2
#while i < 10000:
#    n = (n - 1) * (i-1) * (i-2) + 1
#    if (n % i) == 0:
#        print(i)
#    i += 2
#
#print("--- %s seconds ---" % (time() - startTime))
#sleep(3)
#
#
#
#startTime = time()
#
#i = 3
#n = 1
#while i < 100000:
#    isPrime = True
#
#    for k in range(3, i//n+1, 2):
#        if i % k == 0:
#            isPrime = False
#            break
#    if isPrime:
#        print(i)
#
#    i += 2
#    if i > n**2:
#        n += 2
#
#print("--- %s seconds ---" % (time() - startTime))
#sleep(3)



startTime = time()

def check():
    for k in primes[:n+1]:
        if i % k == 0:
            return False

    return True

primes = []
i = 5
n = 0
while i < 10000000:
    if check():
        #print(i)
        primes.append(i)

    i += 2

    if check():
        #print(i)
        primes.append(i)

    i += 4

    if i > primes[n]**2:
        n += 1

print("--- %s seconds ---" % (time() - startTime))
sleep(3)


from sympy import nextprime
startTime = time()

i = 1
while i < 10000000:
    #print(i)
    i =  nextprime(i)

print("--- %s seconds ---" % (time() - startTime))