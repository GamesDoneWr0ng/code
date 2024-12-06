import numpy as np
data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
data = """3|1

1,2,3,4,5"""

def getNumbers(string):
    result = []
    for number in string.strip().replace("  ", " ").split(","):
        result.append(int(number))
    return result

rulesData, listsData = data.split("\n\n")

rules = [[int(rule[:1]), int(rule[2:])] for rule in rulesData.split("\n")]
lists = [getNumbers(i) for i in listsData.split("\n")]

def comp(a,b) -> bool:
    for rule in rules:
        if a in rule and b in rule:
            return a == rule[0]
    return True

countedLists = [False for _ in lists]
for index, list in enumerate(lists):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(list)):
            for j in range(i+1, len(list)):
                if not comp(list[i], list[j]):
                    #print(list, i, j)
                    countedLists[index] = True
                    sorted = False
                    list.insert(j+1, list.pop(i))
        if sorted:
            break

sum = 0
for i in range(len(lists)):
    if countedLists[i]:
        sum += lists[i][len(lists[i])//2]
        print(lists[i])
print(sum)