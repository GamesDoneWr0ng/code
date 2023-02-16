from pylab import *
from math import e, sin, cos, tan, sqrt, log

# Low number to calculate the derivitive
delta_x = 1E-8
""" 
Small number to calculate the derivitive from

Type: float
"""

def f(graf: str, x: np.ndarray) -> np.ndarray:
    """
    Takes a graf and a x value and returns the y value of the graf at the given x value

    Parameters
    ----------
    graf:
        Type: str
        Description: The graf to put x into
    x: 
        Type: numpy.ndarray
        Description: x value to put into f(x)

    Returns
    -------
    y:
        Type: numpy.ndarray
        Description: y value in the graf for the given x value

    Exsamples
    ---------
    x_values = linspace(-5, 5, 100)



    y_values = f("x**2 + 2*x", x_values)

    y_values = f("5*x**2 + x - 5", x_values)

    y_values = f("3x**3 + 5*x + 9", x_values)

    y_values = f("2x**2 + x", x_values)
    """

    # Creates a list to store y values in
    y_values = []

    # Loops thro all x values and calculates y for all of them
    for i in x:

        # Puts x into the graf returning y as an expresjon
        y = graf.replace("x", f"({str(i)})")

        # Calculates the expresjon and returns an integer
        y = eval(y)

        # Adds y to the list of y values
        y_values.append(y)

    # Returns list of y values as an array
    return np.array(y_values)



def derivert(graf: str, x: np.ndarray) -> np.ndarray:
    """
    Takes an x value and returns the derivitive of f of that x value

    Parameters
    ----------
    graf:
        Type: str
        Description: The graf to put x into
    x: 
        Type: np.ndarray
        Description: x value to put into the derivitive of f

    Returns
    -------
    y:
        Type: np.ndarray
        Description: y value of f'(x) at the given x value
    """

    # Returns the y values
    return (f(graf, x + delta_x) - f(graf, x)) / delta_x



def nullPunkter(x_values: list, y_values: list) -> None:
    """
    Finds all values where y is equal to 0 and draws a point there

    If a y value is positive and the next one is negative, draw a point inbetween the two points

    Parameters
    ----------
    y_values:
        Type: list
        Description: List of points representing y values of a graf
    
    Returns
    -------
    None
    """

    # Last y value checked
    lastY = y_values[0]

    index = 0

    # Loops thro the values
    for y in y_values:
        x = x_values[index]

        # Checks we need to draw a point
        if (y == 0) or (lastY < 0 and y > 0) or (lastY > 0 and y < 0):

            # Draws the point x, 0
            scatter([x], [0], color="red", zorder = 10)

        # Updates the last y value
        lastY = y
        index += 1



# Asks user for graf to use
graf = input("Graf: ")

# Creates a list of x values to caluclate y values from
x_values = linspace(-5, 5, 101)
"""
List of x values to caluclate y values from

Type: numpy.ndarray
"""

# Calculates all y values from x_values variable
y_values = f(graf, x_values)
"""
List of y values in f(x)

Type: numpy.ndarray
"""

dy_values = derivert(graf, x_values)
"""
List of y values in f'(x)

Type: numpy.ndarray
"""

# Draws the grafs
plot(x_values, y_values)
plot(x_values, dy_values)

# Tegner nullpunkter
nullPunkter(x_values, y_values)
nullPunkter(x_values, dy_values)

# Makes the plot look nice 
grid(True)
xlabel("x")
ylabel("y")
axhline(y=0, color="k", zorder=0)
axvline(x=0, color="k", zorder=0)

# Displays whats been drawn
show()

# 1/5 of the code is code rest is comment



"""
from pylab import *
from math import e, sin, cos, tan, sqrt, log

delta_x = 1E-8

def f(graf, x):
    y_values = []
    for i in x:
        y = graf.replace("x", f"({str(i)})")
        y = eval(y)
        y_values.append(y)
    return np.array(y_values)

def derivert(graf, x):
    return (f(graf, x + delta_x) - f(graf, x)) / delta_x

def nullPunkter(x_values, y_values):
    lastY = y_values[0]
    index = 0
    for y in y_values:
        x = x_values[index]
        if (y == 0) or (lastY < 0 and y > 0) or (lastY > 0 and y < 0):
            scatter([x], [0], color="red", zorder = 10)
        lastY = y
        index += 1

graf = input("Graf: ")

x_values = linspace(-5, 5, 101)
y_values = f(graf, x_values)
dy_values = derivert(graf, x_values)

plot(x_values, y_values)
plot(x_values, dy_values)

nullPunkter(x_values, y_values)
nullPunkter(x_values, dy_values)

grid(True)
xlabel("x")
ylabel("y")
axhline(y=0, color="k", zorder=0)
axvline(x=0, color="k", zorder=0)

show()
"""