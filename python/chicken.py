chickens = 30618
eggpermin = 35991497
intHatchery = 5544 * 2*4

goal = 3_000_000_000_000
eggs = 0
mins = 0
eggperchicken = eggpermin / chickens
while eggs < goal:
    eggs += eggperchicken * chickens
    chickens += intHatchery
    mins += 1

print(mins)
