år = int(input("år: "))

def påskedag(år):
    a = år % 19                             # Del årstallet med 19, forkast resultatet, men behold resten, a.
    b = år // 100                           # Del årstallet med 100, behold resultatet, b, 
    c = år %  100                           # og resten, c.
    d = b // 4                              # Del b med 4, behold resultatet, d,
    e = b %  4                              # og resten, e.
    f = (b + 8) // 25                       # Del b + 8 med 25 og behold resultatet, f,
    g = (b - f + 1) // 3                    # Del b - f + 1 med 3 og behold resultatet, g,
    h = (19 * a + b - d - g + 15) % 30      # Del 19  a + b - d - g + 15 med 30 forkast resultatet og behold resten, h.
    i = c // 4                              # Del c med 4, behold resultatet, i,
    k = c %  4                              # og resten, k.
    l = (32 + 2 * e + 2 * i - h - k) % 7    # Del 32 + 2 * e + 2 * i - h - k med 7 forkast resultatet og behold resten, l.
    m = (a + 11 * h + 22 * l) // 451        # Del a + 11 * h + 22 * l med 451 forkast resultatet og behold resten, m.
    n = (h + l - 7 * m + 114) // 31         # Del h + l - 7 * m + 114 med 31 forkast resultatet og behold resten, n.
    p = (h + l - 7 * m + 114) %  31         # Del h + l - 7 * m + 114 med 31 forkast resultatet og behold resten, p.
    return n, p + 1 

for i in range(2000, 2100):
    print(f"{i}: {påskedag(i)}")