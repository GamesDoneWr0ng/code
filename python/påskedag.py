år = int(input("år: "))

def påskedag(år):
    a = år % 19
    b = år // 100
    c = år %  100
    d = b // 4
    e = b %  4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c %  4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    n = (h + l - 7 * m + 114) // 31
    p = (h + l - 7 * m + 114) %  31
    return n, p + 1 

for i in range(2000, 2100):
    print(f"{i}: {påskedag(i)}")