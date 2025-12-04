with open("data/03.txt") as f:
    data = f.read().split("\n")

# data = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111""".split("\n")

def argmax(iterable, key):
    maxIdx = 0
    for i in range(len(iterable)):
        if key(iterable[i]) > key(iterable[maxIdx]):
            maxIdx = i
    return maxIdx

result = 0
for battery in data:
    # maxJolt = int(battery[0])
    # maxIdx = 0
    # for idx, i in enumerate(battery[1:]):
    #     if int(i) > maxJolt:
    #         maxIdx = idx + 1
    #         maxJolt = int(i)

    # if maxIdx == len(battery) - 1:
    #     result += int(max(battery[:-1], key=int) + battery[maxIdx])
    # else:
    #     result += int(battery[maxIdx] + max(battery[maxIdx+1:], key=int))

    res = ""
    idx = -1
    for i in range(12):
        end = -11 + len(res)
        idx += argmax(battery[idx+1 : end if end < 0 else None], key=int) + 1
        res += battery[idx]
    result += int(res)

print(result)