class Vehicle:
    """Class for making a Vehicle."""
    def __init__(self, numberplate: str, brand: str, model: str, owner: str, fuel: str) -> None:
        """Constructor"""
        self.numberplate = numberplate
        self.brand = brand
        self.model = model
        self.owner = owner
        self.fuel = fuel # Instead of creating more classes for electric and gas cars i simply add one field(fancy word for variable of a class) that stores if its a electric or gas car.
    
    def __str__(self) -> str:
        """Used by print."""
        return f"{self.brand:<8} model {self.model:<3} numberplate {self.numberplate:<10} owned by {self.owner:<10} fueltype {self.fuel}"
    
    def info(self) -> str:
        """Same as __str__ but only returns the data without labels. I use this when printing out the whole trafikksystem."""
        return f"{self.brand:<8} {self.model:<5} {self.numberplate:<11} {self.owner:<10} {self.fuel}"