from time import time
from sympy import nextprime
import numpy as np
import cProfile

def timer(func, number, iterations):
    times = []
    for _ in range(iterations):
        startTime = time()
        func(number)
        times.append(time() - startTime)
    print("--- %s seconds average for %s iterations ---" % ((sum(times) / iterations), iterations))

def mathematical(number):
    print(1)
    print(2)

    i = 3
    n = 2
    while i < number:
        n = (n - 1) * (i-1) * (i-2) + 1
        if (n % i) == 0:
            print(i)
        i += 2

def firstMe(number):
    i = 3
    n = 1
    while i < number:
        isPrime = True

        for k in range(3, i//n+1, 2):
            if i % k == 0:
                isPrime = False
                break
        if isPrime:
            print(i)

        i += 2
        if i > n**2:
            n += 2

def me(number):
    def check():
        for k in primes[:n+1]:
            if i % k == 0:
                return False
        return True

    primes = []
    i = 5
    n = 0
    while i < number:
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

def library(number):
    i = 1
    while i < number:
        #print(i)
        i =  nextprime(i)

# Define a function that accepts a number as an argument
def chatGPT(number):
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

def me_and_chatGPT(number):
    sieve = np.ones(number+1, dtype=bool)
    sieve[0] = sieve[1] = False

    for i in range(2, int(number**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = False
    
    primes = np.flatnonzero(sieve)
    return primes

# To 10000000
# Me: --- 43.81807827949524 seconds ---
# External library: --- 26.992177724838257 seconds ---
# Ai: --- 7.066962003707886 seconds ---

timer(me_and_chatGPT, 1_000_000_000, 10)

#cProfile.run("me_and_chatGPT(10000000)")