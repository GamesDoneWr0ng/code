program = [2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0]
registers = [55593699, 0, 0]

# program = [0,3,5,4,3,0]
# registers = [2024,0,0]

solutions = []

ahead = 2
known = ""
posible = [[] for _ in program]
p = 0
a = 0
k = 0
i = 0
while True:
    if a > 2**(10+ahead*3): # 10 bits ahead is worst case
        if len(posible[p]) != 0:
            posible[p].sort(key=lambda x:int(x,2))
            known = posible[p][0]+known
            print(f"{known:>48}")
            p += 1
            a = 0
            k = 0
            i = 0
        else:
            while len(posible[p]) == 0:
                p -= 1
                if p < 0:
                    print(min(solutions))
                    exit()
                posible[p].pop(0)
                known = known[3:]
            a = 0
            k = 0
            i = 0
            known = posible[p][0]+known
            p += 1
            print(f"{known:>48}")

    if program[i+1] < 4:
        combo = program[i+1]
    else:
        combo = registers[program[i+1]-4]

    match program[i]:
        case 0: # adv
            registers[0] = registers[0] >> combo
        case 1: #bxl
            registers[1] = registers[1] ^ program[i+1]
        case 2: # bst
            registers[1] = combo % 8
        case 3: # jnz
            if registers[0] != 0:
                i = program[i+1]
                continue
        case 4: #bxc
            registers[1] = registers[1] ^ registers[2]
        case 5: # out
            #print(c % 8, end=",")
            if combo % 8 == program[k]:
                k += 1
                if k>=len(program):
                    print(int(f"{a:b}"+known,2))
                    solutions.append(int(f"{a:b}"+known,2))
                    while len(posible[p]) == 0:
                        p -= 1
                        posible[p].pop(0)
                        known = known[3:]
                    a = 0
                    k = 0
                    known = posible[p][0]+known
                    p += 1
                    continue
                if k >= p+ahead:
                    if f"{a:b}".zfill(3)[-3:] not in posible[p]:
                        posible[p].append(f"{a:b}".zfill(3)[-3:])
                    a += 1
                    registers[0] = int(f"{a:b}"+known,2)
                    registers[1] = 0
                    registers[2] = 0
                    i = 0
                    k = 0
                    continue
            else:
                a += 1
                registers[0] = int(f"{a:b}"+known,2)
                registers[1] = 0
                registers[2] = 0
                k = 0
                i = 0
                continue
        case 6: # bdv
            registers[1] = registers[0] >> combo
        case 7: # cdv
            registers[2] = registers[0] >> combo
    i += 2
    if i >= len(program):
        a += 1
        registers[0] = int(f"{a:b}"+known,2)
        registers[1] = 0
        registers[2] = 0
        k = 0
        i = 0
        continue
print(f"\nA: {registers[0]} B:{registers[1]} C:{registers[2]}")
#              101010111111 # 4
#             1101010100000 # 5
#      11000001101010100000 # 6
#   10111110110001010111111 # 7
#10010111110110001010111111 # 7

# 520213226413677 too high