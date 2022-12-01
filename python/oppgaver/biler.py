class Person: 
    def __init__(self, navn):
        self._mineBiler = [] # Biler personen eier
        self._laanteBiler = [] # Biler som personen laaner, men noen andre eier
        self._navn = navn
    
    def faaBil(self, bil):
        self._mineBiler.append(bil)
    
    def laan(self, person, bilId):
        for i in main.personer:
            if i._navn == person:
                if bilId >= len(i._mineBiler):
                    raise IndexError
                biler = i._mineBiler
                self._laanteBiler.append(biler[bilId])
                biler.pop(bilId)
                
class Bil:
    def __init__(self, farge, merke, eier):
        self.farge = farge
        self.merke = merke
        self.eier = eier

class Main:
    def __init__(self):
        self.personer = []

main = Main()

main.personer.append(Person("a"))
main.personer.append(Person("b"))

a = main.personer[0]
b = main.personer[1]

a.faaBil(Bil("red", "car1", "a"))
a.faaBil(Bil("blue", "car2", "a"))
b.faaBil(Bil("green", "car3", "b"))

print(a._mineBiler)
print(a._laanteBiler)
print(b._mineBiler)
print(b._laanteBiler)

b.laan("a", 1)

print(a._mineBiler)
print(a._laanteBiler)
print(b._mineBiler)
print(b._laanteBiler)
pass