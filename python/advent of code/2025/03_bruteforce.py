from functools import cache

with open("data/03.txt") as f:
    data = f.read().split("\n")

# data = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111""".split("\n")

@cache
def solve(battery, chosen):
    if len(battery) + chosen < 12 or len(battery) == 0:
        return ""
    if chosen == 11:
        return max(battery, key=int)

    return max(battery[0] + solve(battery[1:], chosen+1) or 0, solve(battery[1:], chosen) or 0, key=int)

total = 0
for battery in data:
    total += int(solve(battery, 0))

print(total)