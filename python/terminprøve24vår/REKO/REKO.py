from collections import Counter
import datetime
from person import Person
from eple import Eple
from mel import Mel

class REKO:
    def __init__(self) -> None:
        self.personer = []
        self.produkter = Counter()

    def leggTilPerson(self, person: Person):
        self.personer.append(person)
    
    def leggTilProdukter(self, produkter):
        self.produkter += produkter

    def fåProdukter(self):
        return self.produkter
    
    def fjærnProdukter(self, produkter):
        self.produkter -= produkter
    
ola = Person("Ola Nordmann", "12345678")
bob = Person("Bob Nordmann", "87654321")
reko = REKO()

reko.leggTilPerson(ola)
reko.leggTilPerson(bob)

ola.selg(Counter([Eple("Gravsten", 56, "Rød"), 
                  Mel("Spelt", 44, datetime.datetime.now())]), reko)

print(bob.bestil(reko))