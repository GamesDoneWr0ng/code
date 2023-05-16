from pylab import *
import math

ax = plt.axes(projection='3d')

breddegrad = math.radians(60.3913)
f = 1.46 * 10**-4 * np.sin(breddegrad)
v = 10 ** -2
d = math.sqrt((2 * v) / abs(f))

tx = -15
ty = 0

def a(z):
    return (math.sqrt(2)/(1000 * f * d)) * e ** (z/d) * (tx * np.cos(z/d + math.pi/4) - ty * np.sin(z/d + math.pi/4))

def b(z):
    return (math.sqrt(2)/(1000 * f * d)) * e ** (z/d) * (tx * np.sin(z/d + math.pi/4) + ty * np.sin(z/d + math.pi/4))

zline = np.linspace(-100, 0, 10000)
xline = a(zline)
yline = b(zline)

ax.plot3D(xline, yline, zline, 'red')

show()