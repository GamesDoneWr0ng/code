from itertools import product, permutations

with open("data/10.txt") as f:
    data: list[str] = f.read().split("\n")


# data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".split("\n")

def findMin1(battery, buttons):
    moves = 0
    states = {battery}
    nextStates = set()
    while True:
        moves += 1
        for state in states:
            for button in buttons:
                if state ^ button == 0:
                    return moves
                nextStates.add(state ^ button)

        states = nextStates
        nextStates = set()

def findMin2(joltage, buttons):
    rules = [[j for j in range(len(buttons)) if i in buttons[j]] for i in range(len(joltage))]

    bonus = 0
    lower = [0 for _ in joltage]
    found = True
    while found:
        found = False
        # subsets
        for i in range(len(rules)):
            for j in range(len(rules)):
                if i == j:
                    continue
                if set(rules[i]).issubset(set(rules[j])):
                    found = True
                    if len(rules[i]) == len(rules[j]):
                        rules.pop(j)
                        joltage.pop(j)
                        lower.pop(j)
                        break
                    for el in rules[i]:
                        rules[j].remove(el)
                    joltage[j] -= joltage[i]
                    break
            else:
                continue
            break

        # size 1
        for i in range(len(rules)):
            if len(rules[i]) == 0:
                found = True
                rules.pop(i)
                joltage.pop(i)
                lower.pop(i)
                break
            elif len(rules[i]) == 1:
                found = True
                button = rules.pop(i)[0]
                presses = joltage.pop(i)
                bonus += presses
                lower.pop(i)
                for idx, rule in enumerate(rules):
                    if button in rule:
                        rule.remove(button)
                        joltage[idx] -= presses
                break

    buttons = [[y for y in range(len(joltage)) if x in rules[y]] for x in range(max(j for i in rules for j in i) + 1)]

    def isValid(presses, rules, joltage):
        return all(sum(presses[j] for j in rules[i]) == joltage[i] for i in range(len(rules)))

    return bonus + sum(min(filter(lambda p: isValid(p, rules, joltage), product(*(range(min((joltage[i] for i in button), default=0) + 1) for button in buttons))), key=sum))


a = b = 0
for i, (battery, *buttons, jolts) in enumerate(map(lambda x: x.split(" "), data)):
    print(i)
    battery = int(battery[-2:0:-1].replace(".", "0").replace("#", "1"), 2)
    buttons1 = list(map(lambda x: sum(2 ** i for i in eval(x.replace(")", ",)"))), buttons))
    buttons2 = list(map(lambda x: eval(x.replace(")", ",)")), buttons))
    joltage = list(eval(f"({jolts[1:-1]},)"))

    # a += findMin1(battery, buttons1)
    b += findMin2(joltage, buttons2)
    # print(findMin2(joltage, buttons2))

print(a, b)