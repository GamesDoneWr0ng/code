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


# Me
startTime = time()

def check():
    for k in primes[:n+1]:
        if i % k == 0:
            return False

    return True

primes = []
i = 5
n = 0
while i < 1000000:
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


# External library
from sympy import nextprime
startTime = time()

i = 1
while i < 1000000:
    #print(i)
    i =  nextprime(i)

print("--- %s seconds ---" % (time() - startTime))
sleep(3)


# Ai
# Define a function that accepts a number as an argument
def calculate_primes(number):
  # Create a list of all numbers from 2 to the given number
  numbers = [i for i in range(2, number+1)]

  # Use a for loop to iterate over the numbers in the list
  for i in numbers:
    # If the current number is not prime, remove it from the list
    if i == -1:
      continue
    for j in range(i*i, number+1, i):
      numbers[j-2] = -1

  # Return the list of prime numbers
  return [i for i in numbers if i != -1]

startTime = time()

# Call the function to calculate the prime numbers up to 1000000
x=calculate_primes(1000000)

print("--- %s seconds ---" % (time() - startTime))

#print(x)

# To 10000000
# Me: --- 43.81807827949524 seconds ---
# External library: --- 26.992177724838257 seconds ---
# Ai: --- 7.066962003707886 seconds ---