import random
total = 0
Stop = False
kortstokk = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
def getCard(kortstokk):
    cardn = random.randint(0, 51)
    card = kortstokk[cardn]
    if card == 1:
        eel = str(input("do you want one or eleven? "))
        if eel == "11":
            kortstokk[cardn] = 11
    return card

while not Stop:
    if len(kortstokk)==0:
        Stop = True
    if total > 21:
        Stop = True
    if total == 21:
        print("win!")
        Stop = True
    
    hss = input("Hit, Stand or Stop? ")
    if hss.lower() == "hit":
        card = getCard(kortstokk)
        print(card)
        total = total + int(card)
        print("total: " + str(total))
    elif hss.lower() == "stand":
        print("stand")
        card = getCard(kortstokk)
        print(card)
        print("total: " + str(total))
    else:
        print("Stop")
        Stop = True