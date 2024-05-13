from produkt import Produkt

class Mel(Produkt):
    def __init__(self, navn, kilopris, bestFør) -> None:
        super().__init__(navn, kilopris)
        self.bestFør = bestFør

    def __str__(self) -> str:
        return super().__str__() + f" Best før: {self.bestFør}"

    def fåBestFør(self) -> int:
        return self.bestFør