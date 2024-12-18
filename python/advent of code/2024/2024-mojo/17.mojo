fn main():
    var program: List[Int] = List[Int](2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0)
    var registers: List[Int] = List[Int](0, 0, 0)

    var a: Int = 0
    var k: Int = 0
    var i: Int = 0
    var c: Int
    while True:
        if program[i+1] < 4:
            c = program[i+1]
        else:
            c = registers[program[i+1]-4]
        if program[i] == 0:
            registers[0] = registers[0] >> c
        elif program[i] == 1:
            registers[1] = registers[1] ^ program[i+1]
        elif program[i] == 2:
            registers[1] = c % 8
        elif program[i] == 3:
            if registers[0] != 0:
                i = program[i+1]
                continue
            elif program[i] == 4:
                registers[1] = registers[1] ^ registers[2]
            elif program[i] == 5:
                if (c % 8) == program[k]:
                    k += 1
                if k >= 5:
                    print(a)
                    break
            else:
                a += 1
                if a % 100000000 == 0:
                    print(a)
                registers[0] = a
                registers[1] = 0
                registers[2] = 0
                k = 0
                i = 0
                continue
        elif program[i] == 6:
            registers[1] = registers[0] >> c
        else:
            registers[2] = registers[0] >> c
        i += 2
        if i >= len(program):
            a += 1
            if a % 100000000 == 0:
                print(a)
            registers[0] = a
            registers[1] = 0
            registers[2] = 0
            k = 0
            i = 0
            continue