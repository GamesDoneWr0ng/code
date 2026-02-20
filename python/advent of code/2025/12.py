with open("data/12.txt") as f:
    data = f.read()

# data = """0:
# ###
# ##.
# ##.
#
# 1:
# ###
# ##.
# .##
#
# 2:
# .##
# ###
# ##.
#
# 3:
# ##.
# ###
# ##.
#
# 4:
# ###
# #..
# ###
#
# 5:
# ###
# .#.
# ###
#
# 4x4: 0 0 0 0 2 0
# 12x5: 1 0 1 0 2 2
# 12x5: 1 0 1 0 3 2"""

*presents, trees = data.split("\n\n")

presents = list(map(lambda x: x.count("#"), presents))

def canFit(size, amounts):
    return sum(presents[i]*amounts[i] for i in range(len(amounts))) <= (size[0] * size[1])

a = 0
for line in trees.splitlines():
    size, *amounts = line.split()
    size = list(map(int, size[:-1].split("x")))
    amounts = list(map(int, amounts))
    a += canFit(size, amounts)

print(a)