with open("data/01.txt") as f:
    data = f.readlines()

# data = """L250""".split("\n")

newData = ""
for line in data:
    newData += (line[0] + "1\n") * int(line[1:])

dial = 50
count = 0
# lastZero = False
for line in newData.strip().split("\n"):

    # dial += (1 if line[0] == "R" else -1) * int(line[1:])
    # if dial >= 100 or dial < 0:
    #     zeros, dial = divmod(dial, 100)
    #     count += abs(zeros)
    #     if lastZero and line[0] == "L" and int(line[1:]) % 100 != 0:
    #         count -= 1
    # elif dial == 0:
    #     count += 1

    # lastZero = dial == 0

    dial = (dial + (1 if line[0] == "R" else -1) * int(line[1:])) % 100
    if dial == 0:
        count += 1

print(count)