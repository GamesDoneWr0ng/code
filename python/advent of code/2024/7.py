from itertools import product
data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def getNumbers(string):
    result = []
    for number in string.strip().replace("  ", " ").split(" "):
        result.append(int(number))
    return result

def checkRow(row):
    goal, numbers = row.split(": ")
    goal = int(goal)
    numbers = getNumbers(numbers)

    for i in product([0,1,2], repeat=len(numbers)-1):
        result = numbers[0]
        for index, b in enumerate(i):
            if b == 0:
                result += numbers[index+1]
            elif b == 1:
                result *= numbers[index+1]
            else:
                result = result*10**(len(f"{numbers[index+1]}")) + numbers[index+1]
        if result == goal:
            return goal
    return 0

result = 0
for row in data.split("\n"):
    result += checkRow(row)

print(result)