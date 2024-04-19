a = [8, 5, 2, 6, 12]
n = len(a)

swapped = True                  # lagrer om vi har gjort en swap denne iterasjonen
while swapped:                  # fram til hele listen er sortet
    swapped = False             # reseter swap variabelen
    i = 0                       # starter på første element
    for i in range(i, n-1):     # går gjennom alle elementene i listen
        if a[i] > a[i+1]:       # sjekker om vi har en swap
            swapped = True      # lagrer at listen ikke er sortert enda
            a[i], a[i+1] = a[i+1], a[i] # python aksepterer dette for å swappe 2 elementer

print(a)