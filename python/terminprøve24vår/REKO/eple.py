from produkt import Produkt

class Eple(Produkt):
    def __init__(self, navn, kilopris, farge) -> None:
        super().__init__(navn, kilopris)
        self.farge = farge

    def __str__(self) -> str:
        return super().__str__() + f" Farge: {self.farge}"

    def fåFarge(self) -> str:
        return self.farge