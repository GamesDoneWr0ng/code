import math
while True:
    formel = int(input("Hvilken formel? (abc(1), linkning sett(2), ulikheter(3)) "))

    #abc formel 
    #krever form:
    #ax^2 + bx + c = 0
    if formel == 1:
        print("ax^2 + bx + c = 0")
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))

        d = b**2-4*a*c
        if d < 0:
            print(str(d) + ", negativt tall under rota ingen løsning.")

        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print("x1: ", x1, " x2: ", x2)

    #linkningsett 
    #krever form:
    #ax + by = c
    #dx + ey = f
    elif formel == 2:
        print("ax + by = c")
        print("dx + ey = f")
        a = input("A: ")
        b = input("B: ")
        c = input("C: ")
        d = input("D: ")
        e = input("E: ")
        f = input("F: ")

        if a*e-b*d == 0:
            print("Kan ikke dele på 0 ingen løsning.")
        else:
            x = (c*e - b*f) / (a*e - b*d)
            y = (a*f - c*d) / (a*e - b*d)
            print("x:", x, "y:", y)

    #ulikheter
    #krever form:
    #ax^2 + bx + c < 0
    elif formel == 3:
        print("ax^2 + bx + c < 0")
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))

        if a == 0:
            print(str(a)+": kan ikke dele på 0")

        d = b**2-4*a*c
        
        if d < 0:
            raise ValueError

        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)

        if a < 0:
            print("x <", x1, ", x >", x2)
        else:
            print(x2, "< x <", x1)
    
    else:
        break