chickens = 150000
eggpermin = 214000000
intHatchery = 4718 * 2*4

goal = 250000000000
eggs = 0
mins = 0
eggperchicken = eggpermin / chickens
while eggs < goal:
    eggs += eggperchicken * chickens
    chickens += intHatchery
    mins += 1

print(mins)