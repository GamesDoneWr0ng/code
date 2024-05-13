from eple import Eple
from mel import Mel

class Person:
    def __init__(self, navn, mobil) -> None:
        self.navn = navn
        self.mobil = mobil
    
    def fåNavn(self):
        return self.navn
    
    def fåMobil(self):
        return self.mobil
    
    def bestil(self):
        pass

    def selg(self):
        pass