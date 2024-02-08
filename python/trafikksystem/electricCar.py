from vehicle import Vehicle
class Electric(Vehicle):
    """Class for a electric car."""
    def __init__(self, registerNumber: str, brand: str, model: str, owner: str) -> None:
        """Constructor"""
        super().__init__(registerNumber, brand, model, owner)

    def getType(self):
        """Return the type of car."""
        return "Electric"