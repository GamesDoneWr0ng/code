class Produkt:
    def __init__(self, navn, kilopris) -> None:
        self.navn = navn
        self.kilopris = kilopris

    def __str__(self) -> str:
        return f"{self.navn}, Kilopris: {self.kilopris}"

    def fåKilopris(self):
        return self.kilopris
    
    def fåNavn(self):
        return self.navn