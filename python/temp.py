from pylab import *

def f(x):
    return np.array([i^10 for i in x])

linX = np.array(range(-100, 100))
linY = f(linX)

plot(linX, linY)

grid(True)
xlabel("x")
ylabel("y")
axhline(y=0, color="k", zorder=0)
axvline(x=0, color="k", zorder=0)

show()