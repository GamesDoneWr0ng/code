import matplotlib.pyplot as plt
import numpy as np

wingSize = 0.35
circlesAmount=4
def wing(t, r):
    radiants = np.deg2rad(t)
    r = np.deg2rad(r)

    circle = wingSize * np.e**np.cos(radiants)
    radius = (circle - np.cos(circlesAmount * radiants)) * np.sin(r*circlesAmount)

    x = np.sin(radiants) * radius * np.cos(r)
    z = np.cos(radiants) * radius
    y = np.sin(r) * radius

    return x,y,z

t, r = np.meshgrid(np.linspace(0,360,180), np.linspace(0,360,180))
x, y, z = wing(t, r)
ax = plt.axes(projection='3d')
ax.plot_surface(x,y,z)
plt.show()