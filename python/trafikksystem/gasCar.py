from vehicle import Vehicle
class GasCar(Vehicle):
    """Class for a gas powerd car."""
    def __init__(self, registerNumber: str, brand: str, model: str, owner: str, fuel: str) -> None:
        """Constructor"""
        super().__init__(registerNumber, brand, model, owner)
        self.fuel = fuel

    def getType(self):
        """Return the type of car."""
        return "Gas"
    
    def __str__(self) -> str:
        return super().__str__() + f" fueltype {self.fuel}"