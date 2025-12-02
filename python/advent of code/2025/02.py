with open("data/02.txt") as f:
    data = f.read().strip().split(",")

# data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".split(",")

def getInvalid(low, high):
    inValid = set()

    n = 2
    while n <= len(high):
        if len(low) == len(high) and len(low) % n == 1:
            n += 1
            continue

        l = int(low)
        h = int(high)
        while l <= h:
            newLow = str(l)
            if len(newLow) % n != 0:
                l = int("1"+"0"*len(newLow))
                continue
            if int(low) <= int(newLow[:len(newLow) // n] * n) <= h:
                inValid.add(int(newLow[:len(newLow) // n] * n))
            l = int(str(int(newLow[:len(newLow) // n]) + 1) + "0" * (len(newLow) // n) * (n-1))

        n += 1

    return inValid

result = 0
for i in data:
    low, high = i.split("-")
    result += sum(getInvalid(low, high))
print(result)