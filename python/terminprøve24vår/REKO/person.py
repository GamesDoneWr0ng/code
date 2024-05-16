from collections import Counter
from bestilling import Bestilling

class Person:
    def __init__(self, navn, mobil) -> None:
        self.navn = navn
        self.mobil = mobil

    def __eq__(self, __value: object) -> bool:
        return self.navn == __value.fåNavn()
    
    def fåNavn(self):
        return self.navn
    
    def fåMobil(self):
        return self.mobil
    
    def bestil(self, reko):
        tilgjengelig: Counter = reko.fåProdukter()
        if sum(tilgjengelig.values()) == 0:
            print("Ingen tilgjengelig produkter.")
            return
        
        print("Tilgjengelig produkter:")
        for index, produkt, mengde in zip(range(len(tilgjengelig)), tilgjengelig.keys(), tilgjengelig.values()):
            if mengde == 0:
                continue
            print(f"{index}: {produkt}: {mengde} kg")
        
        svar = input("Vil du kjøpe noe? y/n ")
        kjøpt = Counter()
        while svar == "y":
            produkt = input(f"Velg produkt 0-{len(tilgjengelig)-1}: ")
            try:
                produkt = int(produkt)
                if produkt < 0 or produkt >= len(tilgjengelig):
                    raise ValueError
            except ValueError:
                print("Ugyldig input.")
                continue

            produkt = list(tilgjengelig.keys())[produkt]

            mengde = input(f"Velg mengde: ")
            try:
                mengde = float(mengde)
                if mengde < 0:
                    raise ValueError
                if tilgjengelig[produkt] < mengde:
                    print("Mengde er for stort.")
                    raise ValueError
            except ValueError:
                print("Ugyldig input.")
                continue

            kjøpt[produkt] += mengde

            svar = input("Vil du kjøpe noe mer? y/n ")

        if sum(kjøpt.values()) == 0:
            return

        bestilling = Bestilling(kjøpt)
        print(bestilling)

        svar = input("Vil du betale? y/n ")
        if svar == "y":
            reko.fjærnProdukter(kjøpt)
            return bestilling
        return None

    def selg(self, produkter, reko):
        reko.produkter += produkter