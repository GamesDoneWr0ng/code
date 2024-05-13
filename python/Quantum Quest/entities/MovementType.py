class MovementType:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, MovementType):
            return self.name == other.name
        return False
    
SELF = MovementType("SELF")
PLAYER = MovementType("PLAYER")