from collections import Counter

with open("data/11.txt") as f:
    data = f.read().splitlines()

# data = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out""".splitlines()

connections = dict()
for i, *connected in map(str.split, data):
    connections[i[:-1]] = connected
connections["out"] = []

paths = Counter()
paths["dac"] = 1
nextPaths = Counter()

a = 0
while len(paths) != 0:
    for source, n in paths.items():
        for path in connections[source]:
            if path == "out":
                a += n
                continue
            nextPaths[path] += n
    paths = nextPaths
    nextPaths = Counter()

print(a)

# svr -> fft = 6296
# fft -> dac = 9252947
# dac -> out = 5034
# svr -> out = 293263494406608