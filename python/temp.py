from math import e

def f(x):
    return x**2 * e**x

x_1 = 1
x_2 = 1.00000000000001

stigTall = (f(x_2) - f(x_1)) / (x_2 - x_1)

print(stigTall)