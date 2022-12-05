from pylab import *

x = [-3, -2, -1, 0, 1, 2, 3, 4]
f = [9, 4, 1, 0, 1, 4, 9, 16]

g = zeros(len(x))

for i in range(len(x)-1):
    g[i] = (f[i+1] - f[i]) / (x[i+1] - x[i])

plot(x[:-1], f[:-1])
plot(x[:-1], g[:-1])
grid()
show()