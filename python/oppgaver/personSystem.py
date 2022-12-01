class Person:
    def __init__(self, navn):
        self._navn = navn

    def hentNavn(self):
        return self._navn

class PersonSystem:
    def __init__(self):
        self.personer = []
    
    def leggTilPerson(self, person):
        self.personer.append(person)
        
    def finnPerson(self, navn):
        for i in self.personer:
            if navn == i._navn:
                return i._navn, self.personer.index(i)
        return "Personen er ikke i listen"

personSystem = PersonSystem()

personSystem.leggTilPerson(Person("a"))
personSystem.leggTilPerson(Person("b"))
personSystem.leggTilPerson(Person("c"))
personSystem.leggTilPerson(Person("d"))
personSystem.leggTilPerson(Person("e"))

print(personSystem.finnPerson("c"))