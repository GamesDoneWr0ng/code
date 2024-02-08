chickens = 16514
eggpermin = 16021822
intHatchery = 4087 * 2*4

goal = 100_000_000_000
eggs = 0
mins = 0
eggperchicken = eggpermin / chickens
while eggs < goal:
    eggs += eggperchicken * chickens
    chickens += intHatchery
    mins += 1

print(mins)

# tacyoon 1h 20min
# dilithium 5h 46min
# antimatter 5h 9min