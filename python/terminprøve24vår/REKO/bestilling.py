class Bestilling:
    def __init__(self, produkter):
        self.produkter: dict = produkter

    def __str__(self) -> str:
        return "Bestilling:\n"+ '\n'.join([str(k) + ": " + str(v) + "kg" for k, v in self.produkter.items()]) + f"\nTotalpris: {self.totalPris()}"
    
    def totalPris(self):
        s = 0
        for produkt, kilo in self.produkter.items():
            s += produkt.kilopris * kilo
        return s