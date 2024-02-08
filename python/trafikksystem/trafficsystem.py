from vehicle import Vehicle
from electricCar import Electric
from gasCar import GasCar
import datetime
import bisect

class TrafficSystem:
    """Traffic system to register and count passing cars."""
    def __init__(self) -> None:
        """Constructor, makes a carRegister dict and a passingsRegister list"""
        self.carRegister: dict = {} # Cars that exist in a actual implementation this could be a actual database
        self.passingRegister = [] # sorted by timestamp

    def registerCar(self, car: Vehicle) -> None:
        """Add a car to the registry."""
        self.carRegister[car] = car

    def registerPassing(self, car: Vehicle, time: int) -> None:
        """Register a Passing. Expects cars tp pass in chronological order. A actual implementation should use time.now(), but this program takes in a time for testing purpocess."""
        self.passingRegister.append((car, time))

    def getPassingsByDate(self, date) -> list:
        """Returns a list of passings for a given date."""
        # binary search for fun and O(logN)
        dates = [i[1].date() for i in self.passingRegister]
        start = bisect.bisect_left(dates, date)
        end = bisect.bisect_right(dates, date)
        return self.passingRegister[start:end]

    def getMostPassings(self):
        """Returns what date has the most passings and what hour of that day that has the most passings."""
        dates = [i[1].date() for i in self.passingRegister] # list of just the dates
        date = max(set(dates), key=lambda x: dates.count(x)) # get max date

        passings = self.getPassingsByDate(date)
        hours = [i[1].hour for i in passings]
        hour = max(set(hours), key=lambda x: hours.count(x)) # get hour with most passings

        return date, hour

    def getMostPassedVehicle(self) -> Vehicle:
        """Returns the car that has the most passings."""
        vehicles = [i[0] for i in self.passingRegister]             # list of only the vehicles
        maxPassing = max(set(vehicles), key=lambda x: vehicles.count(x)) # Get most frequent car

        return maxPassing
    
    def __str__(self) -> str:
        """Displays info about the traficsystem"""
        pass

# testing
car1 = Electric("EK 12345", "Tesla", "3", "Ask")
car2 = GasCar("UI 84623", "Toyota", "IDK", "Someone", "Lead")

print(car1)
print(car2)

trafficSystem = TrafficSystem()

trafficSystem.registerCar(car1)
trafficSystem.registerCar(car2)

trafficSystem.registerPassing(car2, datetime.datetime.fromtimestamp(1))
trafficSystem.registerPassing(car1, datetime.datetime.fromtimestamp(999999))
trafficSystem.registerPassing(car2, datetime.datetime.fromtimestamp(1000000))
trafficSystem.registerPassing(car2, datetime.datetime.fromtimestamp(10000000))
trafficSystem.registerPassing(car2, datetime.datetime.fromtimestamp(100000000))
trafficSystem.registerPassing(car1, datetime.datetime.now())

print(trafficSystem.getMostPassedVehicle())
print(trafficSystem.getMostPassings())