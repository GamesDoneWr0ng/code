from random import choice
options = range(1,10)
while len(options) != 0:
    temp = choice(options)
    print(temp)
    options.remove(temp)