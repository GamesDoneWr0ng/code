import z3

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
    opt = z3.Optimize()
    b = [z3.Int(f"b_{i}") for i in range(len(buttons))]
    sums = [z3.Sum([b[j] for j in range(len(buttons)) if i in buttons[j]]) == joltage[i] for i in range(len(joltage))]
    positive = [i>=0 for i in b]

    for c in sums + positive:
        opt.add(c)

    total = z3.Sum(b)
    opt.minimize(total)

    if opt.check() == z3.sat:
        model = opt.model()
        return model.eval(total).as_long()
    else:
        print("Unsatisfiable")

a = b = 0
for i, (battery, *buttons, jolts) in enumerate(map(lambda x: x.split(" "), data)):
    # print(i)
    battery = int(battery[-2:0:-1].replace(".","0").replace("#","1"), 2)
    buttons1 = list(map(lambda x: sum(2**i for i in eval(x.replace(")", ",)"))), buttons))
    buttons2 = list(map(lambda x: eval(x.replace(")", ",)")), buttons))
    joltage = list(eval(f"({jolts[1:-1]},)"))

    a += findMin1(battery, buttons1)
    b += findMin2(joltage, buttons2)

print(a, b)