from entities.ai.abilities.ability import Ability

class Walk(Ability):
    def __init__(self, maxSpeed, accel, reduce, airMult):
        super.__init__("walk")
        self.maxSpeed = maxSpeed
        self.accel = accel
        self.reduce = reduce
        self.airMult = airMult

    def canConnect(self, pos1, pos2):
        pass

    def update(self):
        pass