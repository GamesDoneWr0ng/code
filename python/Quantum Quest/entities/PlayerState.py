class PlayerState:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, PlayerState):
            return self.name == other.name
        return False
    
NORMAL = PlayerState("NORMAL")
PHOTONDASH = PlayerState("PhotonDash")