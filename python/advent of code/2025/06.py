from math import prod
with open("data/06.txt") as f:
    data = f.read().split("\n")

# why u not saving my spaces
# hardcode my input
data[3] += " "
data[4] += "   "

# data = """123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +  """.split("\n")

# nums = []
# for line in data[:-1]:
#     nums.append(list(map(int, [i for i in line.strip().split(" ") if i])))
#
# total = 0
# for idx, op in enumerate([i for i in data[-1].strip().split(" ") if i]):
#     if "+" in op:
#         total += sum(line[idx] for line in nums)
#     else:
#         total += prod(line[idx] for line in nums)
#
# print(total)


lengths = []
l = 1
for i in data[-1][1:]:
    if i == " ":
        l += 1
    else:
        lengths.append(l)
        l = 1
lengths.append(l+1)

idx = 0
total = 0
for length in lengths:
    nums = []
    for i in range(length - 1):
        num = ""
        for digit in range(len(data) - 1):
            num += data[digit][idx + i]
        nums.append(int(num))

    if data[-1][idx] == "+":
        total += sum(nums)
    else:
        total += prod(nums)

    idx += length

print(total)