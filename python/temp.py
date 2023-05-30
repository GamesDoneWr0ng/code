i = 0

def getSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum

while i < 10000:
    print(getSum(getSum(i)))
    i += 9