def checkCyclic(n):
    if (n != round(n)):
        return False
    n = int(n)

    i = 2
    while True:
        multiple = str(n*i)
        if len(str(n)) != len(multiple):
            return False
        for j in range(len(multiple)):
            if multiple[j:] + multiple[:j] == str(n):
                i += 1
        if i == len(str(n)):
            return True

p = 1
while True:
    p += 4
    number = (10**(p-1)-1)/p
    if checkCyclic(number):
        print(number)
    
    p += 2
    number = (10**(p-1)-1)/p
    if checkCyclic(number):
        print(number)