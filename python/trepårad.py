import numpy as np

tabell = np.array([["#", "#", "#"],
                   ["#", "#", "#"],
                   ["#", "#", "#"]])

print(tabell)

ferdig = False
while not ferdig:
    try:
        row = int(input("row: "))
        col = int(input("col: "))
        xo = input("x or o: ")

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Bad")
            continue
        if xo != "x" and xo != "o":
            print("Bad")
            continue
    except:
        print("Bad")
        continue

    tabell[row][col] = xo
    print(tabell)

    # check if game is over
    for i in range(3):
        for k in ["x", "o"]:
            if np.any([np.all(tabell[i] == k),
                       np.all(tabell[:,i] == k),
                       np.all(tabell.diagonal() == k),
                       np.all(np.fliplr(tabell).diagonal() == k)]):
                print(k, "won")
                ferdig = True
                break