class Vehicle:
    """Class for making a Vehicle."""
    def __init__(self, registerNumber: str, brand: str, model: str, owner: str) -> None:
        """Constructor"""
        self.registerNumber = registerNumber
        self.brand = brand
        self.model = model
        self.owner = owner

    def __hash__(self) -> int:
        """Return the hash of the registerNumber. Used for dictonary and set keys."""
        return hash(self.registerNumber)
    
    def getType(self) -> str:
        """Return the type of car."""
        raise NotImplementedError
    
    def __str__(self) -> str:
        return f"{self.brand} model {self.model} registernumber {self.registerNumber} owned by {self.owner}"