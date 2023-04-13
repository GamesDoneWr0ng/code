import numpy as np

with open("resources/dictonaryEn.txt", "r") as file:
    words = file.readlines()

counts = {"a": 0,
          "b": 0,
          "c": 0,
          "d": 0,
          "e": 0,
          "f": 0,
          "g": 0,
          "h": 0,
          "i": 0,
          "j": 0,
          "k": 0,
          "l": 0,
          "m": 0,
          "n": 0,
          "o": 0,
          "p": 0,
          "q": 0,
          "r": 0,
          "s": 0,
          "t": 0,
          "u": 0,
          "v": 0,
          "w": 0,
          "x": 0,
          "y": 0,
          "z": 0,}

percent = counts.copy()
codes = counts.copy()

# counts
for word in words:#[:10000]:
    for letter in word[:-2]:
        counts[letter] += 1

# percentages
cSum = 0
for i in counts:
    cSum += counts[i]
for i in counts:
    percent[i] = counts[i] / cSum

# entropy
entropy = 0
for i in percent:
    entropy += percent[i] * -np.log2(percent[i])

# make morse 0. 1-
morsePercentages = list(percent.copy().values())
for i in range(26):
    code = f"{i:b}"
    min = list(percent.keys())[np.argmax(morsePercentages)]
    codes[min] = code
    morsePercentages[list(percent.keys()).index(min)] = -1

# second entropy
e2Sum = 0
for i in codes:
    e2Sum += len(codes[i]) * percent[i]

# print
for i in codes:
    print(f"{i}: {codes[i]}".replace("0",".").replace("1","-"))