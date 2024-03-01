from vehicle import Vehicle
import datetime
import bisect

class TrafficSystem:
    """Traffic system to register and count passing cars."""
    def __init__(self) -> None:
        """Constructor, makes a carRegister dict and a passingsRegister list"""
        self.carRegister: dict = {} # Cars that exist. In a actual implementation this could be a actual database
        self.passingRegister: list[tuple[Vehicle, datetime.datetime]] = [] # sorted by timestamp
        """You could make a class for one passing with a vehicle field(fancy word for variable) and a timestamp field.
        However since it would only have 2 fields and nothing else i opted for using a tuple(like a list but it is imutable(you cant change it after creating it)) to store the data.
        The resulting structure can be represented as this:
        [(car1, time1),
         (car2, time2),
         (car3, time3)]
        Here you have a list of passings that you can access as a list. passingRegister[0] will return (car1, time1)
        You can access the data of a passing by calling passing[0] or passing[1] witch returns the car and the timestamp respectfuly.
        """

    def registerCar(self, car: Vehicle) -> None:
        """Add a car to the registry."""
        self.carRegister[car.numberplate] = car

    def registerPassing(self, car: Vehicle, time: int = datetime.datetime.now()) -> None:
        """Register a Passing. Expects cars to pass in chronological order. A actual implementation should use time.now(), but this program takes in a time for testing purpocess."""
        self.passingRegister.append((car, time))

    def getPassingsByDate(self, date: datetime.date) -> list:
        """Returns a list of passings for a given date."""
        dates = [i[1].date() for i in self.passingRegister] # creates a list of only the dates.
        """The method i used is called list comprehension. It does the same as:
        dates = [] # make a empty list of dates
        for i in self.passingRegister: # iterate over all passings
            dates.append(i[1].date()) # i[1] is the timestamp, i[1].date() is the date. Append the date to the list.

        I use this quite often and is a very nice, fast and compact way to do things.
        """

        # binary search for fun and O(logN) speed, O(logN) means fast
        # You could simply use a for loop to find the leftmost instance of the target date, but bisect does it faster.
        start = bisect.bisect_left(dates, date) # finds the leftmost instance of the target date
        end = bisect.bisect_right(dates, date) # finds the rightmost instance of the target date
        return self.passingRegister[start:end] # we know that the passings are sorted by timestamp so all elements between the first and the last instance will also be on the same date.

    def getMostPassings(self):
        """Returns what date has the most passings and what hour of that day that has the most passings."""
        dates = [i[1].date() for i in self.passingRegister] # list of just the dates
        date = max(set(dates), key=dates.count) # get max date
        """The max function returns the element in a iterable(fancy word for list), however we want the date that ocurrs the most often.
        To do this we use a set and the key=dates.count function. The set doesn't allow duplicates so it only has one instance of each date.
        The key part is what function it should use to compare values. If we didn't include this it would try to do date1 < date2.
        This would return the most recent data or simply an error. With dates.count it will pass each element into dates.count before comparing them.
        This means it does dates.count(date1) < dates.count(date2). 
        This returns the most frequent date since dates.count is a function of lists that returns the amount of ocurences in the list of the given element."""

        passings = self.getPassingsByDate(date) # get the passings for that date
        hours = [i[1].hour for i in passings]   # list of just the hours
        hour = max(set(hours), key=hours.count) # get hour with most passings

        return date, hour

    def getMostPassedVehicle(self) -> Vehicle:
        """Returns the car that has the most passings."""
        vehicles = [i[0] for i in self.passingRegister]     # list of only the vehicles
        maxPassing = max(set(vehicles), key=vehicles.count) # Get most frequent car

        return maxPassing
    
    def __str__(self) -> str:
        """Displays info about the traficsystem"""
        cars = "\n".join([str(i) for i in self.carRegister.values()]) # .join is a function of strings that takes in a iterable and returns a string of each element seperated by the string. Since "\n" is a newline this will return "car1 (newline) car2 (newline), car3"
        passes = "\n".join([f"{str(i[1]):<27}" + self.carRegister[i[0]].info() for i in self.passingRegister]) # same as above but making the list is a bit more complicated. f"{str(i[1]):<27}" takes the timestamp of the passing i[1], then converts it to a string with str(), it then uses string formating to make the string at least 27 characters long by filling it up with spaces on the right if it is to short. It then adds info about the car to the string.
        return f"Registered cars:\n{cars}\n\nPassings:                  Brand    Model Numberplate Owner      Fueltype \n{passes}"

# testing
car1 = Vehicle("EK 12345", "Tesla", "3", "Ask", "Electric")
car2 = Vehicle("UI 84623", "Toyota", "IDK", "Someone", "Lead")

print(car1)
print(car2)

trafficSystem = TrafficSystem()

trafficSystem.registerCar(car1)
trafficSystem.registerCar(car2)

trafficSystem.registerPassing("UI 84623", datetime.datetime.fromtimestamp(1))
trafficSystem.registerPassing("EK 12345", datetime.datetime.fromtimestamp(999999))
trafficSystem.registerPassing("UI 84623", datetime.datetime.fromtimestamp(1000000))
trafficSystem.registerPassing("UI 84623", datetime.datetime.fromtimestamp(10000000))
trafficSystem.registerPassing("UI 84623", datetime.datetime.fromtimestamp(100000000))
trafficSystem.registerPassing("EK 12345")

print(trafficSystem.getMostPassedVehicle())
print(trafficSystem.getMostPassings())

print(trafficSystem)