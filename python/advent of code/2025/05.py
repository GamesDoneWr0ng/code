with open("data/05.txt") as f:
    ranges, ids = f.read().split("\n\n")

# ranges, ids = """3-5
# 10-14
# 16-20
# 12-18
#
# 1
# 5
# 8
# 11
# 17
# 32""".split("\n\n")

ranges = list(map(lambda x: list(map(int, x.split("-"))), ranges.split("\n")))
# ids = list(map(int, ids.split("\n")))
#
# count = 0
# for id in ids:
#     for low, high in ranges:
#         if low <= id <= high:
#             count += 1
#             break
#
# print(count)

i = 0
while i < len(ranges):
    low, high = ranges[i]
    for idx, (l, h) in enumerate(ranges):
        if idx == i:
            continue
        if high+1 < l or low-1 > h:
            continue
        ranges[idx][0] = min(l, low)
        ranges[idx][1] = max(h, high)
        ranges.pop(i)
        i = 0
        break
    else:
        i += 1

count = 0
for low, high in ranges:
    count += high - low + 1

print(count)